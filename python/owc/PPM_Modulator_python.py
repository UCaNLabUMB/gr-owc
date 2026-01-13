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

class PPM_Modulator_python(gr.interp_block):
    """
    docstring for block PPM_Modulator_python
    """
    def __init__(self, max_mag = 1, min_mag = 0, samples_per_symbol = 2, samples_per_pulse = 1, modulation_order = 2):
        gr.interp_block.__init__(self,
            name="PPM_Modulator_python",
            in_sig=[np.float32],
            out_sig=[np.float32], interp=samples_per_symbol)
        self.max_magnitude = max_mag
        self.min_magnitude = min_mag
        self.samples_per_symbol = samples_per_symbol
        self.samples_per_pulse = samples_per_pulse
        self.modulation_order = modulation_order


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        i = 0
        z = 0

        while i < len(out):
            decimal = int(in0[z])

            if decimal < 0 or decimal >= self.get_modulation_order():
                decimal = 0;

            for j in range(self.get_samples_per_symbol()):
                out[i + j] = self.get_min_magnitude()

            pulse = decimal * (self.get_samples_per_symbol() // self.get_modulation_order())

            for j in range(self.get_samples_per_pulse()):
                if pulse + j < self.get_samples_per_symbol():
                    out[i + pulse + j] = self.get_max_magnitude()    

            i += self.get_samples_per_symbol()
            z += 1

        return len(output_items[0])

    def set_max_magnitude(self, max_mag):
        self.max_magnitude = max_mag

    def get_max_magnitude(self):
        return self.max_magnitude

    def set_min_magnitude(self, min_mag):
        self.min_magnitude = min_mag

    def get_min_magnitude(self):
        return self.min_magnitude

    def set_samples_per_symbol(self, samples_per_symbol):
        self.samples_per_symbol = samples_per_symbol

    def get_samples_per_symbol(self):
        return self.samples_per_symbol

    def set_samples_per_pulse(self, samples_per_pulse):
        self.samples_per_pulse = samples_per_pulse

    def get_samples_per_pulse(self):
        return self.samples_per_pulse

    def set_modulation_order(self, modulation_order):
        self.modulation_order = modulation_order

    def get_modulation_order(self):
        return self.modulation_order
