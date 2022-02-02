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

#ifndef INCLUDED_OWC_DCO_OFDM_HERMITIAN_SYMMETRY_H
#define INCLUDED_OWC_DCO_OFDM_HERMITIAN_SYMMETRY_H

#include <owc/api.h>
#include <gnuradio/sync_interpolator.h>

namespace gr {
  namespace owc {

    /*!
     * \brief <+description of block+>
     * \ingroup owc
     *
     */
    class OWC_API DCO_OFDM_Hermitian_Symmetry : virtual public gr::sync_interpolator
    {
     public:
      typedef boost::shared_ptr<DCO_OFDM_Hermitian_Symmetry> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of owc::DCO_OFDM_Hermitian_Symmetry.
       *
       * To avoid accidental use of raw pointers, owc::DCO_OFDM_Hermitian_Symmetry's
       * constructor is in a private implementation
       * class. owc::DCO_OFDM_Hermitian_Symmetry::make is the public interface for
       * creating new instances.
       */
      static sptr make(int fft_len);
    };

  } // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_DCO_OFDM_HERMITIAN_SYMMETRY_H */

