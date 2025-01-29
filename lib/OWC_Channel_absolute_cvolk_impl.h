/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OWC_OWC_CHANNEL_ABSOLUTE_CVOLK_IMPL_H
#define INCLUDED_OWC_OWC_CHANNEL_ABSOLUTE_CVOLK_IMPL_H

#include <gnuradio/owc/OWC_Channel_absolute_cvolk.h>

namespace gr {
namespace owc {

class OWC_Channel_absolute_cvolk_impl : public OWC_Channel_absolute_cvolk {
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
    std::vector<float> channel_model_values;
    bool set = true;

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
                
            float H = 1;

            if(distance_array()[index] != 0){
                if (emission_angle_array()[index] <= 90)
                {
                Gt = ((tx_lambertian_order_array()[j] + 1)/(2*M_PI))*pow(cos(emission_angle_array()[index]*(M_PI/180)),tx_lambertian_order_array()[j]);
                }
            
                if ((acceptance_angle_array()[index] >= 0) && (acceptance_angle_array()[index] <= concentrator_FOV_array()[x])){
                    float Ts = optical_filter_transmittance_array()[x];
                    float refractive_index_squared = refractive_index_array()[x]*refractive_index_array()[x]; 
                    float sin_of_concentrator_FOV_squared = sin(concentrator_FOV_array()[x]*(M_PI/180))*sin(concentrator_FOV_array()[x]*(M_PI/180));
                    g = refractive_index_squared/sin_of_concentrator_FOV_squared;
                    Gr = rx_photosensor_area_array()[x]*Ts*g*cos(acceptance_angle_array()[index]*(M_PI/180)); 
                }
            
                float distance_squared = distance_array()[index] * distance_array()[index];
        
                float Ct = E2O_conversion_factor_array()[j];
                float Cr = O2E_conversion_factor_array()[x];
        
                H = Ct*((Gt*Gr)/distance_squared)*Cr;
            }
            channel_model_values.push_back(H);
          }
     }
     set = false;
  }

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
            set = true;
        }

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
                
                    float ux = (x2-x1);  
                    float uy = (y2-y1); 
                    float uz = (z2-z1);
                    
                    float ux_squared = ux*ux;
                    float uy_squared = uy*uy;
                    float uz_squared = uz*uz;
                    
                    float u_mag = sqrt(ux_squared + uy_squared + uz_squared);
                    
                float vx = tx_orientation_array()[j];       
                float vy = tx_orientation_array()[j+1];
                float vz = tx_orientation_array()[j+2];
                
                float vx_squared = vx*vx;
                float vy_squared = vy*vy;
                float vz_squared = vz*vz;
                
                float v_mag = sqrt(vx_squared + vy_squared + vz_squared);
                
                float angle = 0;
                
                if(u_mag != 0){
                    float numerator= (ux*vx)+(uy*vy)+(uz*vz);
                    float denominator = u_mag*v_mag;
                
                    angle = acos((numerator/denominator))*(180/M_PI);
                }
                
                d_emission_angle_array.push_back(angle);
                }
            }
            set = true;   
        }

    void set_acceptance_angle_array()
        {
            d_acceptance_angle_array.clear();
            for (int i = 0; i < 3*r_num_outputs(); i+=3)
            {
                float x1 = rx_coordinates_array()[i];
                float y1 = rx_coordinates_array()[i+1];
                float z1 = rx_coordinates_array()[i+2];
                
            float vx = rx_orientation_array()[i];      
            float vy = rx_orientation_array()[i+1];
            float vz = rx_orientation_array()[i+2];
                
                for (int j = 0; j < 3*r_num_inputs(); j+=3)
                {
                    float x2 = tx_coordinates_array()[j];
                    float y2 = tx_coordinates_array()[j+1];
                    float z2 = tx_coordinates_array()[j+2];
                
                    float ux = (x2-x1);     //tx to rx vector 
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
                
                float angle = 0;
                
                if(u_mag != 0){
                    float numerator= (ux*vx)+(uy*vy)+(uz*vz);
                    float denominator = u_mag*v_mag;
                
                    angle = acos((numerator/denominator))*(180/M_PI);
                }
                
                d_acceptance_angle_array.push_back(angle);
                }
            }
            set = true;   
        }

