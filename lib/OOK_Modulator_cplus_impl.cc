/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "OOK_Modulator_cplus_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace owc {


using input_type = float;

using output_type = float;

OOK_Modulator_cplus::sptr 
OOK_Modulator_cplus::make(float max_mag, float min_mag, int samples_per_symbol) {
  return gnuradio::make_block_sptr<OOK_Modulator_cplus_impl>(
      max_mag, min_mag, samples_per_symbol);
}

/*
 * The private constructor
 */
OOK_Modulator_cplus_impl::OOK_Modulator_cplus_impl(float max_mag, float min_mag, int samples_per_symbol)
    : gr::sync_interpolator(
          "OOK_Modulator_cplus",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1 , 1 , sizeof(output_type)), samples_per_symbol /*<+interpolation+>*/) {
      set_max_magnitude(max_mag);
      set_min_magnitude(min_mag);
      set_samples_per_symbol(samples_per_symbol);
    }

/*
 * Our virtual destructor.
 */
OOK_Modulator_cplus_impl::~OOK_Modulator_cplus_impl() {}

int OOK_Modulator_cplus_impl::work(int noutput_items,
                                   gr_vector_const_void_star &input_items,
                                   gr_vector_void_star &output_items) {
  const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      int i = 0;
      int z = 0;
      
      while(i < noutput_items) {
          for (int j = 0; j < samples_per_symbol(); j++){
            if (in[z] == 0) {out[i++] = min_magnitude();}
            else {out[i++] = max_magnitude();}
            }
          z++;
        }

  return noutput_items;
}

} /* namespace owc */
} /* namespace gr */
