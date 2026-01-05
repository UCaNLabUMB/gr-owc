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

class PAM_Demodulator_python(gr.decim_block):
    """
    docstring for block PAM_Demodulator_python
    """
    def __init__(self, modulation_order = 2.0, max_magnitude = 1.0, min_magnitude = 0.0, samples_per_symbol = 1):
        gr.decim_block.__init__(self,
            name="PAM_Demodulator_python",
            in_sig=[np.float32],
            out_sig=[np.float32], decim=samples_per_symbol)
        self.d_modulation_order = modulation_order
        self.d_max_magnitude = max_magnitude
        self.d_min_magnitude = min_magnitude
        self.d_samples_per_symbol = samples_per_symbol

        self.d_symbol_array = []
        self.d_level_array = []

        self.set_symbol_array()
        self.set_level_array()

    def set_modulation_order(self, modulation_order):
        self.d_modulation_order = modulation_order

    def modulation_order(self):
        return self.d_modulation_order

    def set_max_magnitude(self, max_magnitude):
        self.d_max_magnitude = max_magnitude

    def max_magnitude(self):
        return self.d_max_magnitude

    def set_min_magnitude(self, min_magnitude):
        self.d_min_magnitude = min_magnitude

    def min_magnitude(self):
        return self.d_min_magnitude

    def set_samples_per_symbol(self, samples_per_symbol):
        self.d_samples_per_symbol = samples_per_symbol

    def samples_per_symbol(self):
        return self.d_samples_per_symbol

    def set_symbol_array(self):
        num_bits = int(np.floor(np.log2(self.d_modulation_order)))
        max_symbol = int(2**num_bits)
        self.d_symbol_array = [i for i in range(max_symbol)]

    def symbol_array(self):
        return self.d_symbol_array

    def set_level_array(self):
        self.d_level_array = []
        num_bits = int(np.floor(np.log2(self.d_modulation_order)))
        max_symbol = int(2**num_bits)
        value_range = self.d_max_magnitude - self.d_min_magnitude
        single_level_magnitude = value_range / (self.d_modulation_order - 1)
        level = self.d_min_magnitude
        for _ in range(max_symbol):
            self.d_level_array.append(level)
            level += single_level_magnitude

    def level_array(self):
        return self.d_level_array

    def samples_average_value(self, samples_array, num_incoming_samples):
        s = 0.0
        for i in range(num_incoming_samples):
            s += float(samples_array[i])
        return s / float(num_incoming_samples)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        i = 0
        j = 0

        d_incoming_samples_array = []

        num_incoming_samples = self.samples_per_symbol()

        symbol_level = 0

        while i < len(out):
            for k in range(num_incoming_samples):
                d_incoming_samples_array.append(float(in0[j + k]))

            average_value = self.samples_average_value(d_incoming_samples_array, num_incoming_samples)

            for x in range(self.modulation_order()):
                difference = average_value - self.level_array()[x]
                if abs(difference) < 0.000001:
                    symbol_level = x
                    break

            out[i] = float(self.symbol_array()[symbol_level])
            i += 1

            j += num_incoming_samples
            d_incoming_samples_array = []

        return len(output_items[0])
