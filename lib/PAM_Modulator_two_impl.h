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

#ifndef INCLUDED_OWC_PAM_MODULATOR_TWO_IMPL_H
#define INCLUDED_OWC_PAM_MODULATOR_TWO_IMPL_H

#include <owc/PAM_Modulator_two.h>

namespace gr {
  namespace owc {

    class PAM_Modulator_two_impl : public PAM_Modulator_two
    {
     private:
     int d_modulation_order;
     float d_amplitude;
     float d_mean;
     int d_samples_per_symbol;
     
     std::vector<int> d_symbol_array;
     std::vector<float> d_level_array;

     public:
      PAM_Modulator_two_impl(int modulation_order, float amplitude, float mean, int samples_per_symbol);
      ~PAM_Modulator_two_impl();
      
      void set_modulation_order(int modulation_order) { d_modulation_order = modulation_order; }
      int modulation_order() { return d_modulation_order; }
      
      void set_amplitude(float amplitude) { d_amplitude = amplitude; }
      float amplitude() { return d_amplitude; }
      
      void set_mean(float mean) { d_mean = mean; }
      float mean() { return d_mean; }

      void set_samples_per_symbol(int samples_per_symbol) { d_samples_per_symbol = samples_per_symbol; }
      int samples_per_symbol() { return d_samples_per_symbol; }
      
      void set_symbol_array(int modulation_order)
      {
      	int num_bits = floor(log2(modulation_order));
      	int max_symbol = pow(2,num_bits);
      	
      	for (int i = 0; i < max_symbol; i++)
      	{
      		d_symbol_array.push_back(i);
      	}
      	
      }
      std::vector<int> symbol_array() {return d_symbol_array;}
      
      
      void set_level_array(int modulation_order, float amplitude, float mean)
      {
      	int num_bits = floor(log2(modulation_order));
      	int max_symbol = pow(2,num_bits);
      	
	float max_magnitude = mean + amplitude;
	float min_magnitude = mean - amplitude;
      	
      	float range = max_magnitude - min_magnitude;
      	float single_level_magnitude = range/(modulation_order-1);
      	
      	float levels = min_magnitude;
      	      	
      	for (int i = 0; i < max_symbol; i++)
      	{
      		d_level_array.push_back(levels);
      		levels += single_level_magnitude;
      	}
      	
      }
      std::vector<float> level_array() {return d_level_array;}

      // Where all the action really happens
      int work(
              int noutput_items,
              gr_vector_const_void_star &input_items,
              gr_vector_void_star &output_items
      );
    };

  } // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_PAM_MODULATOR_TWO_IMPL_H */

