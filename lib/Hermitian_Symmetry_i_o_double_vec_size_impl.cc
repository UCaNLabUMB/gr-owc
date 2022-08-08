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
#include "Hermitian_Symmetry_i_o_double_vec_size_impl.h"

namespace gr {
  namespace owc {

    Hermitian_Symmetry_i_o_double_vec_size::sptr
    Hermitian_Symmetry_i_o_double_vec_size::make(int fft_len)
    {
      return gnuradio::get_initial_sptr
        (new Hermitian_Symmetry_i_o_double_vec_size_impl(fft_len));
    }


    /*
     * The private constructor
     */
    Hermitian_Symmetry_i_o_double_vec_size_impl::Hermitian_Symmetry_i_o_double_vec_size_impl(int fft_len)
      : gr::sync_block("Hermitian_Symmetry_i_o_double_vec_size",
              gr::io_signature::make(1, 1, sizeof(gr_complex) * fft_len),
              gr::io_signature::make(1, 1, sizeof(gr_complex) * fft_len * 2))
    {
    	set_fft_len(fft_len);
    }

    /*
     * Our virtual destructor.
     */
    Hermitian_Symmetry_i_o_double_vec_size_impl::~Hermitian_Symmetry_i_o_double_vec_size_impl()
    {
    }

    int
    Hermitian_Symmetry_i_o_double_vec_size_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
	    const gr_complex* in = (const gr_complex*)input_items[0];
	    gr_complex* out = (gr_complex*)output_items[0];
	    //Only allocate the subcarriers on the negative half using the carrier allocator bloc before this block.
	    int zeroth_subcarrier = 0;
	    
	    int output_index = 0;
	    	    
	    for (int i=0; i < noutput_items; i++)      //output_items are actually vectors.
	    {
	    	int sub_carrier_counter = 0;
	    	
	    	std::vector<gr_complex> incoming_samples;
	    	
	    	for (int j = i * fft_len(); j < (i * fft_len()) + fft_len(); j++)
	    	{
	    		if (sub_carrier_counter == zeroth_subcarrier)
	    		{
	    			out[output_index] = 0;                     //Dont allocate the zeroth (firstmost) subcarrier
	    			output_index++;
	    		} 		
	   		else
	    		{
	    			out[output_index] = in[j];
	    			output_index++;
	    			
	    			incoming_samples.push_back(in[j]);
	    		}
	    		
	    		if (sub_carrier_counter == fft_len() - 1)
	    		{
	    			std::reverse(incoming_samples.begin(), incoming_samples.end());
	    			for (int k=0; k < fft_len(); k++)
	    			{	    				
	    				if (k == 0)
	    				{
	    					out[output_index] = 0;
	    					output_index++;
	    				}
	    				else
	    				{
	    					out[output_index] = std::conj(incoming_samples[k - 1]);
	    					output_index++;	
	    				}
	    			}
	    			incoming_samples.clear();
	    		}
	    		sub_carrier_counter++;
	    	}
	    }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace owc */
} /* namespace gr */

