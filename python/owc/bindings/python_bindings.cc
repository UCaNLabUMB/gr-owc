/*
 * Copyright 2020 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

#include <pybind11/pybind11.h>

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <numpy/arrayobject.h>

namespace py = pybind11;

// Headers for binding functions
/**************************************/
// The following comment block is used for
// gr_modtool to insert function prototypes
// Please do not delete
/**************************************/
// BINDING_FUNCTION_PROTOTYPES(
    void bind_OWC_Channel_relative_cplus(py::module& m);
    void bind_OWC_Channel_relative_cpvolk(py::module& m);
    void bind_OOK_Modulator_cplus(py::module& m);
    void bind_OOK_Demodulator_cplus(py::module& m);
    void bind_OOK_Demodulator_cpvolk(py::module& m);
    void bind_OWC_Channel_absolute_cplus(py::module& m);
    void bind_OWC_Channel_absolute_cvolk(py::module& m);
    void bind_PAM_Modulator_cplus(py::module& m);
    void bind_VPPM_Modulator_cplus(py::module& m);
    void bind_PPM_Modulator_cplus(py::module& m);
    void bind_LED_Nonlinearity(py::module& m);
    void bind_Hermitian_Symmetry_i_o_same_vec_size_cplus(py::module& m);
    void bind_Hermitian_Symmetry_i_o_same_vec_size_cpvolk(py::module& m);
    void bind_PAM_Demodulator_cplus(py::module& m);
// ) END BINDING_FUNCTION_PROTOTYPES


// We need this hack because import_array() returns NULL
// for newer Python versions.
// This function is also necessary because it ensures access to the C API
// and removes a warning.
void* init_numpy()
{
    import_array();
    return NULL;
}

PYBIND11_MODULE(owc_python, m)
{
    // Initialize the numpy C API
    // (otherwise we will see segmentation faults)
    init_numpy();

    // Allow access to base block methods
    py::module::import("gnuradio.gr");

    /**************************************/
    // The following comment block is used for
    // gr_modtool to insert binding function calls
    // Please do not delete
    /**************************************/
    // BINDING_FUNCTION_CALLS(
    bind_OWC_Channel_relative_cplus(m);
    bind_OWC_Channel_relative_cpvolk(m);
    bind_OOK_Modulator_cplus(m);
    bind_OOK_Demodulator_cplus(m);
    bind_OOK_Demodulator_cpvolk(m);
    bind_OWC_Channel_absolute_cplus(m);
    bind_OWC_Channel_absolute_cvolk(m);
    bind_PAM_Modulator_cplus(m);
    bind_VPPM_Modulator_cplus(m);
    bind_PPM_Modulator_cplus(m);
    bind_LED_Nonlinearity(m);
    bind_Hermitian_Symmetry_i_o_same_vec_size_cplus(m);
    bind_Hermitian_Symmetry_i_o_same_vec_size_cpvolk(m);
    bind_PAM_Demodulator_cplus(m);
    // ) END BINDING_FUNCTION_CALLS
}