/* -*- c++ -*- */
/* gr-owc OOT module for optical wireless communications.
 * gr-owc is compatible with GNU Radio v3.10
 *
 * Copyright 2024 Kunal Sangurmath from Ubiquitous Communications and Networking (UCAN) Lab, University of Massachusetts, Boston.
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

#include "PAM_Demodulator_cplus_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace owc {

using input_type = float;
using output_type = float;
PAM_Demodulator_cplus::sptr PAM_Demodulator_cplus::make(int modulation_order, float max_magnitude, float min_magnitude, int samples_per_symbol) {
  return gnuradio::make_block_sptr<PAM_Demodulator_cplus_impl>(
      modulation_order, max_magnitude, min_magnitude, samples_per_symbol);
}

/*
 * The private constructor
 */
PAM_Demodulator_cplus_impl::PAM_Demodulator_cplus_impl(int modulation_order, float max_magnitude, float min_magnitude, int samples_per_symbol)
    : gr::sync_decimator(
          "PAM_Demodulator_cplus",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1, 1,sizeof(output_type)),samples_per_symbol) 
    {
      set_modulation_order(modulation_order); 
      set_max_magnitude(max_magnitude);
      set_min_magnitude(min_magnitude);
      set_samples_per_symbol(samples_per_symbol);
      set_symbol_array(modulation_order);
      set_level_array(modulation_order, max_magnitude, min_magnitude);
    }

/*
 * Our virtual destructor.
 */
PAM_Demodulator_cplus_impl::~PAM_Demodulator_cplus_impl() {}

int PAM_Demodulator_cplus_impl::work(int noutput_items,
                                     gr_vector_const_void_star &input_items,
                                     gr_vector_void_star &output_items) {
  const float *in = (const float *) input_items[0];
  float *out = (float *) output_items[0];
      
  int i = 0;
  int j = 0;
      
  std::vector<float> d_incoming_samples_array;
      
  int num_incoming_samples = samples_per_symbol();
      
  int symbol_level = 0;
      
  while(i < noutput_items) {
    for (int k = 0; k < num_incoming_samples; k++){
        d_incoming_samples_array.push_back(in[j+k]);
    }
            
    float average_value = samples_average_value(d_incoming_samples_array, num_incoming_samples);
    
    for (int x = 0; x < modulation_order(); x++){
      float difference = average_value - level_array()[x];
      if ( abs(difference) < 0.000001)
      {
        symbol_level = x;
        break;
      }
    }
    
    out[i++] = symbol_array()[symbol_level];
          
    j += num_incoming_samples;
    d_incoming_samples_array.clear();
  }

  // Tell runtime system how many output items we produced.
  return noutput_items;
}

} /* namespace owc */
} /* namespace gr */
