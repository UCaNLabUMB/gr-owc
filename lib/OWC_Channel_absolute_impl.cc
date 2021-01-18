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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "OWC_Channel_absolute_impl.h"

namespace gr {
  namespace owc {

    OWC_Channel_absolute::sptr
    OWC_Channel_absolute::make(int num_inputs, int num_outputs, const std::vector<float>& tx_coordinates_array, const std::vector<float>& tx_orientation_array, const std::vector<float>& rx_coordinates_array, const std::vector<float>& rx_orientation_array, const std::vector<float>& tx_lambertian_order_array, const std::vector<float>& rx_photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array)
    {
      return gnuradio::get_initial_sptr
        (new OWC_Channel_absolute_impl(num_inputs, num_outputs, tx_coordinates_array, tx_orientation_array, rx_coordinates_array, rx_orientation_array, tx_lambertian_order_array, rx_photosensor_area_array, optical_filter_transmittance_array, refractive_index_array, concentrator_FOV_array, E2O_conversion_factor_array, O2E_conversion_factor_array));
    }


    /*
     * The private constructor
     */
    OWC_Channel_absolute_impl::OWC_Channel_absolute_impl(int num_inputs, int num_outputs, const std::vector<float>& tx_coordinates_array, const std::vector<float>& tx_orientation_array, const std::vector<float>& rx_coordinates_array, const std::vector<float>& rx_orientation_array, const std::vector<float>& tx_lambertian_order_array, const std::vector<float>& rx_photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array)
      : gr::sync_block("OWC_Channel_absolute",
              gr::io_signature::make(1, -1, sizeof(float)),
              gr::io_signature::make(1, -1, sizeof(float)))
    {
	    set_num_inputs(num_inputs);
	    set_num_outputs(num_outputs);
	    
	    set_tx_lambertian_order_array(tx_lambertian_order_array);
	    set_rx_photosensor_area_array(rx_photosensor_area_array);
	    
	    set_distance_array(r_num_inputs(),r_num_outputs(),tx_coordinates_array,rx_coordinates_array);
	    
	    set_emission_angle_array(r_num_inputs(),r_num_outputs(),tx_coordinates_array,tx_orientation_array,rx_coordinates_array);
	    
	    set_acceptance_angle_array(r_num_inputs(),r_num_outputs(),tx_coordinates_array,rx_coordinates_array,rx_orientation_array);
	    
	    set_optical_filter_transmittance_array(optical_filter_transmittance_array);
	    set_refractive_index_array(refractive_index_array);
	    set_concentrator_FOV_array(concentrator_FOV_array);
	    set_E2O_conversion_factor_array(E2O_conversion_factor_array);
	    set_O2E_conversion_factor_array(O2E_conversion_factor_array);
    }

    /*
     * Our virtual destructor.
     */
    OWC_Channel_absolute_impl::~OWC_Channel_absolute_impl()
    {
    }

    int
    OWC_Channel_absolute_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      int ninputs = input_items.size();
      
      int noutputs = output_items.size();
      
      for (int i = 0; i < noutput_items; i++) {
      
		for (int x = 0; x < noutputs; x++)
		{      
			 int current = ninputs*x;
			 
			 float received_power = (((const float*)input_items[0])[i]) * channel_model(emission_angle_array()[current], acceptance_angle_array()[current], distance_array()[current], tx_lambertian_order_array()[0], rx_photosensor_area_array()[x],  optical_filter_transmittance_array()[x], refractive_index_array()[x], concentrator_FOV_array()[x], E2O_conversion_factor_array()[0], O2E_conversion_factor_array()[x]);
			 
			 for (int j = 1; j < ninputs; j++)
			 {
				received_power += (((const float*)input_items[j])[i]) * channel_model(emission_angle_array()[current+j], acceptance_angle_array()[current+j], distance_array()[current+j], tx_lambertian_order_array()[j], rx_photosensor_area_array()[x], optical_filter_transmittance_array()[x], refractive_index_array()[x], concentrator_FOV_array()[x], E2O_conversion_factor_array()[j], O2E_conversion_factor_array()[x]);
			 }

			((float*)output_items[x])[i] = (float)received_power;
		}
	}
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace owc */
} /* namespace gr */

