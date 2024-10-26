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
    from gnuradio.owc import OWC_Channel_relative_cplus
except ImportError:
    import os
    import sys
    dirname, filename = os.path.split(os.path.abspath(__file__))
    sys.path.append(os.path.join(dirname, "bindings"))
    from gnuradio.owc import OWC_Channel_relative_cplus

class qa_OWC_Channel_relative_cplus(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_instance(self):
        instance = OWC_Channel_relative_cplus(1,1,[1],[1],[1],[1],[1],[1],[1],[90],[1],[1])

    def test_001_channel_module(self):
        src_data = (1.0,2.0,3.0,4.0,5.0)
        expected_result = (0.3182,2*0.3182,3*0.3182,4*0.3182,5*0.3182)
        
        src = blocks.vector_source_f(src_data)      
        res = OWC_Channel_relative_cplus(1, 1,[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[1.0],[90],[1.0],[1.0])
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, res)
        self.tb.connect(res, dst)
        self.tb.run()
        
        result_data = dst.data()
        

        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 3)

    def test_002_channel_module(self):
        src_data = (1.0,2.0,3.0,4.0,5.0)
        expected_result = (20*0.0064,20*2*0.0064,20*3*0.0064,20*4*0.0064,20*5*0.0064)
        
        src = blocks.vector_source_f(src_data)      
        blk = OWC_Channel_relative_cplus(1,1,[45],[45],[5],[1],[1],[1],[1],[90],[5],[4])
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 2)

        
    def help3_ff(self, src_data, exp_data, op):
        for s in zip(list(range(len(src_data))), src_data):
            src = blocks.vector_source_f(s[1])
            self.tb.connect(src, (op, s[0]))
                        
        dst1 = blocks.vector_sink_f()
        dst2 = blocks.vector_sink_f()
        self.tb.connect((op,0), dst1)
        self.tb.connect((op,1), dst2)
        self.tb.run()
        
        exp_data1 = exp_data[0]
        exp_data2 = exp_data[1]
        
        result_data1 = dst1.data()
        self.assertFloatTuplesAlmostEqual(exp_data1, result_data1, 3)

        result_data2 = dst2.data()
        self.assertFloatTuplesAlmostEqual(exp_data2, result_data2, 3)

    def test_003_channel_module(self):
        src1_data = (1.0,  2.0, 3.0, 4.0, 5.0)
        src2_data = (1.0, 2.0, 3.0, 4.0, 5.0)
        expected_result1 = ((1*(0.0841))+(1*(0.0192)),(2*(0.0841))+(2*(0.0192)),(3*(0.0841))+(3*(0.0192)),(4*(0.0841))+(4*(0.0192)),(5*(0.0841))+(5*(0.0192)))
        expected_result2 = ((1*(0.0075))+(1*(0.0001533)),(2*(0.0075))+(2*(0.0001533)),(3*(0.0075))+(3*(0.0001533)),(4*(0.0075))+(4*(0.0001533)),(5*(0.0075))+(5*(0.0001533)))
        op = OWC_Channel_relative_cplus(2,2,[30,45,60,75],[20,40,60,80],[2,3,4,5],[2,3],[1,2],[1,1],[1,1],[90,90],[1,1],[1,1])
        self.help3_ff((src1_data, src2_data), (expected_result1, expected_result2), op)
        
        
    def test_004_channel_module(self):
        src_data = (1.0,2.0,3.0,4.0,5.0)
        expected_result = (0,0,0,0,0)
        
        src = blocks.vector_source_f(src_data)      
        blk = OWC_Channel_relative_cplus(1,1,[45],[45],[5],[1],[1],[1],[1],[40],[5],[4])
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 2)

    def test_005_channel_module(self):
        src_data = (1.0,2.0,3.0,4.0,5.0)
        expected_result = (0,0,0,0,0)
        
        src = blocks.vector_source_f(src_data)      
        blk = OWC_Channel_relative_cplus(1,1,[95],[35],[5],[1],[1],[1],[1],[40],[5],[4])
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 2)

    def test_006_channel_module(self):
        src_data = (1.0,2.0,3.0,4.0,5.0)
        #expected_result = (20*0.0064,20*2*0.0064,20*3*0.0064,20*4*0.0064,20*5*0.0064)
        expected_result1 = (0, 0, 0, 0, 0)
        
        src = blocks.vector_source_f(src_data)      
        blk = OWC_Channel_relative_cplus(1,1,[45],[45],[5],[1],[1],[1],[1],[90],[5],[4])
        blk.set_emission_angle_array([95])
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result1, result_data, 2)

    def test_006_channel_module(self):
        src_data = (1.0,2.0,3.0,4.0,5.0)
        expected_result = (20*0.0064,20*2*0.0064,20*3*0.0064,20*4*0.0064,20*5*0.0064)
        
        src = blocks.vector_source_f(src_data)      
        blk = OWC_Channel_relative_cplus(1,1,[-45],[45],[5],[1],[1],[1],[1],[90],[5],[4])
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 2)

    def test_007_channel_module(self):
        src_data = (1.0,2.0,3.0,4.0,5.0)
        expected_result = (0, 0, 0, 0, 0)
        
        src = blocks.vector_source_f(src_data)      
        blk = OWC_Channel_relative_cplus(1,1,[-45],[45],[5],[1],[1],[1],[1],[90],[5],[4])
        blk.set_acceptance_angle_array([-95])
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()
        
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 2)


if __name__ == '__main__':
    gr_unittest.run(qa_OWC_Channel_relative_cplus)