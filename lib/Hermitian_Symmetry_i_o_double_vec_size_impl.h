/* -*- c++ -*- */
/* gr-owc OOT module for optical wireless communications. 
 *
 * Copyright 2021 Arsalan Ahmed from The Ubiquitous Communications and Networking (UCAN) Lab, University of Massachusetts, Boston.
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

#ifndef INCLUDED_OWC_HERMITIAN_SYMMETRY_I_O_DOUBLE_VEC_SIZE_IMPL_H
#define INCLUDED_OWC_HERMITIAN_SYMMETRY_I_O_DOUBLE_VEC_SIZE_IMPL_H

#include <owc/Hermitian_Symmetry_i_o_double_vec_size.h>

namespace gr {
  namespace owc {

    class Hermitian_Symmetry_i_o_double_vec_size_impl : public Hermitian_Symmetry_i_o_double_vec_size
    {
     private:
      int d_fft_len;

     public:
      Hermitian_Symmetry_i_o_double_vec_size_impl(int fft_len);
      ~Hermitian_Symmetry_i_o_double_vec_size_impl();
      
      void set_fft_len(int fft_len){d_fft_len = fft_len;}
      int fft_len() {return d_fft_len;}

      // Where all the action really happens
      int work(
              int noutput_items,
              gr_vector_const_void_star &input_items,
              gr_vector_void_star &output_items
      );
    };

  } // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_HERMITIAN_SYMMETRY_I_O_DOUBLE_VEC_SIZE_IMPL_H */

