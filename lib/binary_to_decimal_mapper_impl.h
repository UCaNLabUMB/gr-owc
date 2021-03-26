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

#ifndef INCLUDED_OWC_BINARY_TO_DECIMAL_MAPPER_IMPL_H
#define INCLUDED_OWC_BINARY_TO_DECIMAL_MAPPER_IMPL_H

#include <owc/binary_to_decimal_mapper.h>

namespace gr {
  namespace owc {

    class binary_to_decimal_mapper_impl : public binary_to_decimal_mapper
    {
     private:
     int d_modulation_order;

     public:
      binary_to_decimal_mapper_impl(int modulation_order);
      ~binary_to_decimal_mapper_impl();

      void set_modulation_order(int modulation_order) { d_modulation_order = modulation_order; }
      int modulation_order() { return d_modulation_order; }
      
      int bits_to_decimal(std::vector<float> bits_array, float num_bits)
      {
      	int decimal_value = 0;
      	
      	reverse(bits_array.begin(),bits_array.end());
      	
      	for (int i = 0; i < num_bits; i++)
      	{
      		if (bits_array[i] == 1) 
      		{decimal_value += pow(2,i);}
      	}
      	return decimal_value;
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

#endif /* INCLUDED_OWC_BINARY_TO_DECIMAL_MAPPER_IMPL_H */

