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
#include "decimal_to_binary_mapper_impl.h"

namespace gr {
  namespace owc {

    decimal_to_binary_mapper::sptr
    decimal_to_binary_mapper::make(int modulation_order)
    {
      return gnuradio::get_initial_sptr
        (new decimal_to_binary_mapper_impl(modulation_order));
    }


    /*
     * The private constructor
     */
    decimal_to_binary_mapper_impl::decimal_to_binary_mapper_impl(int modulation_order)
      : gr::sync_interpolator("decimal_to_binary_mapper",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)), floor(log2(modulation_order)))
    {
    	set_modulation_order(modulation_order);
    }

    /*
     * Our virtual destructor.
     */
    decimal_to_binary_mapper_impl::~decimal_to_binary_mapper_impl()
    {
    }

    int
    decimal_to_binary_mapper_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];
      
      int num_output_bits = floor(log2(modulation_order()));

      int i = 0;
      int z = 0;
      
      
      while(i < noutput_items) {
      		int decimal_value = in[z];
      		std::vector<int> binary = decimal_to_binary(decimal_value, num_output_bits);
      		for (int j = 0; j < num_output_bits; j++){
      			out[i++] = binary[j];	
      		}
      	z++;}

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace owc */
} /* namespace gr */

