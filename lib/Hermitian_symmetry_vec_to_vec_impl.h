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

#ifndef INCLUDED_OWC_HERMITIAN_SYMMETRY_VEC_TO_VEC_IMPL_H
#define INCLUDED_OWC_HERMITIAN_SYMMETRY_VEC_TO_VEC_IMPL_H

#include <owc/Hermitian_symmetry_vec_to_vec.h>

namespace gr {
  namespace owc {

    class Hermitian_symmetry_vec_to_vec_impl : public Hermitian_symmetry_vec_to_vec
    {
     private:
      int d_fft_len;
      
      int d_current_num_remaining_samples;
      
      std::vector<gr_complex> d_remaining_input_samples;

     public:
      Hermitian_symmetry_vec_to_vec_impl(int fft_len);
      ~Hermitian_symmetry_vec_to_vec_impl();
      
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

#endif /* INCLUDED_OWC_HERMITIAN_SYMMETRY_VEC_TO_VEC_IMPL_H */

