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
#include "PAM_Modulator_two_impl.h"

namespace gr {
  namespace owc {

    PAM_Modulator_two::sptr
    PAM_Modulator_two::make(int modulation_order, float amplitude, float mean, int samples_per_symbol)
    {
      return gnuradio::get_initial_sptr
        (new PAM_Modulator_two_impl(modulation_order, amplitude, mean, samples_per_symbol));
    }


    /*
     * The private constructor
     */
    PAM_Modulator_two_impl::PAM_Modulator_two_impl(int modulation_order, float amplitude, float mean, int samples_per_symbol)
      : gr::sync_interpolator("PAM_Modulator_two",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)), samples_per_symbol)
    {
	set_modulation_order(modulation_order); 
	set_amplitude(amplitude);
    	set_mean(mean);
    	set_samples_per_symbol(samples_per_symbol);
    	set_symbol_array(modulation_order);
    	set_level_array(modulation_order, amplitude, mean);
    }

    /*
     * Our virtual destructor.
     */
    PAM_Modulator_two_impl::~PAM_Modulator_two_impl()
    {
    }

    int
    PAM_Modulator_two_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];
      
      int log_2_M = floor(log2(modulation_order()));
      int max_symbol = pow(2,log_2_M);
      int symbol_index = 0;
      
      int i = 0;
      int z = 0;
      
      while(i < noutput_items) {
      		int decimal = 	in[z];	
      		for (int j = 0; j < samples_per_symbol(); j++){
      			for (int m = 0; m < max_symbol; m++)
			{
				if (decimal == symbol_array()[m])
				{symbol_index = m;
				 break;}
			}
						
			out[i++] = level_array()[symbol_index];
      			
      		}
      		z++;
      		symbol_index = 0;}


      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace owc */
} /* namespace gr */

