#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
try:
    from gnuradio.owc import OOK_Demodulator_cpvolk
except ImportError:
    import os
    import sys
    dirname, filename = os.path.split(os.path.abspath(__file__))
    sys.path.append(os.path.join(dirname, "bindings"))
    from gnuradio.owc import OOK_Demodulator_cpvolk

class qa_OOK_Demodulator_cpvolk(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_instance(self):
        instance = OOK_Demodulator_cpvolk(0.5, 1)

    def test_001_OOK_Demod(self):
        src_data = (8,8,8,0,0,0)
        expected_result = (1,0)

        src = blocks.vector_source_f(src_data)
        blk = OOK_Demodulator_cpvolk(4,3)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)
        
    def test_002_OOK_Demod(self):
        src_data = (2,2,1.5,1.5,2,2)
        expected_result = (1,0,1)

        src = blocks.vector_source_f(src_data)
        blk = OOK_Demodulator_cpvolk(1.75,2)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)
        
    def test_003_OOK_Demod(self):
        src_data = (20,20,20,20,10,10,10,10)
        expected_result = (1,0)

        src = blocks.vector_source_f(src_data)
        blk = OOK_Demodulator_cpvolk(15,4)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def test_004_OOK_Demod(self):
        src_data = (10, 15, 45, 55, 0, 49, 49, 49, 49, 100)
        expected_result = (0, 1)

        src = blocks.vector_source_f(src_data)
        blk = OOK_Demodulator_cpvolk(50,5)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def test_005_OOK_Demod(self):
        src_data = (0.4999, 0.4999, 0.4999, 0.4999, 0.50001, 0.50001, 0.50001, 0.50001)
        expected_result = (0, 1)

        src = blocks.vector_source_f(src_data)
        blk = OOK_Demodulator_cpvolk(0.5,4)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def test_006_OOK_Demod(self):
        src_data = (0, 0, 0, 0, 0, 0, 0, 1.5, 1, 1, 1, 1, 1, 1, 1, 1)
        expected_result = (0, 0, 0, 1, 1, 1, 1, 1)

        src = blocks.vector_source_f(src_data)
        blk = OOK_Demodulator_cpvolk(0.5,2)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)


if __name__ == '__main__':
    gr_unittest.run(qa_OOK_Demodulator_cpvolk)
