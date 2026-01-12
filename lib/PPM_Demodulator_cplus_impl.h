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

#ifndef INCLUDED_OWC_PPM_DEMODULATOR_CPLUS_IMPL_H
#define INCLUDED_OWC_PPM_DEMODULATOR_CPLUS_IMPL_H

#include <gnuradio/owc/PPM_Demodulator_cplus.h>

namespace gr {
namespace owc {

class PPM_Demodulator_cplus_impl : public PPM_Demodulator_cplus {
private:
  int d_samples_per_symbol;
  int d_samples_per_pulse;
  int d_modulation_order;
  std::vector<std::vector<float>> cases;

  void initialize_vector_PPM(){
    const int slot = samples_per_symbol() / modulation_order(); 

    cases.assign(modulation_order(), std::vector<float>(samples_per_symbol(), 0.0f));

    for (int k = 0; k < modulation_order(); k++) {
        int start = k * slot;

        for (int n = 0; n < samples_per_pulse(); n++) {
            int i = start + n;
            if (i < samples_per_symbol()) {
                cases[k][i] = 1.0f;
            }
        }
    }
  }

  float matched_filter_ppm(std::vector<float> samples_array){
 
    int best_k = -1;
    float best_metric = std::numeric_limits<float>::min();

    for (int k = 0; k < modulation_order(); k++) {
        float metric = 0.0f;
        for (int x = 0; x < samples_per_symbol(); x++) {
            metric += samples_array[x] * cases[k][x];
        }

        if (metric > best_metric) {
            best_metric = metric;
            best_k = k;
        }
    }

    return (float)best_k;
  }

public:
  PPM_Demodulator_cplus_impl(int samples_per_symbol, int samples_per_pulse, int modulation_order);
  ~PPM_Demodulator_cplus_impl();

  void set_samples_per_symbol(int samples_per_symbol) { d_samples_per_symbol = samples_per_symbol;}
  int samples_per_symbol() { return d_samples_per_symbol; }
      
  void set_samples_per_pulse(int samples_per_pulse) { d_samples_per_pulse = samples_per_pulse;}
  int samples_per_pulse() { return d_samples_per_pulse; }

  void set_modulation_order(int modulation_order) { d_modulation_order = modulation_order;}
  int modulation_order() { return d_modulation_order; }

  // Where all the action really happens
  int work(int noutput_items, gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_PPM_DEMODULATOR_CPLUS_IMPL_H */
