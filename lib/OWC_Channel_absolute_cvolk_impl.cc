/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "OWC_Channel_absolute_cvolk_impl.h"
#include <gnuradio/io_signature.h>
#include <volk/volk.h>
#include <numeric>

namespace gr {
namespace owc {


using input_type = float;

using output_type = float;
    OWC_Channel_absolute_cvolk::sptr
    OWC_Channel_absolute_cvolk::make(int num_inputs, int num_outputs, const std::vector<float>& tx_coordinates_array, const std::vector<float>& tx_orientation_array, const std::vector<float>& rx_coordinates_array, const std::vector<float>& rx_orientation_array, const std::vector<float>& tx_lambertian_order_array, const std::vector<float>& rx_photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, bool clip_neg, bool shot_noise, float sample_rate, float responsivity, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array)
    {
      return gnuradio::make_block_sptr<OWC_Channel_absolute_cvolk_impl>(
        num_inputs,
        num_outputs,
        tx_coordinates_array,
        tx_orientation_array,
        rx_coordinates_array,
        rx_orientation_array,
        tx_lambertian_order_array,
        rx_photosensor_area_array,
        optical_filter_transmittance_array,
        refractive_index_array,
        clip_neg,
        shot_noise,
        sample_rate, 
        responsivity,
        concentrator_FOV_array,
        E2O_conversion_factor_array,
        O2E_conversion_factor_array);
    }

    /*
     * The private constructor
     */
    OWC_Channel_absolute_cvolk_impl::OWC_Channel_absolute_cvolk_impl(int num_inputs, int num_outputs, const std::vector<float>& tx_coordinates_array, const std::vector<float>& tx_orientation_array, const std::vector<float>& rx_coordinates_array, const std::vector<float>& rx_orientation_array, const std::vector<float>& tx_lambertian_order_array, const std::vector<float>& rx_photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, bool clip_neg, bool shot_noise, float sample_rate, float responsivity, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array)
      : gr::sync_block("OWC_Channel_absolute_cvolk",
              gr::io_signature::make(1, -1, sizeof(input_type)),
              gr::io_signature::make(1, -1, sizeof(output_type))),
      gen(std::random_device{}())
    {
      set_num_inputs(num_inputs);
      set_num_outputs(num_outputs);
      
      set_tx_lambertian_order_array(tx_lambertian_order_array);
      set_rx_photosensor_area_array(rx_photosensor_area_array);
            
      set_tx_coordinates_array(tx_coordinates_array);
      set_tx_orientation_array(tx_orientation_array);
      set_rx_coordinates_array(rx_coordinates_array);
      set_rx_orientation_array(rx_orientation_array);

      
      set_optical_filter_transmittance_array(optical_filter_transmittance_array);
      set_refractive_index_array(refractive_index_array);
      set_clip_neg(clip_neg);
      set_shot_noise(shot_noise);
      set_sample_rate(sample_rate);
      set_responsivity(responsivity);
      set_concentrator_FOV_array(concentrator_FOV_array);
      set_E2O_conversion_factor_array(E2O_conversion_factor_array);
      set_O2E_conversion_factor_array(O2E_conversion_factor_array);
      set_distance_array();
      set_emission_angle_array();
      set_acceptance_angle_array();
      calculate_channel_model_values();
    }

    /*
     * Our virtual destructor.
     */
    OWC_Channel_absolute_cvolk_impl::~OWC_Channel_absolute_cvolk_impl() {}

    
    int OWC_Channel_absolute_cvolk_impl::work(
        int noutput_items, gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items) {

      int ninputs = input_items.size();
      int noutputs = output_items.size();
      //const float clip = 0.0;

      if(set){
        set_distance_array();
        set_emission_angle_array();
        set_acceptance_angle_array();
        calculate_channel_model_values();
      }

      float* temp_results = (float*)volk_malloc(noutput_items * sizeof(float), volk_get_alignment());
      float* noise_values = (float*)volk_malloc(noutput_items * sizeof(float), volk_get_alignment());
      float* clipped_inputs = (float*)volk_malloc(noutput_items * sizeof(float), volk_get_alignment());
      float* clip = (float*)volk_malloc(noutput_items * sizeof(float), volk_get_alignment());
      std::fill_n(clip, noutput_items, 0.0f);

      for (int x = 0; x < noutputs; x++) {
        float* output_buffer = (float*)output_items[x];

        volk_32f_s32f_multiply_32f(output_buffer, output_buffer, 0.0f, noutput_items);

        for (int j = 0; j < ninputs; j++) {
            int index = x * ninputs + j;
            const float* input_buffer = (const float*)input_items[j];
            float channel_value = channel_model_values[index];

            if (get_clip_neg()) {
              volk_32f_x2_max_32f(clipped_inputs, input_buffer, clip, noutput_items);
            } else {
              std::memcpy(clipped_inputs, input_buffer, noutput_items * sizeof(float));
            }

            volk_32f_s32f_multiply_32f(temp_results, clipped_inputs, channel_value, noutput_items);
            volk_32f_x2_add_32f(output_buffer, output_buffer, temp_results, noutput_items);
        }

        if(get_shot_noise()){
            float P_sum = 0.0f;
            P_sum = std::accumulate(output_buffer, output_buffer + noutput_items, 0.0f);
            /*for(int k = 0; k < noutput_items; k++){
                P_sum += output_buffer[k];
            }*/
            float P_avg = P_sum / noutput_items;
            float std_dev = calculate_shot_noise(P_avg);
            std::normal_distribution<float> noise_dist(0.0f, std_dev);

            std::generate_n(noise_values, noutput_items, [&]() {
                return noise_dist(gen);
            });

            volk_32f_x2_add_32f(output_buffer, output_buffer, noise_values, noutput_items);
        }
      }

      volk_free(temp_results);
      volk_free(noise_values);
      volk_free(clipped_inputs);
      return noutput_items;
    }

    } /* namespace owc */
    } /* namespace gr */
