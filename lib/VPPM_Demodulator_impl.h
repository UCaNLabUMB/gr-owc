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

#ifndef INCLUDED_OWC_VPPM_DEMODULATOR_IMPL_H
#define INCLUDED_OWC_VPPM_DEMODULATOR_IMPL_H

#include <owc/VPPM_Demodulator.h>

namespace gr {
  namespace owc {

    class VPPM_Demodulator_impl : public VPPM_Demodulator
    {
     private:
     int d_samples_per_symbol;
     int d_samples_per_pulse;
     float d_gain;

     public:
      VPPM_Demodulator_impl(int samples_per_symbol, int samples_per_pulse, float gain);
      ~VPPM_Demodulator_impl();
      
      void set_samples_per_symbol(int samples_per_symbol) { d_samples_per_symbol = samples_per_symbol; }
      int samples_per_symbol() { return d_samples_per_symbol; }
      
      void set_samples_per_pulse(int samples_per_pulse) { d_samples_per_pulse = samples_per_pulse; }
      int samples_per_pulse() { return d_samples_per_pulse; }
      
      void set_gain(float gain) { d_gain = gain; }
      float gain() { return d_gain; }
      
      float matched_filter(std::vector<float> samples_array, int num_incoming_samples, int samples_per_pulse, float gain)
      {
        std::vector<float> matching_signal_for_low;
        std::vector<float> matching_signal_for_high;
        
        for (int i = 0; i < num_incoming_samples; i++)
        {
		if (i < samples_per_pulse)
		{
			matching_signal_for_low.push_back(gain);
		}
		else
		{
			matching_signal_for_low.push_back(0);
		}
        }
        
        for (int j = 0; j < num_incoming_samples; j++)
        {
		if (j >= (num_incoming_samples - samples_per_pulse))
		{
			matching_signal_for_high.push_back((-1) * gain);
		}
		else
		{
			matching_signal_for_high.push_back(0);
		}
        }
        
        float positive_sum = 0;
        float negative_sum = 0;
        
        for (int x = 0; x < num_incoming_samples; x++)
        {
        	positive_sum += samples_array[x] * matching_signal_for_low[x];
        	negative_sum += samples_array[x] * matching_signal_for_high[x];
        }
            	
      	return positive_sum + negative_sum;
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

#endif /* INCLUDED_OWC_VPPM_DEMODULATOR_IMPL_H */

