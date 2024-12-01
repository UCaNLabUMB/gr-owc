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

#include "PPM_Modulator_cplus_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace owc {

using input_type = float;
using output_type = float;

PPM_Modulator_cplus::sptr PPM_Modulator_cplus::make(float max_mag, float min_mag,
                                                    int samples_per_symbol,
                                                    int samples_per_pulse,
                                                    int modulation_order) {
  return gnuradio::make_block_sptr<PPM_Modulator_cplus_impl>(
      max_mag, min_mag, samples_per_symbol, samples_per_pulse,
      modulation_order);
}

/*
 * The private constructor
 */
PPM_Modulator_cplus_impl::PPM_Modulator_cplus_impl(float max_mag, float min_mag,
                                                   int samples_per_symbol,
                                                   int samples_per_pulse,
                                                   int modulation_order)
    : gr::sync_interpolator(
          "PPM_Modulator_cplus",
          gr::io_signature::make(1 , 1 , sizeof(input_type)),
          gr::io_signature::make(1 , 1 , sizeof(output_type)), samples_per_symbol) 
    {
      set_modulation_order(modulation_order); 
      set_max_magnitude(max_mag);
      set_min_magnitude(min_mag);
      set_samples_per_symbol(samples_per_symbol);
      set_samples_per_pulse(samples_per_pulse);
    }

/*
 * Our virtual destructor.
 */
PPM_Modulator_cplus_impl::~PPM_Modulator_cplus_impl() {}

int PPM_Modulator_cplus_impl::work(int noutput_items,
                                   gr_vector_const_void_star &input_items,
                                   gr_vector_void_star &output_items) {
  const float *in = (const float *)input_items[0];
  float *out = (float *)output_items[0];

  int i = 0;
  int z = 0;

  while (i < noutput_items) {
    int decimal = in[z];

    for (int j = 0; j < samples_per_symbol(); j++) {
      out[i + j] = min_magnitude();
    }

    int pulse = decimal * (samples_per_symbol() / modulation_order());

    for (int j = 0; j < samples_per_pulse(); j++) {
      if (pulse + j < samples_per_symbol()) {
        out[i + pulse + j] = max_magnitude();
      }
    }

    i += samples_per_symbol();
    z++;
  }


  // Tell runtime system how many output items we produced.
  return noutput_items;
}

} /* namespace owc */
} /* namespace gr */
