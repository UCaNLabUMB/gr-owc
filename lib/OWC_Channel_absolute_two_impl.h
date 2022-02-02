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

#ifndef INCLUDED_OWC_OWC_CHANNEL_ABSOLUTE_TWO_IMPL_H
#define INCLUDED_OWC_OWC_CHANNEL_ABSOLUTE_TWO_IMPL_H

#include <owc/OWC_Channel_absolute_two.h>
#include <gnuradio/random.h>

namespace gr {
  namespace owc {

    class OWC_Channel_absolute_two_impl : public OWC_Channel_absolute_two
    {
     private:
      	int d_num_inputs = 1;
      	int d_num_outputs = 1;
      	
	std::vector<float> d_tx_lambertian_order_array;
	std::vector<float> d_rx_photosensor_area_array;
	
	std::vector<float> d_distance_array;
	
	std::vector<float> d_emission_angle_array;
	std::vector<float> d_acceptance_angle_array;
	
	std::vector<float> d_optical_filter_transmittance_array;
	std::vector<float> d_refractive_index_array;
	std::vector<float> d_concentrator_FOV_array;
	std::vector<float> d_E2O_conversion_factor_array;
	std::vector<float> d_O2E_conversion_factor_array;
	
	std::vector<float> d_tx_coordinates_array;
	std::vector<float> d_tx_orientation_array;
	std::vector<float> d_rx_coordinates_array;
	std::vector<float> d_rx_orientation_array;
	
	int d_sample_rate;
	
	std::vector<int> d_num_delay_samples_array;
	std::vector<int> d_blockage_array;
	
	std::vector<float> d_remaining_input_samples;
	
	std::vector<float> d_noise_power_array;
	
	gr::random d_rng;
	
	int d_noutput_items_previous = 10000;//Using 10000 (a very large number just to be safe) zeros initially to add at the very start

     public:
      OWC_Channel_absolute_two_impl(int num_inputs, int num_outputs, const std::vector<float>& tx_coordinates_array, const std::vector<float>& tx_orientation_array, const std::vector<float>& rx_coordinates_array, const std::vector<float>& rx_orientation_array, const std::vector<float>& tx_lambertian_order_array, const std::vector<float>& rx_photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array, int sample_rate, const std::vector<int>& blockage_array, const std::vector<float>& noise_power_array);
      ~OWC_Channel_absolute_two_impl();
      
      void set_num_inputs(int num_inputs){d_num_inputs = num_inputs;}
      int r_num_inputs() {return d_num_inputs;}
      
      void set_num_outputs(int num_outputs){d_num_outputs = num_outputs;}
      int r_num_outputs() {return d_num_outputs;}
      
      void set_tx_coordinates_array(std::vector<float> tx_coordinates_array){d_tx_coordinates_array = tx_coordinates_array;}
      std::vector<float> tx_coordinates_array() {return d_tx_coordinates_array;}     
      
      void set_tx_orientation_array(std::vector<float> tx_orientation_array){d_tx_orientation_array = tx_orientation_array;}
      std::vector<float> tx_orientation_array() {return d_tx_orientation_array;}  
      
      void set_rx_coordinates_array(std::vector<float> rx_coordinates_array){d_rx_coordinates_array = rx_coordinates_array;}
      std::vector<float> rx_coordinates_array() {return d_rx_coordinates_array;}     
      
      void set_rx_orientation_array(std::vector<float> rx_orientation_array){d_rx_orientation_array = rx_orientation_array;}
      std::vector<float> rx_orientation_array() {return d_rx_orientation_array;}  
      
      void set_tx_lambertian_order_array(std::vector<float> tx_lambertian_order_array){d_tx_lambertian_order_array = tx_lambertian_order_array;}
      std::vector<float> tx_lambertian_order_array() {return d_tx_lambertian_order_array;}       
      
