/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OWC_OOK_DEMODULATOR_CPLUS_IMPL_H
#define INCLUDED_OWC_OOK_DEMODULATOR_CPLUS_IMPL_H

#include <gnuradio/owc/OOK_Demodulator_cplus.h>

namespace gr {
namespace owc {

class OOK_Demodulator_cplus_impl : public OOK_Demodulator_cplus {
private:
  float d_threshold;
  int d_samples_per_symbol;

public:
  OOK_Demodulator_cplus_impl(float threshold, int samples_per_symbol);
  ~OOK_Demodulator_cplus_impl();

  void set_threshold(float threshold) { d_threshold = threshold; }
  float threshold() { return d_threshold; }

  void set_samples_per_symbol(int samples_per_symbol) { d_samples_per_symbol = samples_per_symbol; }
  int samples_per_symbol() { return d_samples_per_symbol;}

  int work(int noutput_items, gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OOK_DEMODULATOR_CPLUS_IMPL_H */
