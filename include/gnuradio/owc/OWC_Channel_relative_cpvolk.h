/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OWC_OWC_CHANNEL_RELATIVE_CPVOLK_H
#define INCLUDED_OWC_OWC_CHANNEL_RELATIVE_CPVOLK_H

#include <gnuradio/owc/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
namespace owc {

/*!
 * \brief <+description of block+>
 * \ingroup owc
 *
 */
class OWC_API OWC_Channel_relative_cpvolk : virtual public gr::sync_block
{
public:
    typedef std::shared_ptr<OWC_Channel_relative_cpvolk> sptr;

    /*!
     * \brief Return a shared_ptr to a new instance of owc::OWC_Channel_relative_cpvolk.
     *
     * To avoid accidental use of raw pointers, owc::OWC_Channel_relative_cpvolk's
     * constructor is in a private implementation
     * class. owc::OWC_Channel_relative_cpvolk::make is the public interface for
     * creating new instances.
     */
    static sptr make(int num_inputs, int num_outputs, const std::vector<float>& emission_angle_array, const std::vector<float>& acceptance_angle_array, const std::vector<float>& distance_array, const std::vector<float>& lambertian_order_array, const std::vector<float>& photosensor_area_array, const std::vector<float>& optical_filter_transmittance_array, const std::vector<float>& refractive_index_array, bool clip_neg, bool shot_noise, float sample_rate, float responsivity, const std::vector<float>& concentrator_FOV_array, const std::vector<float>& E2O_conversion_factor_array, const std::vector<float>& O2E_conversion_factor_array);

    virtual void set_emission_angle_array(std::vector<float> emission_angle_array) = 0;
    virtual std::vector<float> emission_angle_array() = 0;
      
    virtual void set_acceptance_angle_array(std::vector<float> acceptance_angle_array) = 0;
    virtual std::vector<float> acceptance_angle_array() = 0;
      
    virtual void set_distance_array(std::vector<float> distance_array) = 0;
    virtual std::vector<float> distance_array() = 0;
      
    virtual void set_lambertian_order_array(std::vector<float> lambertian_order_array) = 0;
    virtual std::vector<float> lambertian_order_array() = 0;
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OWC_CHANNEL_RELATIVE_CPVOLK_H */
