/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "OWC_Channel_absolute_cvolk_impl.h"
#include <gnuradio/io_signature.h>
#include <volk/volk.h>

namespace gr {
namespace owc {


using input_type = float;

using output_type = float;
    OWC_Channel_absolute_cvolk::sptr
    OWC_Channel_absolute_cvolk::make(int num_inputs, int num_outputs, const std::vector<float>& tx_coordinates_array, const std::vector<float>& tx_orientation_array, const std::vector<float>& rx_coordinates_array, const std::vector<float>& rx_orientation_array, const std::vector<float>& tx_lambertian_order_array, const std::vector<float>& rx_photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array)
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
        concentrator_FOV_array,
        E2O_conversion_factor_array,
        O2E_conversion_factor_array);
    }

    /*
     * The private constructor
     */
    OWC_Channel_absolute_cvolk_impl::OWC_Channel_absolute_cvolk_impl(int num_inputs, int num_outputs, const std::vector<float>& tx_coordinates_array, const std::vector<float>& tx_orientation_array, const std::vector<float>& rx_coordinates_array, const std::vector<float>& rx_orientation_array, const std::vector<float>& tx_lambertian_order_array, const std::vector<float>& rx_photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array)
      : gr::sync_block("OWC_Channel_absolute_cvolk",
              gr::io_signature::make(1, -1, sizeof(input_type)),
              gr::io_signature::make(1, -1, sizeof(output_type)))
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
      unsigned int alignment = volk_get_alignment();

      int ninputs = input_items.size();
      int noutputs = output_items.size();

      if(set == true){
        set_distance_array();
        set_emission_angle_array();
        set_acceptance_angle_array();
        calculate_channel_model_values();
    }

      for (int i = 0; i < noutput_items; i++) {
          for (int x = 0; x < noutputs; x++) {
            float received_power = 0.0f;
            float* temp_results = (float*)volk_malloc(ninputs * sizeof(float), alignment);

            for (int j = 0; j < ninputs; j++) {
                temp_results[j] = ((const float*)input_items[j])[i];
            }

            volk_32f_x2_multiply_32f(temp_results, temp_results, &channel_model_values[x * ninputs], ninputs);


            volk_32f_accumulator_s32f(&received_power, temp_results, ninputs);

            ((float*)output_items[x])[i] = received_power;
            volk_free(temp_results);
        }
    }
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

    } /* namespace owc */
    } /* namespace gr */
