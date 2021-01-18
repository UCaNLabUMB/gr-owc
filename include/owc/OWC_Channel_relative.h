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

#ifndef INCLUDED_OWC_OWC_CHANNEL_RELATIVE_H
#define INCLUDED_OWC_OWC_CHANNEL_RELATIVE_H

#include <owc/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace owc {

    /*!
     * \brief <+description of block+>
     * \ingroup owc
     *
     */
    class OWC_API OWC_Channel_relative : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<OWC_Channel_relative> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of owc::OWC_Channel_relative.
       *
       * To avoid accidental use of raw pointers, owc::OWC_Channel_relative's
       * constructor is in a private implementation
       * class. owc::OWC_Channel_relative::make is the public interface for
       * creating new instances.
       */
      static sptr make(int num_inputs, int num_outputs, const std::vector<float>& emission_angle_array, const std::vector<float>& acceptance_angle_array, const std::vector<float>& distance_array, const std::vector<float>& lambertian_order_array, const std::vector<float>& photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array);
      
      virtual void set_emission_angle_array(std::vector<float> emission_angle_array) = 0;
      virtual std::vector<float> emission_angle_array() = 0;
      
      virtual void set_acceptance_angle_array(std::vector<float> acceptance_angle_array) = 0;
      virtual std::vector<float> acceptance_angle_array() = 0;
      
      virtual void set_distance_array(std::vector<float> distance_array) = 0;
      virtual std::vector<float> distance_array() = 0;
      
    };

  } // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OWC_CHANNEL_RELATIVE_H */

