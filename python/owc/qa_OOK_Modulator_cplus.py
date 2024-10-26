#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking (UCAN) Lab, University of Massachusetts, Boston.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
try:
    from gnuradio.owc import OOK_Modulator_cplus
except ImportError:
    import os
    import sys
    dirname, filename = os.path.split(os.path.abspath(__file__))
    sys.path.append(os.path.join(dirname, "bindings"))
    from gnuradio.owc import OOK_Modulator_cplus

class qa_OOK_Modulator_cplus(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_instance(self):
        instance = OOK_Modulator_cplus(2,1,2)

    def test_001_OOK(self):
        src_data = (0,1,0,1,0)
        expected_result = (1,1,2,2,1,1,2,2,1,1)
        
        src = blocks.vector_source_f(src_data)      
        blk = OOK_Modulator_cplus(2,1,2)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def test_002_OOK(self):
        src_data = (0,1,0,1,1)
        expected_result = (1,1,1,2,2,2,1,1,1,2,2,2,2,2,2)
        
        src = blocks.vector_source_f(src_data)      
        blk = OOK_Modulator_cplus(2,1,3)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def test_003_OOK(self):
        src_data = (0,1,1,1,1,0,0)
        expected_result = (0.5,1.5,1.5,1.5,1.5,0.5,0.5)
        
        src = blocks.vector_source_f(src_data)      
        blk = OOK_Modulator_cplus(1.5,0.5,1)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)


if __name__ == '__main__':
    gr_unittest.run(qa_OOK_Modulator_cplus)
