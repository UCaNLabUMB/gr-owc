#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr

class OOK_Demodulator_Python(gr.decim_block):
    """
    docstring for block OOK_Demodulator_Python
    """
    def __init__(self, threshold = 0.5, samples_per_symbol = 1):
        gr.decim_block.__init__(self,
            name="OOK_Demodulator_Python",
            in_sig=[np.float32 ],
            out_sig=[np.float32 ], decim=samples_per_symbol)
        self.threshold = threshold
        self.samples_per_symbol = samples_per_symbol


    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_threshold(self):
        return self.threshold

    def set_samples_per_symbol(self, samples_per_symbol):
        self.samples_per_symbol = samples_per_symbol

    def get_samples_per_symbol(self):
        return self.samples_per_symbol

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        
        i = 0
        j = 0
        d_samples_per_symbol = self.get_samples_per_symbol()

        while i < len(out):
            samples_array = in0[j:j + d_samples_per_symbol]
            average_val = np.mean(samples_array)

            if average_val > self.threshold:
                out[i] = 1.0
            else:
                out[i] = 0.0

            i += 1
            j += d_samples_per_symbol

        return len(output_items[0])

    
