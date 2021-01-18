/* -*- c++ -*- */
/* gr-owc OOT module for optical wireless communications. 
 *
 * Copyright 2021 Arsalan Ahmed from The Ubiquitous Communications and Networking (UCAN) Lab, University of Massachusetts, Boston.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 *
 */

#ifndef INCLUDED_OWC_OWC_CHANNEL_RELATIVE_IMPL_H
#define INCLUDED_OWC_OWC_CHANNEL_RELATIVE_IMPL_H

#include <owc/OWC_Channel_relative.h>

namespace gr {
  namespace owc {

    class OWC_Channel_relative_impl : public OWC_Channel_relative
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
	std::vector<float> d_concentrator_FOV_array;
	std::vector<float> d_E2O_conversion_factor_array;
	std::vector<float> d_O2E_conversion_factor_array;

     public:
      OWC_Channel_relative_impl(int num_inputs, int num_outputs, const std::vector<float>& emission_angle_array, const std::vector<float>& acceptance_angle_array, const std::vector<float>& distance_array, const std::vector<float>& lambertian_order_array, const std::vector<float>& photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array);
      ~OWC_Channel_relative_impl();
      
      void set_num_inputs(int num_inputs){d_num_inputs = num_inputs;}
      int r_num_inputs() {return d_num_inputs;}
      
      void set_num_outputs(int num_outputs){d_num_outputs = num_outputs;}
      int r_num_outputs() {return d_num_outputs;}
      
      void set_emission_angle_array(std::vector<float> emission_angle_array){d_emission_angle_array = emission_angle_array;}
      std::vector<float> emission_angle_array() {return d_emission_angle_array;}
      
      void set_acceptance_angle_array(std::vector<float> acceptance_angle_array){d_acceptance_angle_array = acceptance_angle_array;}
      std::vector<float> acceptance_angle_array() {return d_acceptance_angle_array;}
      
      void set_distance_array(std::vector<float> distance_array){d_distance_array = distance_array;}
      std::vector<float> distance_array() {return d_distance_array;}
      
      void set_lambertian_order_array(std::vector<float> lambertian_order_array){d_lambertian_order_array = lambertian_order_array;}
      std::vector<float> lambertian_order_array() {return d_lambertian_order_array;}
      
      void set_photosensor_area_array(std::vector<float> photosensor_area_array){d_photosensor_area_array = photosensor_area_array;}
      std::vector<float> photosensor_area_array() {return d_photosensor_area_array;}
      
      void set_optical_filter_transmittance_array(std::vector<float> optical_filter_transmittance_array){d_optical_filter_transmittance_array = optical_filter_transmittance_array;}
      std::vector<float> optical_filter_transmittance_array() {return d_optical_filter_transmittance_array;}
      
      void set_refractive_index_array(std::vector<float> refractive_index_array){d_refractive_index_array = refractive_index_array;}
      std::vector<float> refractive_index_array() {return d_refractive_index_array;}
      
      void set_concentrator_FOV_array(std::vector<float> concentrator_FOV_array){d_concentrator_FOV_array = concentrator_FOV_array;}
      std::vector<float> concentrator_FOV_array() {return d_concentrator_FOV_array;}
      
      void set_E2O_conversion_factor_array(std::vector<float> E2O_conversion_factor_array){d_E2O_conversion_factor_array = E2O_conversion_factor_array;}
      std::vector<float> E2O_conversion_factor_array() {return d_E2O_conversion_factor_array;}
      
      void set_O2E_conversion_factor_array(std::vector<float> O2E_conversion_factor_array){d_O2E_conversion_factor_array = O2E_conversion_factor_array;}
      std::vector<float> O2E_conversion_factor_array() {return d_O2E_conversion_factor_array;}
      
      float channel_model(float emission_angle, float acceptance_angle, float distance, float lambertian_order, float ps_area, float optical_filter_transmittance, float refractive_index, float concentrator_FOV, float E2O_conversion_factor, float O2E_conversion_factor){
       	     	
       	float Gt = ((lambertian_order + 1)/(2*M_PI))*pow(cos(emission_angle*(M_PI/180)),lambertian_order);
       	
       	float Ts = optical_filter_transmittance;
       	
       	float refractive_index_squared = refractive_index*refractive_index; 
       	float sin_of_concentrator_FOV_squared = sin(concentrator_FOV*(M_PI/180))*sin(concentrator_FOV*(M_PI/180));
       	float g = refractive_index_squared/sin_of_concentrator_FOV_squared;
       	if ((acceptance_angle < 0) || (acceptance_angle > concentrator_FOV))
       	{g = 0;}
       	
       	float Gr = ps_area*Ts*g*cos(acceptance_angle*(M_PI/180)); 
       	float distance_squared = distance * distance;
       	
       	float Ct = E2O_conversion_factor;
       	float Cr = O2E_conversion_factor;
       	
       	float H = Ct*((Gt*Gr)/distance_squared)*Cr;
       	
       	return H;       	     }

      // Where all the action really happens
      int work(
              int noutput_items,
              gr_vector_const_void_star &input_items,
              gr_vector_void_star &output_items
      );
    };

  } // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OWC_CHANNEL_RELATIVE_IMPL_H */

