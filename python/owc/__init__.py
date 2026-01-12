#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

# The presence of this file turns this directory into a Python package

'''
This is the GNU Radio OWC module. Place your Python package
description here (python/__init__.py).
'''
import os

# import pybind11 generated symbols into the owc namespace
try:
    # this might fail if the module is python-only
    from .owc_python import *
except ModuleNotFoundError:
    pass

# import any pure python here
from .OWC_Channel_relative_python import OWC_Channel_relative_python
from .OOK_Modulator_Python import OOK_Modulator_Python
from .OOK_Demodulator_Python import OOK_Demodulator_Python
from .OWC_Channel_absolute_python import OWC_Channel_absolute_python
from .PAM_Modulator_python import PAM_Modulator_python
from .VPPM_Modulator_python import VPPM_Modulator_python
from .PPM_Modulator_python import PPM_Modulator_python
from .PAM_Demodulator_python import PAM_Demodulator_python
from .VPPM_Demodulator_python import VPPM_Demodulator_python
from .PPM_Demodulator_python import PPM_Demodulator_python

#
