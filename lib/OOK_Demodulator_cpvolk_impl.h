/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OWC_OOK_DEMODULATOR_CPVOLK_IMPL_H
#define INCLUDED_OWC_OOK_DEMODULATOR_CPVOLK_IMPL_H

#include <gnuradio/owc/OOK_Demodulator_cpvolk.h>

namespace gr {
namespace owc {

class OOK_Demodulator_cpvolk_impl : public OOK_Demodulator_cpvolk {
private:
  float d_threshold;
  int d_samples_per_symbol;

public:
  OOK_Demodulator_cpvolk_impl(float threshold, int samples_per_symbol);
  ~OOK_Demodulator_cpvolk_impl();

  void set_threshold(float threshold) { d_threshold = threshold; }
  float threshold() { return d_threshold; }

  void set_samples_per_symbol(int samples_per_symbol) { d_samples_per_symbol = samples_per_symbol; }
  int samples_per_symbol() { return d_samples_per_symbol;}

  // Where all the action really happens
  int work(int noutput_items, gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OOK_DEMODULATOR_CPVOLK_IMPL_H */
