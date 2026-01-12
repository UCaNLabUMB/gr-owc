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

class PPM_Demodulator_python(gr.decim_block):
    """
    docstring for block PPM_Demodulator_python
    """
    def __init__(self, samples_per_symbol = 2.0, samples_per_pulse = 1.0, modulation_order = 2):
        gr.decim_block.__init__(self,
            name="PPM_Demodulator_python",
            in_sig=[np.float32],
            out_sig=[np.float32],
            decim=samples_per_symbol)

        self.d_samples_per_symbol = samples_per_symbol
        self.d_samples_per_pulse = samples_per_pulse
        self.d_modulation_order = modulation_order

        self.cases = []

        self.set_samples_per_symbol(samples_per_symbol)
        self.set_samples_per_pulse(samples_per_pulse)
        self.set_modulation_order(modulation_order)
        self.initialize_vector_PPM()

    def set_samples_per_symbol(self, samples_per_symbol):
        self.d_samples_per_symbol = samples_per_symbol

    def samples_per_symbol(self):
        return self.d_samples_per_symbol

    def set_samples_per_pulse(self, samples_per_pulse):
        self.d_samples_per_pulse = samples_per_pulse

    def samples_per_pulse(self):
        return self.d_samples_per_pulse

    def set_modulation_order(self, modulation_order):
        self.d_modulation_order = modulation_order

    def modulation_order(self):
        return self.d_modulation_order

    def initialize_vector_PPM(self):
        slot = int(self.samples_per_symbol() / self.modulation_order())

        self.cases = []
        for _ in range(int(self.modulation_order())):
            self.cases.append([0.0] * int(self.samples_per_symbol()))

        for k in range(int(self.modulation_order())):
            start = k * slot

            for n in range(int(self.samples_per_pulse())):
                i = start + n
                if i < int(self.samples_per_symbol()):
                    self.cases[k][i] = 1.0

    def matched_filter_ppm(self, samples_array):
        best_k = -1
        best_metric = -np.inf

        for k in range(int(self.modulation_order())):
            metric = 0.0
            for x in range(int(self.samples_per_symbol())):
                metric += samples_array[x] * self.cases[k][x]

            if metric > best_metric:
                best_metric = metric
                best_k = k

        return float(best_k)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        i = 0
        j = 0

        d_incoming_samples_array = []

        while i < len(out):

            for k in range(int(self.samples_per_symbol())):
                d_incoming_samples_array.append(in0[j + k])

            out[i] = self.matched_filter_ppm(d_incoming_samples_array)
            i += 1

            j += int(self.samples_per_symbol())
            d_incoming_samples_array = []


        return len(output_items[0])
