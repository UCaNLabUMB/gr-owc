/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OWC_OWC_CHANNEL_RELATIVE_CPVOLK_IMPL_H
#define INCLUDED_OWC_OWC_CHANNEL_RELATIVE_CPVOLK_IMPL_H

#include <gnuradio/owc/OWC_Channel_relative_cpvolk.h>
#include <random>
#include <algorithm>
#include <cmath>

namespace gr {
namespace owc {

class OWC_Channel_relative_cpvolk_impl : public OWC_Channel_relative_cpvolk
{
private:
    int d_num_inputs = 1;
    int d_num_outputs = 1;
    std::vector<float> d_emission_angle_array;
    std::vector<float> d_acceptance_angle_array;
    std::vector<float> d_distance_array;
    std::vector<float> d_lambertian_order_array; 
    std::vector<float> d_photosensor_area_array;
    std::vector<float> d_optical_filter_transmittance_array;
    std::vector<float> d_refractive_index_array;
    bool d_clip_neg;
    bool d_shot_noise;
    float d_sample_rate;
    float d_responsivity;
    std::vector<float> d_concentrator_FOV_array;
    std::vector<float> d_E2O_conversion_factor_array;
    std::vector<float> d_O2E_conversion_factor_array;
    std::vector<float> channel_model_values;
    bool set = true;
    std::mt19937 gen;

    void calculate_channel_model_values()
      {
      channel_model_values.clear();
      int nout = r_num_outputs();
      int nin = r_num_inputs();
      for (int x = 0; x < nout; x++) {
        for (int j = 0; j < nin; j++) {
            float Gt = 0;
            float Gr = 0;
            float g = 0;
            int index = x * nin + j;
                
            if (emission_angle_array()[index] <= 90)
            {
                Gt = ((lambertian_order_array()[j] + 1)/(2*M_PI))*pow(cos(emission_angle_array()[index]*(M_PI/180)),lambertian_order_array()[j]);
            }
            
            if (std::abs(acceptance_angle_array()[index]) <= concentrator_FOV_array()[x]){
                float Ts = optical_filter_transmittance_array()[x];
                float refractive_index_squared = refractive_index_array()[x]*refractive_index_array()[x]; 
                float sin_of_concentrator_FOV_squared = sin(concentrator_FOV_array()[x]*(M_PI/180))*sin(concentrator_FOV_array()[x]*(M_PI/180));
                g = refractive_index_squared/sin_of_concentrator_FOV_squared;
                Gr = photosensor_area_array()[x]*Ts*g*cos(acceptance_angle_array()[index]*(M_PI/180)); 
            }
            
            float distance_squared = distance_array()[index] * distance_array()[index];
        
            float Ct = E2O_conversion_factor_array()[j];
            float Cr = O2E_conversion_factor_array()[x];
        
            float H = Ct*((Gt*Gr)/distance_squared)*Cr;
            channel_model_values.push_back(H);
          }
        }
        set = false;
    }

    float calculate_shot_noise(float P_avg) {
        const float q = 1.60217663e-19;
        float S_shot = 2 * q * responsivity() * P_avg;
        float variance = S_shot * sample_rate();
        return std::sqrt(variance);
    }

public:
    OWC_Channel_relative_cpvolk_impl(int num_inputs, int num_outputs, const std::vector<float>& emission_angle_array, const std::vector<float>& acceptance_angle_array, const std::vector<float>& distance_array, const std::vector<float>& lambertian_order_array, const std::vector<float>& photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, bool clip_neg, bool shot_noise, float sample_rate, float responsivity,const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array);
    ~OWC_Channel_relative_cpvolk_impl();

    void set_num_inputs(int num_inputs){d_num_inputs = num_inputs; set = true;}
    int r_num_inputs() {return d_num_inputs;}
      
    void set_num_outputs(int num_outputs){d_num_outputs = num_outputs; set = true;}
    int r_num_outputs() {return d_num_outputs;}
      
    void set_emission_angle_array(std::vector<float> emission_angle_array){d_emission_angle_array = emission_angle_array; set = true;}
    std::vector<float> emission_angle_array() {return d_emission_angle_array;}
      
    void set_acceptance_angle_array(std::vector<float> acceptance_angle_array){d_acceptance_angle_array = acceptance_angle_array; set = true;}
    std::vector<float> acceptance_angle_array() {return d_acceptance_angle_array;}
      
    void set_distance_array(std::vector<float> distance_array){d_distance_array = distance_array; set = true;}
    std::vector<float> distance_array() {return d_distance_array;}
      
    void set_lambertian_order_array(std::vector<float> lambertian_order_array){d_lambertian_order_array = lambertian_order_array; set = true;}
    std::vector<float> lambertian_order_array() {return d_lambertian_order_array;}
      
    void set_photosensor_area_array(std::vector<float> photosensor_area_array){d_photosensor_area_array = photosensor_area_array; set = true;}
    std::vector<float> photosensor_area_array() {return d_photosensor_area_array;}
      
    void set_optical_filter_transmittance_array(std::vector<float> optical_filter_transmittance_array){d_optical_filter_transmittance_array = optical_filter_transmittance_array; set = true;}
    std::vector<float> optical_filter_transmittance_array() {return d_optical_filter_transmittance_array;}
      
    void set_refractive_index_array(std::vector<float> refractive_index_array){d_refractive_index_array = refractive_index_array; set = true;}
    std::vector<float> refractive_index_array() {return d_refractive_index_array;}

    void set_clip_neg(bool clip_neg){d_clip_neg = clip_neg;}
    bool get_clip_neg(){return d_clip_neg;}

    void set_shot_noise(bool shot_noise){d_shot_noise = shot_noise;}
    bool get_shot_noise(){return d_shot_noise;}

    void set_sample_rate(float sample_rate){d_sample_rate = sample_rate;}
    float sample_rate() {return d_sample_rate;}

    void set_responsivity(float responsivity){d_responsivity = responsivity;}
    float responsivity() {return d_responsivity;}
      
    void set_concentrator_FOV_array(std::vector<float> concentrator_FOV_array){d_concentrator_FOV_array = concentrator_FOV_array; set = true;}
    std::vector<float> concentrator_FOV_array() {return d_concentrator_FOV_array;}
      
    void set_E2O_conversion_factor_array(std::vector<float> E2O_conversion_factor_array){d_E2O_conversion_factor_array = E2O_conversion_factor_array; set = true;}
    std::vector<float> E2O_conversion_factor_array() {return d_E2O_conversion_factor_array;}
      
    void set_O2E_conversion_factor_array(std::vector<float> O2E_conversion_factor_array){d_O2E_conversion_factor_array = O2E_conversion_factor_array; set = true;}
    std::vector<float> O2E_conversion_factor_array() {return d_O2E_conversion_factor_array;}

    
    int work(int noutput_items,
             gr_vector_const_void_star& input_items,
             gr_vector_void_star& output_items);
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OWC_CHANNEL_RELATIVE_CPVOLK_IMPL_H */