public:
    OWC_Channel_absolute_cvolk_impl(int num_inputs, int num_outputs, const std::vector<float>& tx_coordinates_array, const std::vector<float>& tx_orientation_array, const std::vector<float>& rx_coordinates_array, const std::vector<float>& rx_orientation_array, const std::vector<float>& tx_lambertian_order_array, const std::vector<float>& rx_photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array);
    ~OWC_Channel_absolute_cvolk_impl();

    void set_num_inputs(int num_inputs){d_num_inputs = num_inputs; set = true;}
    int r_num_inputs() {return d_num_inputs;}
      
    void set_num_outputs(int num_outputs){d_num_outputs = num_outputs; set = true;}
    int r_num_outputs() {return d_num_outputs;}

    void set_tx_coordinates_array(std::vector<float> tx_coordinates_array){d_tx_coordinates_array = tx_coordinates_array; set = true;}
    std::vector<float> tx_coordinates_array() {return d_tx_coordinates_array;}     
      
    void set_tx_orientation_array(std::vector<float> tx_orientation_array){d_tx_orientation_array = tx_orientation_array; set = true;}
    std::vector<float> tx_orientation_array() {return d_tx_orientation_array;}

    void set_rx_coordinates_array(std::vector<float> rx_coordinates_array){d_rx_coordinates_array = rx_coordinates_array; set = true;}
    std::vector<float> rx_coordinates_array() {return d_rx_coordinates_array;}     
      
    void set_rx_orientation_array(std::vector<float> rx_orientation_array){d_rx_orientation_array = rx_orientation_array; set = true;}
    std::vector<float> rx_orientation_array() {return d_rx_orientation_array;}   

    void set_tx_lambertian_order_array(std::vector<float> tx_lambertian_order_array){d_tx_lambertian_order_array = tx_lambertian_order_array; set = true;}
    std::vector<float> tx_lambertian_order_array() {return d_tx_lambertian_order_array;}       
      
    void set_rx_photosensor_area_array(std::vector<float> rx_photosensor_area_array){d_rx_photosensor_area_array = rx_photosensor_area_array; set = true;}
    std::vector<float> rx_photosensor_area_array() {return d_rx_photosensor_area_array;}  

    void set_optical_filter_transmittance_array(std::vector<float> optical_filter_transmittance_array){d_optical_filter_transmittance_array = optical_filter_transmittance_array; set = true;}
    std::vector<float> optical_filter_transmittance_array() {return d_optical_filter_transmittance_array;}
      
    void set_refractive_index_array(std::vector<float> refractive_index_array){d_refractive_index_array = refractive_index_array; set = true;}
    std::vector<float> refractive_index_array() {return d_refractive_index_array;}
      
    void set_concentrator_FOV_array(std::vector<float> concentrator_FOV_array){d_concentrator_FOV_array = concentrator_FOV_array; set = true;}
    std::vector<float> concentrator_FOV_array() {return d_concentrator_FOV_array;}
      
    void set_E2O_conversion_factor_array(std::vector<float> E2O_conversion_factor_array){d_E2O_conversion_factor_array = E2O_conversion_factor_array; set = true;}
    std::vector<float> E2O_conversion_factor_array() {return d_E2O_conversion_factor_array;}
      
    void set_O2E_conversion_factor_array(std::vector<float> O2E_conversion_factor_array){d_O2E_conversion_factor_array = O2E_conversion_factor_array; set = true;}
    std::vector<float> O2E_conversion_factor_array() {return d_O2E_conversion_factor_array;} 

        
    std::vector<float> distance_array() {return d_distance_array;} 
        
    
    std::vector<float> emission_angle_array() {return d_emission_angle_array;} 
        
    
    std::vector<float> acceptance_angle_array() {return d_acceptance_angle_array;}

      // Where all the action really happens
    int work(int noutput_items, gr_vector_const_void_star &input_items,
               gr_vector_void_star &output_items);
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OWC_CHANNEL_ABSOLUTE_CVOLK_IMPL_H */
