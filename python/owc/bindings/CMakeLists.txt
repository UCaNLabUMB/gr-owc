# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT owc_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT owc_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND owc_python_files
    OWC_Channel_relative_cplus_python.cc
    OWC_Channel_relative_cpvolk_python.cc
    OOK_Modulator_cplus_python.cc
    OOK_Demodulator_cplus_python.cc
    OOK_Demodulator_cpvolk_python.cc
    OWC_Channel_absolute_cplus_python.cc
    OWC_Channel_absolute_cvolk_python.cc
    PAM_Modulator_cplus_python.cc
    VPPM_Modulator_cplus_python.cc
    PPM_Modulator_cplus_python.cc
    LED_Nonlinearity_python.cc python_bindings.cc)

GR_PYBIND_MAKE_OOT(owc
   ../../..
   gr::owc
   "${owc_python_files}")

# copy bindings extension for use in QA test module
add_custom_command(TARGET owc_python POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:owc_python>
    ${PROJECT_BINARY_DIR}/test_modules/gnuradio/owc/
)

install(TARGETS owc_python DESTINATION ${GR_PYTHON_DIR}/gnuradio/owc COMPONENT pythonapi)
