/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OWC_OOK_MODULATOR_CPLUS_IMPL_H
#define INCLUDED_OWC_OOK_MODULATOR_CPLUS_IMPL_H

#include <gnuradio/owc/OOK_Modulator_cplus.h>

namespace gr {
namespace owc {

class OOK_Modulator_cplus_impl : public OOK_Modulator_cplus {
private:
  float d_max_magnitude;
  float d_min_magnitude;
  int d_samples_per_symbol;

public:
  OOK_Modulator_cplus_impl(float max_mag, float min_mag, int samples_per_symbol);
  ~OOK_Modulator_cplus_impl();

  void set_max_magnitude(float max_magnitude) { d_max_magnitude = max_magnitude; }
  float max_magnitude() { return d_max_magnitude; }
      
  void set_min_magnitude(float min_magnitude) { d_min_magnitude = min_magnitude; }
  float min_magnitude() { return d_min_magnitude; }

  void set_samples_per_symbol(int samples_per_symbol) { d_samples_per_symbol = samples_per_symbol; }
  int samples_per_symbol() { return d_samples_per_symbol; }


  // Where all the action really happens
  int work(int noutput_items, gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OOK_MODULATOR_CPLUS_IMPL_H */
