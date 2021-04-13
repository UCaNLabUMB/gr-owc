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
#include "OOK_Demodulator_impl.h"

namespace gr {
  namespace owc {

    OOK_Demodulator::sptr
    OOK_Demodulator::make(float threshold, int samples_per_symbol)
    {
      return gnuradio::get_initial_sptr
        (new OOK_Demodulator_impl(threshold, samples_per_symbol));
    }


    /*
     * The private constructor
     */
    OOK_Demodulator_impl::OOK_Demodulator_impl(float threshold, int samples_per_symbol)
      : gr::sync_decimator("OOK_Demodulator",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)), samples_per_symbol)
    {
	set_threshold(threshold);
    	set_samples_per_symbol(samples_per_symbol);
    }

    /*
     * Our virtual destructor.
     */
    OOK_Demodulator_impl::~OOK_Demodulator_impl()
    {
    }

    int
    OOK_Demodulator_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      int i = 0;
      int j = 0;
      
      std::vector<float> d_samples_array;
      
      int num_incoming_samples = samples_per_symbol();
      
      while(i < noutput_items) {
      		for (int k = 0; k < num_incoming_samples; k++)
      			{
      				d_samples_array.push_back(in[j+k]);
      			}
      			
		float average_value = samples_average_value(d_samples_array, num_incoming_samples);
		
		if (average_value > threshold())
		{out[i++] = 1.0;}
		
		else
		{out[i++] = 0.0;}
      
	j += num_incoming_samples;
	d_samples_array.clear();
      }
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace owc */
} /* namespace gr */

