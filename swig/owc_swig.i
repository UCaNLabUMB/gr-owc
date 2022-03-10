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
#include "owc/OOK_Demodulator.h"
#include "owc/PAM_Demodulator.h"
#include "owc/decimal_to_binary_mapper.h"
#include "owc/VPPM_Demodulator.h"
#include "owc/OWC_Channel_relative_two.h"
#include "owc/OWC_Channel_absolute_two.h"
#include "owc/Hermitian_symmetry_vec_to_vec.h"
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
%include "owc/OOK_Demodulator.h"
GR_SWIG_BLOCK_MAGIC2(owc, OOK_Demodulator);
%include "owc/PAM_Demodulator.h"
GR_SWIG_BLOCK_MAGIC2(owc, PAM_Demodulator);
%include "owc/decimal_to_binary_mapper.h"
GR_SWIG_BLOCK_MAGIC2(owc, decimal_to_binary_mapper);
%include "owc/VPPM_Demodulator.h"
GR_SWIG_BLOCK_MAGIC2(owc, VPPM_Demodulator);
%include "owc/OWC_Channel_relative_two.h"
GR_SWIG_BLOCK_MAGIC2(owc, OWC_Channel_relative_two);
%include "owc/OWC_Channel_absolute_two.h"
GR_SWIG_BLOCK_MAGIC2(owc, OWC_Channel_absolute_two);


%include "owc/Hermitian_symmetry_vec_to_vec.h"
GR_SWIG_BLOCK_MAGIC2(owc, Hermitian_symmetry_vec_to_vec);
