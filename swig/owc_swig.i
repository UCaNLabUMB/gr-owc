/* -*- c++ -*- */

#define OWC_API

%include "gnuradio.i"           // the common stuff

//load generated python docstrings
%include "owc_swig_doc.i"

%{
#include "owc/OWC_Channel_relative.h"
#include "owc/OWC_Channel_absolute.h"
#include "owc/OOK_Modulator_one.h"
#include "owc/OOK_Modulator_two.h"
#include "owc/binary_to_decimal_mapper.h"
#include "owc/PAM_Modulator_one.h"
#include "owc/PAM_Modulator_two.h"
#include "owc/VPPM_Modulator_one.h"
#include "owc/VPPM_Modulator_two.h"
%}

%include "owc/OWC_Channel_relative.h"
GR_SWIG_BLOCK_MAGIC2(owc, OWC_Channel_relative);
%include "owc/OWC_Channel_absolute.h"
GR_SWIG_BLOCK_MAGIC2(owc, OWC_Channel_absolute);

%include "owc/OOK_Modulator_one.h"
GR_SWIG_BLOCK_MAGIC2(owc, OOK_Modulator_one);
%include "owc/OOK_Modulator_two.h"
GR_SWIG_BLOCK_MAGIC2(owc, OOK_Modulator_two);
%include "owc/binary_to_decimal_mapper.h"
GR_SWIG_BLOCK_MAGIC2(owc, binary_to_decimal_mapper);
%include "owc/PAM_Modulator_one.h"
GR_SWIG_BLOCK_MAGIC2(owc, PAM_Modulator_one);
%include "owc/PAM_Modulator_two.h"
GR_SWIG_BLOCK_MAGIC2(owc, PAM_Modulator_two);

%include "owc/VPPM_Modulator_one.h"
GR_SWIG_BLOCK_MAGIC2(owc, VPPM_Modulator_one);
%include "owc/VPPM_Modulator_two.h"
GR_SWIG_BLOCK_MAGIC2(owc, VPPM_Modulator_two);
