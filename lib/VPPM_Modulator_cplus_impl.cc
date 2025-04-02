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

#include "VPPM_Modulator_cplus_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace owc {

using input_type = float;
using output_type = float;
VPPM_Modulator_cplus::sptr VPPM_Modulator_cplus::make(float max_mag, float min_mag,
                                                      int samples_per_symbol,
                                                      int samples_per_pulse) {
  return gnuradio::make_block_sptr<VPPM_Modulator_cplus_impl>(
      max_mag, min_mag, samples_per_symbol, samples_per_pulse);
}

/*
 * The private constructor
 */
VPPM_Modulator_cplus_impl::VPPM_Modulator_cplus_impl(float max_mag, float min_mag,
                                                     int samples_per_symbol,
                                                     int samples_per_pulse)
    : gr::sync_interpolator(
          "VPPM_Modulator_cplus",
          gr::io_signature::make(1, 1,
                                 sizeof(input_type)),
          gr::io_signature::make(1, 1,
                                 sizeof(output_type)),
          samples_per_symbol) 
    {
      set_max_magnitude(max_mag);
      set_min_magnitude(min_mag);
      set_samples_per_symbol(samples_per_symbol);
      set_samples_per_pulse(samples_per_pulse);
    }

/*
 * Our virtual destructor.
 */
VPPM_Modulator_cplus_impl::~VPPM_Modulator_cplus_impl() {}

int VPPM_Modulator_cplus_impl::work(int noutput_items,
                                    gr_vector_const_void_star &input_items,
                                    gr_vector_void_star &output_items) {
  
  const float *in = (const float *) input_items[0];
  float *out = (float *) output_items[0];

  int symbol_len = samples_per_symbol();
  int pulse_len = samples_per_pulse();
  int rest_len = symbol_len - pulse_len;

  std::vector<float> case1(symbol_len);
  std::vector<float> case2(symbol_len);

  for (int j = 0; j < symbol_len; j++) {
    if (j < pulse_len)
      case1[j] = max_magnitude();
    else
      case1[j] = min_magnitude();

    if (j < rest_len)
      case2[j] = min_magnitude();
    else
      case2[j] = max_magnitude();
  }

  int i = 0;
  int z = 0;

  while (i < noutput_items) {
    const float *symbol_ptr = (in[z] == 0) ? case1.data() : case2.data();
    std::memcpy(out + i, symbol_ptr, sizeof(float) * symbol_len);

    i += symbol_len;
    z++;
  }


  // Tell runtime system how many output items we produced.
  return noutput_items;
}

} /* namespace owc */
} /* namespace gr */
