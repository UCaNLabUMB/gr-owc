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
#include "binary_to_decimal_mapper_impl.h"

namespace gr {
  namespace owc {

    binary_to_decimal_mapper::sptr
    binary_to_decimal_mapper::make(int modulation_order)
    {
      return gnuradio::get_initial_sptr
        (new binary_to_decimal_mapper_impl(modulation_order));
    }


    /*
     * The private constructor
     */
    binary_to_decimal_mapper_impl::binary_to_decimal_mapper_impl(int modulation_order)
      : gr::sync_decimator("binary_to_decimal_mapper",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)), floor(log2(modulation_order)))
    {
    	set_modulation_order(modulation_order);
    }

    /*
     * Our virtual destructor.
     */
    binary_to_decimal_mapper_impl::~binary_to_decimal_mapper_impl()
    {
    }

    int
    binary_to_decimal_mapper_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      int i = 0;
      int j = 0;
      
      std::vector<float> d_bits_array;
      
      int num_input_bits = floor(log2(modulation_order()));
      
      
      while(i < noutput_items) {
      		for (int k = 0; k < num_input_bits; k++)
      			{
      				d_bits_array.push_back(in[j+k]);
      			}
      			
		int decimal = bits_to_decimal(d_bits_array, num_input_bits);
      
      
		out[i++] = decimal;
		j += num_input_bits;
		d_bits_array.clear();
      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace owc */
} /* namespace gr */

