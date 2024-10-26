/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "OOK_Demodulator_cpvolk_impl.h"
#include <gnuradio/io_signature.h>
#include <volk/volk.h>

namespace gr {
namespace owc {


using input_type = float;
using output_type = float;

OOK_Demodulator_cpvolk::sptr 
OOK_Demodulator_cpvolk::make(float threshold, int samples_per_symbol) {
  return gnuradio::make_block_sptr<OOK_Demodulator_cpvolk_impl>(threshold, samples_per_symbol);
}

/*
 * The private constructor
 */
OOK_Demodulator_cpvolk_impl::OOK_Demodulator_cpvolk_impl(float threshold, int samples_per_symbol)
    : gr::sync_decimator(
          "OOK_Demodulator_cpvolk",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1, 1, sizeof(output_type)), samples_per_symbol) 
          {
            set_threshold(threshold);
            set_samples_per_symbol(samples_per_symbol);
    }

/*
 * Our virtual destructor.
 */
OOK_Demodulator_cpvolk_impl::~OOK_Demodulator_cpvolk_impl() {}

int OOK_Demodulator_cpvolk_impl::work(int noutput_items,
                                      gr_vector_const_void_star &input_items,
                                      gr_vector_void_star &output_items) {
  const float *in = (const float *) input_items[0];
  float *out = (float *) output_items[0];

  unsigned int alignment = volk_get_alignment();
  
  int d_samples_per_symbol = samples_per_symbol();

  float* temp_sum = (float*) volk_malloc(sizeof(float), alignment);

  int i = 0;
  int j = 0;
            
  while(i < noutput_items) {
     
    volk_32f_accumulator_s32f(temp_sum, in + j, d_samples_per_symbol);
    float average_value = *temp_sum  / d_samples_per_symbol;
    
    if (average_value > threshold()){
      out[i++] = 1.0;
    }
    
    else{
      out[i++] = 0.0;
    }
      
    j += d_samples_per_symbol;
    
  }

  volk_free(temp_sum);

  return noutput_items;
}

} /* namespace owc */
} /* namespace gr */