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

#ifndef INCLUDED_OWC_VPPM_MODULATOR_TWO_IMPL_H
#define INCLUDED_OWC_VPPM_MODULATOR_TWO_IMPL_H

#include <owc/VPPM_Modulator_two.h>

namespace gr {
  namespace owc {

    class VPPM_Modulator_two_impl : public VPPM_Modulator_two
    {
     private:
     float d_amplitude;
     float d_mean;
     int d_samples_per_symbol;
     int d_samples_per_pulse;

     public:
      VPPM_Modulator_two_impl(float amplitude, float mean, int samples_per_symbol, int samples_per_pulse);
      ~VPPM_Modulator_two_impl();
      
      void set_amplitude(float amplitude) { d_amplitude = amplitude; }
      float amplitude() { return d_amplitude; }
      
      void set_mean(float mean) { d_mean = mean; }
      float mean() { return d_mean; }

      void set_samples_per_symbol(int samples_per_symbol) { d_samples_per_symbol = samples_per_symbol; }
      int samples_per_symbol() { return d_samples_per_symbol; }
      
      void set_samples_per_pulse(int samples_per_pulse) { d_samples_per_pulse = samples_per_pulse; }
      int samples_per_pulse() { return d_samples_per_pulse; }

      // Where all the action really happens
      int work(
              int noutput_items,
              gr_vector_const_void_star &input_items,
              gr_vector_void_star &output_items
      );
    };

  } // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_VPPM_MODULATOR_TWO_IMPL_H */