      void set_rx_photosensor_area_array(std::vector<float> rx_photosensor_area_array){d_rx_photosensor_area_array = rx_photosensor_area_array;}
      std::vector<float> rx_photosensor_area_array() {return d_rx_photosensor_area_array;}   
      
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
      
      float channel_model(float emission_angle, float acceptance_angle, float distance, float lambertian_order, float ps_area, float optical_filter_transmittance, float refractive_index, float concentrator_FOV, float E2O_conversion_factor, float O2E_conversion_factor, int blockage){
       	float Gt = 0;
       	     	
       	if (emission_angle <= 90)
       	{
       		Gt = ((lambertian_order + 1)/(2*M_PI))*pow(cos(emission_angle*(M_PI/180)),lambertian_order);
       	}
       	else
       	{
       		Gt = 0;
       	}
       	
       	float Ts = optical_filter_transmittance;
       	
       	float refractive_index_squared = refractive_index*refractive_index; 
       	float sin_of_concentrator_FOV_squared = sin(concentrator_FOV*(M_PI/180))*sin(concentrator_FOV*(M_PI/180));
       	float g = refractive_index_squared/sin_of_concentrator_FOV_squared;
       	if ((acceptance_angle < 0) || (acceptance_angle > concentrator_FOV))
       	{g = 0.0;}
       	
       	float Gr = ps_area*Ts*g*cos(acceptance_angle*(M_PI/180)); 
       	float distance_squared = distance * distance;
       	
       	float Ct = E2O_conversion_factor;
       	float Cr = O2E_conversion_factor;
       	
       	float H = Ct*((Gt*Gr)/distance_squared)*Cr;
       	
       	H = H * blockage;
       	
       	return H;       	     }
       	      
 
     	void set_distance_array()
     	{     		
     		d_distance_array.clear();
     		for (int i = 0; i < 3*r_num_outputs(); i+=3)
     		{
     			float x2 = rx_coordinates_array()[i];
     			float y2 = rx_coordinates_array()[i+1];
     			float z2 = rx_coordinates_array()[i+2];
     			
     			for (int j = 0; j < 3*r_num_inputs(); j+=3)
     			{
	     			float x1 = tx_coordinates_array()[j];
	     			float y1 = tx_coordinates_array()[j+1];
	     			float z1 = tx_coordinates_array()[j+2];
     			
     				float xSquared = (x2-x1)*(x2-x1); 
     				float ySquared = (y2-y1)*(y2-y1); 
     				float zSquared = (z2-z1)*(z2-z1);
     				
     				float distance = sqrt(xSquared+ySquared+zSquared);
     				
     				d_distance_array.push_back(distance); 
     			}
     		}
     	}
     	
     	std::vector<float> distance_array() {return d_distance_array;} 
     	
	void set_emission_angle_array()
     	{     
     		d_emission_angle_array.clear();		
     		for (int i = 0; i < 3*r_num_outputs(); i+=3)
     		{
     			float x2 = rx_coordinates_array()[i];
     			float y2 = rx_coordinates_array()[i+1];
     			float z2 = rx_coordinates_array()[i+2];
     			
     			for (int j = 0; j < 3*r_num_inputs(); j+=3)
     			{
	     			float x1 = tx_coordinates_array()[j];
	     			float y1 = tx_coordinates_array()[j+1];
	     			float z1 = tx_coordinates_array()[j+2];
     			
     				float ux = (x2-x1);		//tx to rx vector 
     				float uy = (y2-y1); 
     				float uz = (z2-z1);
     				
     				float ux_squared = ux*ux;
     				float uy_squared = uy*uy;
     				float uz_squared = uz*uz;
     				
     				float u_mag = sqrt(ux_squared + uy_squared + uz_squared);
     				
				float vx = tx_orientation_array()[j];		//tx orientation vector
				float vy = tx_orientation_array()[j+1];
				float vz = tx_orientation_array()[j+2];
				
				float vx_squared = vx*vx;
				float vy_squared = vy*vy;
				float vz_squared = vz*vz;
				
				float v_mag = sqrt(vx_squared + vy_squared + vz_squared);
				
				float numerator= (ux*vx)+(uy*vy)+(uz*vz);
				float denominator =u_mag*v_mag;
				
				float angle = acos((numerator/denominator))*(180/M_PI);
				
				d_emission_angle_array.push_back(angle);
     			}
     		}	
     	}
     	std::vector<float> emission_angle_array() {return d_emission_angle_array;} 
     	
