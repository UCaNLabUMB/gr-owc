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

#ifndef INCLUDED_OWC_HERMITIAN_SYMMETRY_I_O_SAME_VEC_SIZE_CPLUS_IMPL_H
#define INCLUDED_OWC_HERMITIAN_SYMMETRY_I_O_SAME_VEC_SIZE_CPLUS_IMPL_H

#include <gnuradio/owc/Hermitian_Symmetry_i_o_same_vec_size_cplus.h>

namespace gr {
namespace owc {

class Hermitian_Symmetry_i_o_same_vec_size_cplus_impl
    : public Hermitian_Symmetry_i_o_same_vec_size_cplus {
private:
  int d_fft_len;
  bool d_use_negative_coefficients;

public:
  Hermitian_Symmetry_i_o_same_vec_size_cplus_impl(int fft_len, bool use_negative_coefficients);
  ~Hermitian_Symmetry_i_o_same_vec_size_cplus_impl();

  void set_fft_len(int fft_len){d_fft_len = fft_len;}
  int fft_len() {return d_fft_len;}

  void set_use_negative_coefficients(bool use_negative_coefficients){d_use_negative_coefficients = use_negative_coefficients;}
  bool use_negative_coefficients() {return d_use_negative_coefficients;}

  // Where all the action really happens
  int work(int noutput_items, gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_HERMITIAN_SYMMETRY_I_O_SAME_VEC_SIZE_CPLUS_IMPL_H */
