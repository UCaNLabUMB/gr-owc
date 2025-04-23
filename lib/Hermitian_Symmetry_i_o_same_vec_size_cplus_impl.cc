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

#include "Hermitian_Symmetry_i_o_same_vec_size_cplus_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace owc {

using input_type = gr_complex;

using output_type = gr_complex;

Hermitian_Symmetry_i_o_same_vec_size_cplus::sptr
Hermitian_Symmetry_i_o_same_vec_size_cplus::make(int fft_len, bool use_negative_coefficients) {
  return gnuradio::make_block_sptr<
      Hermitian_Symmetry_i_o_same_vec_size_cplus_impl>(
      fft_len, use_negative_coefficients);
}

/*
 * The private constructor
 */
Hermitian_Symmetry_i_o_same_vec_size_cplus_impl::
    Hermitian_Symmetry_i_o_same_vec_size_cplus_impl(int fft_len, bool use_negative_coefficients)
    : gr::sync_block(
          "Hermitian_Symmetry_i_o_same_vec_size_cplus",
          gr::io_signature::make(1 , 1 , sizeof(input_type) * fft_len),
          gr::io_signature::make(1 , 1 , sizeof(output_type) * fft_len)) 
    {
        set_fft_len(fft_len);
        set_use_negative_coefficients(use_negative_coefficients);
    }


/*
 * Our virtual destructor.
 */
Hermitian_Symmetry_i_o_same_vec_size_cplus_impl::
    ~Hermitian_Symmetry_i_o_same_vec_size_cplus_impl() {}

int Hermitian_Symmetry_i_o_same_vec_size_cplus_impl::work(
    int noutput_items, gr_vector_const_void_star &input_items,
    gr_vector_void_star &output_items) {
    const gr_complex* in = (const gr_complex*)input_items[0];
    gr_complex* out = (gr_complex*)output_items[0];

    int zeroth_subcarrier = 0;
    int middle_subcarrier = fft_len() / 2;

    for (int i = 0; i < noutput_items; i++) {
        int mid_subcarr_index = std::max(i * middle_subcarrier, middle_subcarrier);
        int sub_carrier_counter = 0;

        for (int j = i * fft_len(); j < (i + 1) * fft_len(); j++) {
            if (sub_carrier_counter == zeroth_subcarrier) {
                out[j] = 0;
            } else if (sub_carrier_counter == middle_subcarrier) {
                out[j] = 0;
            } else if (!use_negative_coefficients() && sub_carrier_counter < middle_subcarrier) {
                out[j] = in[j];
            } else if (!use_negative_coefficients()) {
                out[j] = std::conj(in[mid_subcarr_index - (j - mid_subcarr_index)]);
            } else if (use_negative_coefficients() && sub_carrier_counter > middle_subcarrier) {
                out[j] = in[j];
            } else if (use_negative_coefficients()) {
                out[j] = std::conj(in[mid_subcarr_index + (mid_subcarr_index - j)]);
            }
        sub_carrier_counter++;
        }
    }


  // Tell runtime system how many output items we produced.
  return noutput_items;
}

} /* namespace owc */
} /* namespace gr */
