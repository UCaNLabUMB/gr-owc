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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from gnuradio.owc import PPM_Demodulator_python

class qa_PPM_Demodulator_python(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_instance(self):
        instance = PPM_Demodulator_python(2, 1, 2)

    def test_001_PPM_Demod(self):
        expected_result = (0, 3, 1, 2)
        src_data = (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0)
        
        src = blocks.vector_source_f(src_data)      
        blk = PPM_Demodulator_python(8, 2, 4)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def test_002_PPM_Demod(self):
        expected_result = (0, 3, 1, 2)
        src_data = (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0)
        
        src = blocks.vector_source_f(src_data)      
        blk = PPM_Demodulator_python(8, 1, 4)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def test_003_PPM_Demod(self):
        expected_result = (0, 1)
        src_data = (5, 5, -3, -3, -3, -3, 5, 5)
        
        src = blocks.vector_source_f(src_data)      
        blk = PPM_Demodulator_python(4, 2, 2)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def test_004_PPM_Demod(self):
        expected_result = (0, 1, 2, 3, 4, 5)
        src_data = (15, -10, -10, -10, -10, -10, -10, 15, -10, -10, -10, -10, -10, -10, 15, -10, -10, -10, -10, -10, -10, 15, -10, -10, -10, -10, -10, -10, 15, -10, -10, -10, -10, -10, -10, 15)
        
        src = blocks.vector_source_f(src_data)      
        blk = PPM_Demodulator_python(6, 1, 6)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)


if __name__ == '__main__':
    gr_unittest.run(qa_PPM_Demodulator_python)
