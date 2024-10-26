/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OWC_OOK_MODULATOR_CPLUS_H
#define INCLUDED_OWC_OOK_MODULATOR_CPLUS_H

#include <gnuradio/owc/api.h>
#include <gnuradio/sync_interpolator.h>

namespace gr {
namespace owc {

/*!
 * \brief <+description of block+>
 * \ingroup owc
 *
 */
class OWC_API OOK_Modulator_cplus : virtual public gr::sync_interpolator {
public:
  typedef std::shared_ptr<OOK_Modulator_cplus> sptr;

  /*!
   * \brief Return a shared_ptr to a new instance of owc::OOK_Modulator_cplus.
   *
   * To avoid accidental use of raw pointers, owc::OOK_Modulator_cplus's
   * constructor is in a private implementation
   * class. owc::OOK_Modulator_cplus::make is the public interface for
   * creating new instances.
   */
  static sptr make(float max_mag, float min_mag, int samples_per_symbol);

  virtual void set_max_magnitude(float max_mag) = 0;
  virtual float max_magnitude() = 0;
      
  virtual void set_min_magnitude(float min_mag) = 0;
  virtual float min_magnitude() = 0;

  virtual void set_samples_per_symbol(int samples_per_symbol) = 0;
  virtual int samples_per_symbol() = 0;

};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OOK_MODULATOR_CPLUS_H */
