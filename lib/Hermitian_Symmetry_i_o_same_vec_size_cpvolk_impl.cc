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

#include "Hermitian_Symmetry_i_o_same_vec_size_cpvolk_impl.h"
#include <gnuradio/io_signature.h>
#include <volk/volk.h>

namespace gr {
namespace owc {

using input_type = gr_complex;

using output_type = gr_complex;

Hermitian_Symmetry_i_o_same_vec_size_cpvolk::sptr
Hermitian_Symmetry_i_o_same_vec_size_cpvolk::make(int fft_len, bool use_negative_coefficients) {
  return gnuradio::make_block_sptr<
      Hermitian_Symmetry_i_o_same_vec_size_cpvolk_impl>(
      fft_len, use_negative_coefficients);
}

/*
 * The private constructor
 */
Hermitian_Symmetry_i_o_same_vec_size_cpvolk_impl::
    Hermitian_Symmetry_i_o_same_vec_size_cpvolk_impl(int fft_len, bool use_negative_coefficients)
    : gr::sync_block(
          "Hermitian_Symmetry_i_o_same_vec_size_cpvolk",
          gr::io_signature::make(1 , 1 , sizeof(input_type) * fft_len),
          gr::io_signature::make(1 , 1 , sizeof(output_type) * fft_len)) 
    {
        set_fft_len(fft_len);
        set_use_negative_coefficients(use_negative_coefficients);
    }

/*
 * Our virtual destructor.
 */
Hermitian_Symmetry_i_o_same_vec_size_cpvolk_impl::
    ~Hermitian_Symmetry_i_o_same_vec_size_cpvolk_impl() {}

int Hermitian_Symmetry_i_o_same_vec_size_cpvolk_impl::work(
    int noutput_items, gr_vector_const_void_star &input_items,
    gr_vector_void_star &output_items) {

    const gr_complex* in = (const gr_complex*)input_items[0];
    gr_complex* out = (gr_complex*)output_items[0];
    
    int mid = fft_len() / 2;

    std::vector<gr_complex> temp_buffer(mid - 1);
    std::vector<gr_complex> ones((mid-1), gr_complex(1.0f, 0.0f));

    for (int i = 0; i < noutput_items; i++) {
        gr_complex* out_vec = &out[i * fft_len()];
        const gr_complex* in_vec = &in[i * fft_len()];

        out_vec[0] = gr_complex(0, 0);         
        out_vec[mid] = gr_complex(0, 0);       

        if (use_negative_coefficients()) {
            volk_32fc_x2_multiply_32fc(&out_vec[1], &in_vec[1], ones.data(), (mid - 1));
            std::reverse_copy(&in_vec[1], &in_vec[mid], temp_buffer.begin());
            volk_32fc_conjugate_32fc(&out_vec[mid+1], temp_buffer.data(), mid - 1);
        } else {
            volk_32fc_x2_multiply_32fc(&out_vec[mid + 1], &in_vec[mid + 1], ones.data(), (mid - 1));
            std::reverse_copy(&in_vec[mid + 1], &in_vec[d_fft_len], temp_buffer.begin());
            volk_32fc_conjugate_32fc(&out_vec[1], temp_buffer.data(), mid - 1);
    }
  }


  // Tell runtime system how many output items we produced.
  return noutput_items;
}

} /* namespace owc */
} /* namespace gr */
