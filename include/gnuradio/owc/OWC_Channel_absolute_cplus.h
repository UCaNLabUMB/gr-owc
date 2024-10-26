/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OWC_OWC_CHANNEL_ABSOLUTE_CPLUS_H
#define INCLUDED_OWC_OWC_CHANNEL_ABSOLUTE_CPLUS_H

#include <gnuradio/owc/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
namespace owc {

/*!
 * \brief <+description of block+>
 * \ingroup owc
 *
 */
class OWC_API OWC_Channel_absolute_cplus : virtual public gr::sync_block {
public:
  typedef std::shared_ptr<OWC_Channel_absolute_cplus> sptr;

  /*!
   * \brief Return a shared_ptr to a new instance of owc::OWC_Channel_absolute_cplus.
   *
   * To avoid accidental use of raw pointers, owc::OWC_Channel_absolute_cplus's
   * constructor is in a private implementation
   * class. owc::OWC_Channel_absolute_cplus::make is the public interface for
   * creating new instances.
   */
  static sptr make(
      int num_inputs, int num_outputs, const std::vector<float>& tx_coordinates_array, const std::vector<float>& tx_orientation_array, const std::vector<float>& rx_coordinates_array, const std::vector<float>& rx_orientation_array, const std::vector<float>& tx_lambertian_order_array, const std::vector<float>& rx_photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array);

  virtual void set_tx_coordinates_array(std::vector<float> tx_coordinates_array) = 0;
  virtual std::vector<float> tx_coordinates_array() = 0;   
      
  virtual void set_tx_orientation_array(std::vector<float> tx_orientation_array) = 0;
  virtual std::vector<float> tx_orientation_array() = 0; 
      
  virtual void set_rx_coordinates_array(std::vector<float> rx_coordinates_array) = 0;
  virtual std::vector<float> rx_coordinates_array() = 0;    
      
  virtual void set_rx_orientation_array(std::vector<float> rx_orientation_array) = 0;
  virtual std::vector<float> rx_orientation_array() = 0; 
      
  virtual void set_tx_lambertian_order_array(std::vector<float> lambertian_order_array) = 0;
  virtual std::vector<float> tx_lambertian_order_array() = 0; 
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OWC_CHANNEL_ABSOLUTE_CPLUS_H */
