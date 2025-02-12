/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "OWC_Channel_relative_cpvolk_impl.h"
#include <gnuradio/io_signature.h>
#include <gnuradio/owc/OWC_Channel_relative_cpvolk.h>
#include <volk/volk.h>

namespace gr {
namespace owc {


using input_type = float;

using output_type = float;

OWC_Channel_relative_cpvolk::sptr
OWC_Channel_relative_cpvolk::make(int num_inputs, int num_outputs, const std::vector<float>& emission_angle_array, const std::vector<float>& acceptance_angle_array, const std::vector<float>& distance_array, const std::vector<float>& lambertian_order_array, const std::vector<float>& photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array)
{
    return gnuradio::make_block_sptr<OWC_Channel_relative_cpvolk_impl>(
        num_inputs,
        num_outputs,
        emission_angle_array,
        acceptance_angle_array,
        distance_array,
        lambertian_order_array,
        photosensor_area_array,
        optical_filter_transmittance_array,
        refractive_index_array,
        concentrator_FOV_array,
        E2O_conversion_factor_array,
        O2E_conversion_factor_array);
}


/*
 * The private constructor
 */
OWC_Channel_relative_cpvolk_impl::OWC_Channel_relative_cpvolk_impl(int num_inputs, int num_outputs, const std::vector<float>& emission_angle_array, const std::vector<float>& acceptance_angle_array, const std::vector<float>& distance_array, const std::vector<float>& lambertian_order_array, const std::vector<float>& photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array)
    : gr::sync_block("OWC_Channel_relative_cpvolk",
                     gr::io_signature::make(
                         1 , -1 , sizeof(input_type)),
                     gr::io_signature::make(
                         1 , -1 , sizeof(output_type)))
{
    set_num_inputs(num_inputs);
    set_num_outputs(num_outputs);
    set_emission_angle_array(emission_angle_array);
    set_acceptance_angle_array(acceptance_angle_array);
    set_distance_array(distance_array);
    set_lambertian_order_array(lambertian_order_array);
    set_photosensor_area_array(photosensor_area_array);
    set_optical_filter_transmittance_array(optical_filter_transmittance_array);
    set_refractive_index_array(refractive_index_array);
    set_concentrator_FOV_array(concentrator_FOV_array);
    set_E2O_conversion_factor_array(E2O_conversion_factor_array);
    set_O2E_conversion_factor_array(O2E_conversion_factor_array);
    calculate_channel_model_values();
}

/*
 * Our virtual destructor.
 */
OWC_Channel_relative_cpvolk_impl::~OWC_Channel_relative_cpvolk_impl() {}


int OWC_Channel_relative_cpvolk_impl::work(int noutput_items,
                                           gr_vector_const_void_star& input_items,
                                           gr_vector_void_star& output_items)
{
    int ninputs = input_items.size();
    int noutputs = output_items.size();

    if (set) {
        calculate_channel_model_values();
    }

    float* temp_results = (float*)volk_malloc(noutput_items * sizeof(float), volk_get_alignment());

    for (int x = 0; x < noutputs; x++) {
        float* output_buffer = (float*)output_items[x];
        
        volk_32f_s32f_multiply_32f(output_buffer, output_buffer, 0.0f, noutput_items);
        
        for (int j = 0; j < ninputs; j++) {
            int index = x * ninputs + j;
            const float* input_buffer = (const float*)input_items[j];
            float channel_value = channel_model_values[index];
            
            volk_32f_s32f_multiply_32f(temp_results, input_buffer, channel_value, noutput_items);
            volk_32f_x2_add_32f(output_buffer, output_buffer, temp_results, noutput_items);
        }
    }

    volk_free(temp_results);
    return noutput_items;
}

} /* namespace owc */
} /* namespace gr */
