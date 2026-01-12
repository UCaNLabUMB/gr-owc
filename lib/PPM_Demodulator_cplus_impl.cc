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

#include "PPM_Demodulator_cplus_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace owc {

using input_type = float;
using output_type = float;
PPM_Demodulator_cplus::sptr PPM_Demodulator_cplus::make(int samples_per_symbol, int samples_per_pulse, int modulation_order) {
  return gnuradio::make_block_sptr<PPM_Demodulator_cplus_impl>(
      samples_per_symbol, samples_per_pulse, modulation_order);
}

/*
 * The private constructor
 */
PPM_Demodulator_cplus_impl::PPM_Demodulator_cplus_impl(int samples_per_symbol, int samples_per_pulse, int modulation_order)
    : gr::sync_decimator(
          "PPM_Demodulator_cplus",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1 , 1 ,sizeof(output_type)), samples_per_symbol) 
    {
      set_samples_per_symbol(samples_per_symbol);
      set_samples_per_pulse(samples_per_pulse);
      set_modulation_order(modulation_order);
      initialize_vector_PPM();
    }

/*
 * Our virtual destructor.
 */
PPM_Demodulator_cplus_impl::~PPM_Demodulator_cplus_impl() {}

int PPM_Demodulator_cplus_impl::work(int noutput_items,
                                     gr_vector_const_void_star &input_items,
                                     gr_vector_void_star &output_items) {
  const float *in = (const float *) input_items[0];
  float *out = (float *) output_items[0];

  int i = 0;
  int j = 0;

  std::vector<float> d_incoming_samples_array;

  while (i < noutput_items) {

    for (int k = 0; k < samples_per_symbol(); k++) {
      d_incoming_samples_array.push_back(in[j + k]);
    }

    out[i++] = matched_filter_ppm(d_incoming_samples_array);

    j += samples_per_symbol();
    d_incoming_samples_array.clear();
  }


  // Tell runtime system how many output items we produced.
  return noutput_items;
}

} /* namespace owc */
} /* namespace gr */
