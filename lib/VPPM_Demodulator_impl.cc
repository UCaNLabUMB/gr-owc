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
#include "VPPM_Demodulator_impl.h"

namespace gr {
  namespace owc {

    VPPM_Demodulator::sptr
    VPPM_Demodulator::make(int samples_per_symbol, int samples_per_pulse, float gain)
    {
      return gnuradio::get_initial_sptr
        (new VPPM_Demodulator_impl(samples_per_symbol, samples_per_pulse, gain));
    }


    /*
     * The private constructor
     */
    VPPM_Demodulator_impl::VPPM_Demodulator_impl(int samples_per_symbol, int samples_per_pulse, float gain)
      : gr::sync_decimator("VPPM_Demodulator",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)), samples_per_symbol)
    {
    	set_samples_per_symbol(samples_per_symbol);
    	set_samples_per_pulse(samples_per_pulse);
    	set_gain(gain);
    }

    /*
     * Our virtual destructor.
     */
    VPPM_Demodulator_impl::~VPPM_Demodulator_impl()
    {
    }

    int
    VPPM_Demodulator_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];
      
      int i = 0;
      int j = 0;
      
      std::vector<float> d_incoming_samples_array;
      
      int symbol_level = 0;
      
      while(i < noutput_items) {
      		for (int k = 0; k < samples_per_symbol(); k++)
      			{
      				d_incoming_samples_array.push_back(in[j+k]);
      			}
      			
		float matched_filter_output = matched_filter(d_incoming_samples_array, samples_per_symbol(), samples_per_pulse(), gain());
		
		if (matched_filter_output > 0)
		{
			out[i++] = 0;
		}
		else
		{
			out[i++] = 1.0;
		}
      		
	j += samples_per_symbol();
	d_incoming_samples_array.clear();
	}

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace owc */
} /* namespace gr */

