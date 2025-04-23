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

#ifndef INCLUDED_OWC_HERMITIAN_SYMMETRY_I_O_SAME_VEC_SIZE_CPLUS_H
#define INCLUDED_OWC_HERMITIAN_SYMMETRY_I_O_SAME_VEC_SIZE_CPLUS_H

#include <gnuradio/owc/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
namespace owc {

/*!
 * \brief <+description of block+>
 * \ingroup owc
 *
 */
class OWC_API Hermitian_Symmetry_i_o_same_vec_size_cplus
    : virtual public gr::sync_block {
public:
  typedef std::shared_ptr<Hermitian_Symmetry_i_o_same_vec_size_cplus> sptr;

  /*!
   * \brief Return a shared_ptr to a new instance of
   * owc::Hermitian_Symmetry_i_o_same_vec_size_cplus.
   *
   * To avoid accidental use of raw pointers,
   * owc::Hermitian_Symmetry_i_o_same_vec_size_cplus's constructor is in a
   * private implementation class.
   * owc::Hermitian_Symmetry_i_o_same_vec_size_cplus::make is the public
   * interface for creating new instances.
   */
  static sptr make(int fft_len, bool use_negative_coefficients);
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_HERMITIAN_SYMMETRY_I_O_SAME_VEC_SIZE_CPLUS_H */
