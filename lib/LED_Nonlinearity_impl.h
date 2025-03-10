/* -*- c++ -*- */
/* gr-owc OOT module for optical wireless communications.
 * gr-owc is compatible with GNU Radio v3.10
 *
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
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

#ifndef INCLUDED_OWC_LED_NONLINEARITY_IMPL_H
#define INCLUDED_OWC_LED_NONLINEARITY_IMPL_H

#include <gnuradio/owc/LED_Nonlinearity.h>

namespace gr {
namespace owc {

class LED_Nonlinearity_impl : public LED_Nonlinearity {
private:
  float d_L;
  float d_k;
  float d_x0;

public:
  LED_Nonlinearity_impl(float L, float k, float x0);
  ~LED_Nonlinearity_impl();

  void set_Maximum(float L) { d_L = L; }
  float Maximum() { return d_L; }

  void set_Steepness(float k) { d_k = k; }
  float Steepness() { return d_k;}

  void set_Inflextion_Point(float x0) { d_x0 = x0; }
  float Inflextion_Point() { return d_x0;}

  // Where all the action really happens
  int work(int noutput_items, gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_LED_NONLINEARITY_IMPL_H */
