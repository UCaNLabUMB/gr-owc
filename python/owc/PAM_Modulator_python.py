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

class PAM_Modulator_python(gr.interp_block):
    """
    docstring for block PAM_Modulator_python
    """
    def __init__(self, modulation_order = 2, max_magnitude = 1, min_magnitude = 0, samples_per_symbol = 1):
        gr.interp_block.__init__(self,
            name="PAM_Modulator_python",
            in_sig=[np.float32],
            out_sig=[np.float32], interp=samples_per_symbol)
        self.modulation_order = modulation_order
        self.max_magnitude = max_magnitude
        self.min_magnitude = min_magnitude
        self.samples_per_symbol = samples_per_symbol

        self.d_symbol_array = []
        self.d_level_array = []

        self.set_symbol_array()
        self.set_level_array()


    def set_symbol_array(self):
        num_bits = int(np.floor(np.log2(self.modulation_order)))
        max_symbol = int(2**num_bits)
        self.d_symbol_array = [i for i in range(max_symbol)]

    def set_level_array(self):
        self.d_level_array = []
        num_bits = int(np.floor(np.log2(self.modulation_order)))
        max_symbol = int(2**num_bits)
        value_range = self.max_magnitude - self.min_magnitude
        single_level_magnitude = value_range / (self.modulation_order - 1)
        level = self.min_magnitude
        for _ in range(max_symbol):
            self.d_level_array.append(level)
            level += single_level_magnitude

    def symbol_array(self):
        return self.d_symbol_array

    def level_array(self):
        return self.d_level_array

    def set_modulation_order(self, modulation_order):
        self.modulation_order = modulation_order

    def get_modulation_order(self):
        return self.modulation_order

    def set_max_magnitude(self, max_magnitude):
        self.max_magnitude = max_magnitude

    def get_max_magnitude(self):
        return self.max_magnitude

    def set_min_magnitude(self, min_magnitude):
        self.min_magnitude = min_magnitude
        self.set_level_array()

    def get_min_magnitude(self):
        return self.min_magnitude

    def set_samples_per_symbol(self, samples_per_symbol):
        self.samples_per_symbol = samples_per_symbol

    def get_samples_per_symbol(self):
        return self.samples_per_symbol

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        log_2_M = int(np.floor(np.log2(self.modulation_order)))
        max_symbol = int(2**log_2_M)
        symbol_index = 0

        i = 0
        z = 0

        self.set_level_array()

        while i < len(out):
            decimal = int(in0[z])
            
            for j in range(self.samples_per_symbol):
                for m in range(max_symbol):
                    if decimal == self.d_symbol_array[m]:
                        symbol_index = m
                        break
                out[i] = self.d_level_array[symbol_index]
                i += 1

            z += 1
            symbol_index = 0

        return len(output_items[0])