	void set_acceptance_angle_array()
     	{
     		d_acceptance_angle_array.clear();
     		for (int i = 0; i < 3*r_num_outputs(); i+=3)
     		{
     			float x1 = rx_coordinates_array()[i];
     			float y1 = rx_coordinates_array()[i+1];
     			float z1 = rx_coordinates_array()[i+2];
     			
			float vx = rx_orientation_array()[i];		//tx orientation vector
			float vy = rx_orientation_array()[i+1];
			float vz = rx_orientation_array()[i+2];
     			
     			for (int j = 0; j < 3*r_num_inputs(); j+=3)
     			{
	     			float x2 = tx_coordinates_array()[j];
	     			float y2 = tx_coordinates_array()[j+1];
	     			float z2 = tx_coordinates_array()[j+2];
     			
     				float ux = (x2-x1);		//tx to rx vector 
     				float uy = (y2-y1); 
     				float uz = (z2-z1);
     				
     				float ux_squared = ux*ux;
     				float uy_squared = uy*uy;
     				float uz_squared = uz*uz;
     				
     				float u_mag = sqrt(ux_squared + uy_squared + uz_squared);
				
				float vx_squared = vx*vx;
				float vy_squared = vy*vy;
				float vz_squared = vz*vz;
				
				float v_mag = sqrt(vx_squared + vy_squared + vz_squared);
				
				float numerator= (ux*vx)+(uy*vy)+(uz*vz);
				float denominator =u_mag*v_mag;
				
				float angle = acos(numerator/denominator)*(180/M_PI); 
				
				d_acceptance_angle_array.push_back(angle);
     			}
     		}	
     	}
     	std::vector<float> acceptance_angle_array() {return d_acceptance_angle_array;}
     	
      void set_sample_rate(int sample_rate){d_sample_rate = sample_rate;}
      int sample_rate() {return d_sample_rate;}
      
      void set_num_delay_samples_array()
      {      	
      	d_num_delay_samples_array.clear();
      	float speed_of_light = 299792458;
      	
      	float propagation_time = 0;
      	float num_delay_samples = 0;
      	 
      	int array_length = r_num_inputs()*r_num_outputs();
      	
      	for (int x = 0; x < array_length; x++)
      	{
      		propagation_time = distance_array()[x] / speed_of_light;
      		num_delay_samples = round(propagation_time * sample_rate());  
      		
      		d_num_delay_samples_array.push_back(num_delay_samples); 
      	}
      }      
      std::vector<int> num_delay_samples_array() {return d_num_delay_samples_array;}
           
      void set_blockage_array(std::vector<int> blockage_array){d_blockage_array = blockage_array;}
      std::vector<int> blockage_array() {return d_blockage_array;}
      
      void set_remaining_samples_array()
      {
      		for (int x = 0; x < r_num_inputs()*d_noutput_items_previous; x++)
      		{
      			d_remaining_input_samples.push_back(0);
      		}
      }
      std::vector<float> remaining_samples_array() {return d_remaining_input_samples;}
      
      void set_noise_power_array(std::vector<float> noise_power_array){d_noise_power_array = noise_power_array;}
      std::vector<float> noise_power_array() {return d_noise_power_array;}

      // Where all the action really happens
      int work(
              int noutput_items,
              gr_vector_const_void_star &input_items,
              gr_vector_void_star &output_items
      );
    };

  } // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OWC_CHANNEL_ABSOLUTE_TWO_IMPL_H */

