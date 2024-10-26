/* -*- c++ -*- */
/*
 * Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OWC_OOK_DEMODULATOR_CPLUS_H
#define INCLUDED_OWC_OOK_DEMODULATOR_CPLUS_H

#include <gnuradio/owc/api.h>
#include <gnuradio/sync_decimator.h>

namespace gr {
namespace owc {

/*!
 * \brief <+description of block+>
 * \ingroup owc
 *
 */
class OWC_API OOK_Demodulator_cplus : virtual public gr::sync_decimator {
public:
  typedef std::shared_ptr<OOK_Demodulator_cplus> sptr;

  /*!
   * \brief Return a shared_ptr to a new instance of owc::OOK_Demodulator_cplus.
   *
   * To avoid accidental use of raw pointers, owc::OOK_Demodulator_cplus's
   * constructor is in a private implementation
   * class. owc::OOK_Demodulator_cplus::make is the public interface for
   * creating new instances.
   */
  static sptr make(float threshold, int samples_per_symbol);
  virtual void set_threshold(float threshold) = 0;
  virtual float threshold() = 0;
};

} // namespace owc
} // namespace gr

#endif /* INCLUDED_OWC_OOK_DEMODULATOR_CPLUS_H */
