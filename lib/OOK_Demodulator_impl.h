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

#ifndef INCLUDED_OWC_OOK_DEMODULATOR_IMPL_H
#define INCLUDED_OWC_OOK_DEMODULATOR_IMPL_H

#include <owc/OOK_Demodulator.h>

namespace gr {
  namespace owc {

    class OOK_Demodulator_impl : public OOK_Demodulator
    {
     private:
     float d_threshold;
     int d_samples_per_symbol;

     public:
      OOK_Demodulator_impl(float threshold, int samples_per_symbol);
      ~OOK_Demodulator_impl();
      
      void set_threshold(float threshold) { d_threshold = threshold; }
      float threshold() { return d_threshold; }

      void set_samples_per_symbol(int samples_per_symbol) { d_samples_per_symbol = samples_per_symbol; }
      int samples_per_symbol() { return d_samples_per_symbol;}
      
      float samples_average_value(std::vector<float> samples_array, int num_incoming_samples)
      {
      	float sum = 0;
      	
      	for (int i = 0; i < num_incoming_samples; i++)
      	{
		sum += samples_array[i];
      	}
      	
      	return (sum/num_incoming_samples);
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

#endif /* INCLUDED_OWC_OOK_DEMODULATOR_IMPL_H */

