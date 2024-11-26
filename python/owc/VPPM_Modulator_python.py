#!/usr/bin/env python
# -*- coding: utf-8 -*-
# gr-owc OOT module for optical wireless communications.
# gr-owc is compatible with GNU Radio v3.10
#
# Copyright 2024 Kunal Sangurmath from Ubiquitous Communications and Networking (UCAN) Lab, University of Massachusetts, Boston.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#
#


import numpy as np
from gnuradio import gr

class VPPM_Modulator_python(gr.interp_block):
    """
    docstring for block VPPM_Modulator_python
    """
    def __init__(self, max_mag = 1, min_mag = 0, samples_per_symbol = 2, samples_per_pulse = 1):
        gr.interp_block.__init__(self,
            name="VPPM_Modulator_python",
            in_sig=[np.float32],
            out_sig=[np.float32], interp=samples_per_symbol)
        self.max_mag = max_mag
        self.min_mag = min_mag
        self.samples_per_symbol = samples_per_symbol
        self.samples_per_pulse = samples_per_pulse


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        i = 0
        z = 0

        while i < len(out):
            for j in range(self.samples_per_symbol):
                if in0[z] == 0:
                    if j < self.samples_per_pulse:
                        out[i] = self.max_mag
                    else:
                        out[i] = self.min_mag
                else:
                    if j >= self.samples_per_symbol - self.samples_per_pulse:
                        out[i] = self.max_mag
                    else:
                        out[i] = self.min_mag
                i += 1
            z += 1

        return len(output_items[0])

    def set_max_magnitude(self, max_mag):
        self.max_mag = max_mag

    def get_max_magnitude(self):
        return self.max_mag

    def set_min_magnitude(self, min_mag):
        self.min_mag = min_mag

    def get_min_magnitude(self):
        return self.min_mag

    def set_samples_per_symbol(self, samples_per_symbol):
        self.samples_per_symbol = samples_per_symbol

    def get_samples_per_symbol(self):
        return self.samples_per_symbol

    def set_samples_per_pulse(self, samples_per_pulse):
        self.samples_per_pulse = samples_per_pulse

    def get_samples_per_pulse(self):
        return self.samples_per_pulse
