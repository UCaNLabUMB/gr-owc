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

#ifndef INCLUDED_OWC_DECIMAL_TO_BINARY_MAPPER_IMPL_H
#define INCLUDED_OWC_DECIMAL_TO_BINARY_MAPPER_IMPL_H

#include <owc/decimal_to_binary_mapper.h>

namespace gr {
  namespace owc {

    class decimal_to_binary_mapper_impl : public decimal_to_binary_mapper
    {
     private:
     int d_modulation_order;

     public:
      decimal_to_binary_mapper_impl(int modulation_order);
      ~decimal_to_binary_mapper_impl();
      
      void set_modulation_order(int modulation_order) { d_modulation_order = modulation_order; }
      int modulation_order() { return d_modulation_order; }
      
      std::vector<int> decimal_to_binary(int decimal_value, int num_output_bits)
      {
      		std::vector<int> binary_array;
      		int decimal_divide = decimal_value;
      		int rem = 0;      
      		
      		for (int x = 0; x < num_output_bits; x++)
      		{
			rem = decimal_divide % 2;
			binary_array.push_back(rem);
			decimal_divide = decimal_divide/2; 
      		}
      		
		reverse(binary_array.begin(),binary_array.end());
		return binary_array;
      } 

      // Where all the action really happens
      int work(
              int noutput_items,
              gr_vector_const_void_star &input_items,
              gr_vector_void_star &output_items
      );
    };

  } // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_DECIMAL_TO_BINARY_MAPPER_IMPL_H */

