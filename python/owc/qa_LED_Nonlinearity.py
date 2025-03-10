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
try:
    from gnuradio.owc import LED_Nonlinearity
except ImportError:
    import os
    import sys
    dirname, filename = os.path.split(os.path.abspath(__file__))
    sys.path.append(os.path.join(dirname, "bindings"))
    from gnuradio.owc import LED_Nonlinearity

class qa_LED_Nonlinearity(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_instance(self):
        instance = LED_Nonlinearity(1, 1, 0)

    def test_001_LED_NL(self):
        src_data = (-2.0,-1.0,0.0,1.0,2.0,3.0)
        expected_result = (1.19,2.69,5.00,7.31,8.81,9.52)

        src = blocks.vector_source_f(src_data)
        blk = LED_Nonlinearity(10,1.0,0)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        print ("Source: ")
        print (str(src_data).strip('[]'))
        print ("Results")
        print (str(result_data).strip('[]'))
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 1)

    def test_002_LED_NL(self):
        src_data = (-1000,-10,0,10,1000)
        expected_result = (0.0,0.0067,0.5,0.9933,1.0)

        src = blocks.vector_source_f(src_data)
        blk = LED_Nonlinearity(1,0.5,0)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 1)

    def test_003_LED_NL(self):
        src_data = (-0.5,-0.2,0.0,0.2,0.5)
        expected_result = (0.033,0.59,2.50,4.42,4.97)

        src = blocks.vector_source_f(src_data)
        blk = LED_Nonlinearity(5,10,0)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 1)

    def test_004_LED_NL(self):
        src_data = (0,1,2,3,4)
        expected_result = (1.19,2.69,5.00,7.31,8.81)

        src = blocks.vector_source_f(src_data)
        blk = LED_Nonlinearity(10,1,2)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 1)

    def test_005_LED_NL(self):
        src_data = (-10,-5,0,5,10)
        expected_result = (2.69,3.78,5,6.25,7.35)

        src = blocks.vector_source_f(src_data)
        blk = LED_Nonlinearity(10,0.1,0)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 1)

    def test_006_LED_NL(self):
        src_data = (-10,-5,0,5,10)
        expected_result = (0,0,0,0,0)

        src = blocks.vector_source_f(src_data)
        blk = LED_Nonlinearity(0.0,1,0.0)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 1)


if __name__ == '__main__':
    gr_unittest.run(qa_LED_Nonlinearity)
