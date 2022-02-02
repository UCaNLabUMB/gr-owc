#!/usr/bin/env python
# -*- coding: utf-8 -*-
# gr-owc OOT module for optical wireless communications. 
#
# Copyright 2021 Arsalan Ahmed from The Ubiquitous Communications and Networking (UCAN) Lab, University of Massachusetts, Boston.
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
import owc_swig as owc

class qa_OWC_Channel_relative_two(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001_t(self):
    	src_data = (1.0,2.0,3.0,4.0,5.0)
    	expected_result = (0, 0, 0.3182, 2*0.3182, 3*0.3182)
    	
    	src = blocks.vector_source_f(src_data)   	
    	blk = owc.OWC_Channel_relative_two(1,1,[1],[1],[1],[1],[1],[1],[1],[90],[1],[1],500000000,[1],[0])
    	dst = blocks.vector_sink_f()
    	
    	self.tb.connect(src, blk)
    	self.tb.connect(blk, dst)
    	self.tb.run()
    	
    	result_data = dst.data()
    	
    	print ("Source: ")
    	print (str(src_data).strip('[]'))
    	print ("Results")
    	print (str(result_data).strip('[]'))
    	self.assertFloatTuplesAlmostEqual(expected_result, result_data, 3)
    	
    def test_002_t(self):
    	src_data = (1.0,2.0,3.0,4.0,5.0)
    	expected_result = (0, 0.3182, 2*0.3182, 3*0.3182, 4*0.3182)
    	
    	src = blocks.vector_source_f(src_data)   	
    	blk = owc.OWC_Channel_relative_two(1,1,[1],[1],[1],[1],[1],[1],[1],[90],[1],[1],200000000,[1],[0])
    	dst = blocks.vector_sink_f()
    	
    	self.tb.connect(src, blk)
    	self.tb.connect(blk, dst)
    	self.tb.run()
    	
    	result_data = dst.data()
    	
    	print ("Source: ")
    	print (str(src_data).strip('[]'))
    	print ("Results")
    	print (str(result_data).strip('[]'))
    	self.assertFloatTuplesAlmostEqual(expected_result, result_data, 3)
    	
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
        
        print ("Result1")
        print (str(dst1.data()).strip('[]'))
        
        print ("Result2")
        print (str(dst2.data()).strip('[]'))
        
        result_data1 = dst1.data()
        self.assertFloatTuplesAlmostEqual(exp_data1, result_data1, 3)

        result_data2 = dst2.data()
        self.assertFloatTuplesAlmostEqual(exp_data2, result_data2, 3)


    def test_003_t(self):
        src1_data = (1.0,  2.0, 3.0, 4.0, 5.0)
        src2_data = (1.0, 2.0, 3.0, 4.0, 5.0)
        
        expected_result1 = (0,0,0,(1*(0.0841*0))+(1*(0.0192)),(2*(0.0841*0))+(2*(0.0192)))
        
        expected_result2 = (0,0,0,0,(1*(0.0075))+(1*(0.0001533*0)))
        
        op = owc.OWC_Channel_relative_two(2,2,[30,45,60,75],[20,40,60,80],[2,3,4,5],[2,3],[1,2],[1,1],[1,1],[90,90],[1,1],[1,1],300000000,[0,1,1,0],[0,0])
        
        self.help3_ff((src1_data, src2_data), (expected_result1, expected_result2), op)


if __name__ == '__main__':
    gr_unittest.run(qa_OWC_Channel_relative_two)
