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

#ifndef INCLUDED_OWC_VPPM_DEMODULATOR_CPLUS_IMPL_H
#define INCLUDED_OWC_VPPM_DEMODULATOR_CPLUS_IMPL_H

#include <gnuradio/owc/VPPM_Demodulator_cplus.h>

namespace gr {
namespace owc {

class VPPM_Demodulator_cplus_impl : public VPPM_Demodulator_cplus {
private:
  int d_samples_per_symbol;
  int d_samples_per_pulse;

  std::vector<float> case1;
  std::vector<float> case0;

  void initialize_vector(){
    int symbol_len = samples_per_symbol();
    int pulse_len = samples_per_pulse();
    int rest_len = symbol_len - pulse_len;
    case0.resize(symbol_len);
    case1.resize(symbol_len);

    for (int j = 0; j < symbol_len; j++) {
      if (j < pulse_len)
        case0[j] = 1.0;
      else
        case0[j] = 0.0;

      if (j < rest_len)
        case1[j] = 0.0;
      else
        case1[j] = 1.0;
    }
  }

  float matched_filter(std::vector<float> samples_array){
    float v1 = 0;
    float v0 = 0;
        
    for (int x = 0; x < d_samples_per_symbol; x++)
    {
      v1 += samples_array[x] * case1[x];
      v0 += samples_array[x] * case0[x];
    }
              
    return (v1 > v0) ? 1.0 : 0.0;
  }

public:
  VPPM_Demodulator_cplus_impl(int samples_per_symbol, int samples_per_pulse);
  ~VPPM_Demodulator_cplus_impl();

  void set_samples_per_symbol(int samples_per_symbol) { d_samples_per_symbol = samples_per_symbol; }
  int samples_per_symbol() { return d_samples_per_symbol; }
      
  void set_samples_per_pulse(int samples_per_pulse) { d_samples_per_pulse = samples_per_pulse; }
  int samples_per_pulse() { return d_samples_per_pulse; }

  // Where all the action really happens
  int work(int noutput_items, gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_VPPM_DEMODULATOR_CPLUS_IMPL_H */
