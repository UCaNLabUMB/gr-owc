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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "VPPM_Modulator_one_impl.h"

namespace gr {
  namespace owc {

    VPPM_Modulator_one::sptr
    VPPM_Modulator_one::make(float max_magnitude, float min_magnitude, int samples_per_symbol, int samples_per_pulse)
    {
      return gnuradio::get_initial_sptr
        (new VPPM_Modulator_one_impl(max_magnitude, min_magnitude, samples_per_symbol, samples_per_pulse));
    }


    /*
     * The private constructor
     */
    VPPM_Modulator_one_impl::VPPM_Modulator_one_impl(float max_magnitude, float min_magnitude, int samples_per_symbol, int samples_per_pulse)
      : gr::sync_interpolator("VPPM_Modulator_one",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)), samples_per_symbol)
    {
    	set_max_magnitude(max_magnitude);
    	set_min_magnitude(min_magnitude);
    	set_samples_per_symbol(samples_per_symbol);
    	set_samples_per_pulse(samples_per_pulse);
    }

    /*
     * Our virtual destructor.
     */
    VPPM_Modulator_one_impl::~VPPM_Modulator_one_impl()
    {
    }

    int
    VPPM_Modulator_one_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      int i = 0;
      int z = 0;
      
      while(i < noutput_items) {
      		for (int j = 0; j < samples_per_symbol(); j++){
      			if (in[z] == 0) 
      			{
      				if (j < samples_per_pulse())
      				{
      					out[i++] = max_magnitude();
      				}
      				else
      				{
      					out[i++] = min_magnitude();
      				}
      			}
      			
      			else 
      			{
      				if (j >= samples_per_symbol() - samples_per_pulse())
      				{
      					out[i++] = max_magnitude();
      				}
      				else
      				{
      					out[i++] = min_magnitude();
      				}
      			}
      			
      		}
      	z++;}

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace owc */
} /* namespace gr */

