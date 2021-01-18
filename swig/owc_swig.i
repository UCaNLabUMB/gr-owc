/* -*- c++ -*- */

#define OWC_API

%include "gnuradio.i"           // the common stuff

//load generated python docstrings
%include "owc_swig_doc.i"

%{
#include "owc/OWC_Channel_relative.h"
#include "owc/OWC_Channel_absolute.h"
%}

%include "owc/OWC_Channel_relative.h"
GR_SWIG_BLOCK_MAGIC2(owc, OWC_Channel_relative);
%include "owc/OWC_Channel_absolute.h"
GR_SWIG_BLOCK_MAGIC2(owc, OWC_Channel_absolute);
