/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "OOK_Demodulator_cplus_impl.h"
#include <gnuradio/io_signature.h>
#include <numeric>

namespace gr {
namespace owc {

using input_type = float;
using output_type = float;

OOK_Demodulator_cplus::sptr 
OOK_Demodulator_cplus::make(float threshold, int samples_per_symbol) {
  return gnuradio::make_block_sptr<OOK_Demodulator_cplus_impl>(threshold, samples_per_symbol);
}

/*
 * The private constructor
 */
OOK_Demodulator_cplus_impl::OOK_Demodulator_cplus_impl(float threshold,
                                                       int samples_per_symbol)
    : gr::sync_decimator(
          "OOK_Demodulator_cplus",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1, 1, sizeof(output_type)), samples_per_symbol) 
    {
      set_threshold(threshold);
      set_samples_per_symbol(samples_per_symbol);
    }

/*
 * Our virtual destructor.
 */
OOK_Demodulator_cplus_impl::~OOK_Demodulator_cplus_impl() {}

int OOK_Demodulator_cplus_impl::work(int noutput_items,
                                     gr_vector_const_void_star &input_items,
                                     gr_vector_void_star &output_items) {
  const float *in = (const float *) input_items[0];
  float *out = (float *) output_items[0];

  int i = 0;
  int j = 0;
      
  std::vector<float> d_samples_array;
      
  int d_samples_per_symbol = samples_per_symbol();
      
  while(i < noutput_items) {
    for (int k = 0; k < d_samples_per_symbol; k++)
      {
        d_samples_array.push_back(in[j+k]);
      }
            
    float average_value = std::reduce(d_samples_array.begin(), d_samples_array.end()) / d_samples_per_symbol;
    
    if (average_value > threshold()){
      out[i++] = 1.0;
    }
    
    else{
      out[i++] = 0.0;
    }
      
    j += d_samples_per_symbol;
    d_samples_array.clear();
  }

  return noutput_items;
}

} /* namespace owc */
} /* namespace gr */
