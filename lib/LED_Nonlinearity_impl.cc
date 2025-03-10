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

#include "LED_Nonlinearity_impl.h"
#include <gnuradio/io_signature.h>
#include <volk/volk.h>
#include <algorithm>
//#include<cmath>

namespace gr {
namespace owc {


using input_type = float;

using output_type = float;

LED_Nonlinearity::sptr LED_Nonlinearity::make(float L, float k, float x0) {
  return gnuradio::make_block_sptr<LED_Nonlinearity_impl>(
    L, 
    k, 
    x0
    );
}

/*
 * The private constructor
 */
LED_Nonlinearity_impl::LED_Nonlinearity_impl(float L, float k, float x0)
    : gr::sync_block(
          "LED_Nonlinearity",
          gr::io_signature::make(1 , 1 ,
                                 sizeof(input_type)),
          gr::io_signature::make(1 , 1 ,
                                 sizeof(output_type))) 
    {
      set_Maximum(L);
      set_Steepness(k);
      set_Inflextion_Point(x0);
    }

/*
 * Our virtual destructor.
 */
LED_Nonlinearity_impl::~LED_Nonlinearity_impl() {}

int LED_Nonlinearity_impl::work(int noutput_items,
                                gr_vector_const_void_star &input_items,
                                gr_vector_void_star &output_items) {
  const float *in = (const float *) input_items[0];
  float *out = (float *) output_items[0];

  float *exp_values = (float *)volk_malloc(noutput_items * sizeof(float), volk_get_alignment());
  float *denom_values = (float *)volk_malloc(noutput_items * sizeof(float), volk_get_alignment());

  float *x0_values = (float *)volk_malloc(noutput_items * sizeof(float), volk_get_alignment());
  std::fill_n(x0_values, noutput_items, Inflextion_Point());
  float *L_values = (float *)volk_malloc(noutput_items * sizeof(float), volk_get_alignment());
  std::fill_n(L_values, noutput_items, Maximum());
  float *one_values = (float *)volk_malloc(noutput_items * sizeof(float), volk_get_alignment());
  std::fill_n(one_values, noutput_items, 1.0f);
  float st = -Steepness();

  volk_32f_x2_subtract_32f(exp_values, in, x0_values, noutput_items);   
  volk_32f_s32f_multiply_32f(exp_values, exp_values, st, noutput_items); 
  volk_32f_expfast_32f(exp_values, exp_values, noutput_items); 
         
  volk_32f_x2_add_32f(denom_values, exp_values, one_values, noutput_items); 
  volk_32f_x2_divide_32f(out, L_values, denom_values, noutput_items);

  volk_free(exp_values);
  volk_free(denom_values);
  volk_free(x0_values);
  volk_free(one_values);
  volk_free(L_values);

/*  float x0 = Inflextion_Point();
  float L = Maximum();
  float k = Steepness();

  for (int i = 0; i < noutput_items; i++) {
      float exponent = -k * (in[i] - x0);
      float denom = 1.0f + std::exp(exponent);
      out[i] = L / denom;
  }*/

  // Tell runtime system how many output items we produced.
  return noutput_items;
}

} /* namespace owc */
} /* namespace gr */
