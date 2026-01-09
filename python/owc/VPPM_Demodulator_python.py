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

class VPPM_Demodulator_python(gr.decim_block):
    """
    docstring for block VPPM_Demodulator_python
    """
    def __init__(self, samples_per_symbol = 2.0, samples_per_pulse = 1.0):
        gr.decim_block.__init__(self,
            name="VPPM_Demodulator_python",
            in_sig=[np.float32],
            out_sig=[np.float32], decim=samples_per_symbol)

        self.d_samples_per_symbol = samples_per_symbol
        self.d_samples_per_pulse = samples_per_pulse

        self.case1 = []
        self.case0 = []

        self.set_samples_per_symbol(samples_per_symbol)
        self.set_samples_per_pulse(samples_per_pulse)
        self.initialize_vector()

    def set_samples_per_symbol(self, samples_per_symbol):
        self.d_samples_per_symbol = samples_per_symbol

    def samples_per_symbol(self):
        return self.d_samples_per_symbol

    def set_samples_per_pulse(self, samples_per_pulse):
        self.d_samples_per_pulse = samples_per_pulse

    def samples_per_pulse(self):
        return self.d_samples_per_pulse

    def initialize_vector(self):
        symbol_len = self.samples_per_symbol()
        pulse_len = self.samples_per_pulse()
        rest_len = symbol_len - pulse_len

        self.case0 = [0.0] * symbol_len
        self.case1 = [0.0] * symbol_len

        for j in range(symbol_len):
            if j < pulse_len:
                self.case0[j] = 1.0
            else:
                self.case0[j] = 0.0

            if j < rest_len:
                self.case1[j] = 0.0
            else:
                self.case1[j] = 1.0

    def matched_filter(self, samples_array):
        v1 = 0.0
        v0 = 0.0

        for x in range(self.samples_per_symbol()):
            v1 += samples_array[x] * self.case1[x]
            v0 += samples_array[x] * self.case0[x]

        return 1.0 if (v1 > v0) else 0.0


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        i = 0
        j = 0

        d_incoming_samples_array = []

        while i < len(out):
            for k in range(self.samples_per_symbol()):
                d_incoming_samples_array.append(in0[j + k])

            out[i] = self.matched_filter(d_incoming_samples_array)
            i += 1

            j += self.samples_per_symbol()
            d_incoming_samples_array = []


        return len(output_items[0])
