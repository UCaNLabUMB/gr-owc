#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr

class OOK_Modulator_Python(gr.interp_block):
    """
    docstring for block OOK_Modulator_Python
    """
    def __init__(self, max_mag = 1.0, min_mag = 0.0, samples_per_symbol = 1):
        gr.interp_block.__init__(self,
            name="OOK_Modulator_Python",
            in_sig=[np.float32],
            out_sig=[np.float32], interp=samples_per_symbol)
        self.max_mag = max_mag
        self.min_mag = min_mag
        self.samples_per_symbol = samples_per_symbol


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        i = 0
        z = 0

        while i < len(out):
            for j in range(self.get_samples_per_symbol()):
                if in0[z] == 0:
                    out[i] = self.get_min_magnitude()
                else:
                    out[i] = self.get_max_magnitude()
                i+=1
            z+=1

        return len(output_items[0])

    def set_min_magnitude(self, min_mag):
        self.min_mag = min_mag

    def get_min_magnitude(self):
        return self.min_mag

    def set_max_magnitude(self, max_mag):
        self.max_mag = max_mag
        
    def get_max_magnitude(self):
        return self.max_mag

    def set_samples_per_symbol(self, samples_per_symbol):
        self.samples_per_symbol = samples_per_symbol
        
    def get_samples_per_symbol(self):
       return self.samples_per_symbol
