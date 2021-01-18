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

class qa_OWC_Channel_absolute(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001_t(self):
    	src_data = (1.0,2.0,3.0,4.0,5.0)
    	expected_result = (0.0173,2*0.0173,3*0.0173,4*0.0173,5*0.0173)
    	
    	src = blocks.vector_source_f(src_data)   	
    	blk = owc.OWC_Channel_absolute(1,1,[1,2,5],[0,0,-1],[2,2,0],[0,0,1],[2],[1],[1],[1],[90],[1],[1])
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
    	expected_result = (0.0017,2*0.0017,3*0.0017,4*0.0017,5*0.0017)
    	
    	src = blocks.vector_source_f(src_data)   	
    	blk = owc.OWC_Channel_absolute(1,1,[10,10,10],[-1,0,-1],[4,4,4],[0,0,1],[2],[1],[1],[1],[90],[1],[1])
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
        
        result_data1 = dst1.data()
        self.assertFloatTuplesAlmostEqual(exp_data1, result_data1, 3)

        result_data2 = dst2.data()
        self.assertFloatTuplesAlmostEqual(exp_data2, result_data2, 3)

    def test_003_t(self):
        src1_data = (1.0,  2.0, 3.0, 4.0, 5.0)
        src2_data = (1.0, 2.0, 3.0, 4.0, 5.0)
        expected_result1 = ((1*(0.00047858))+(1*(0.0019)),(2*(0.00047858))+(2*(0.0019)),(3*(0.00047858))+(3*(0.0019)),(4*(0.00047858))+(4*(0.0019)),(5*(0.00047858))+(5*(0.0019)))
        expected_result2 = ((1*(0.0020))+(1*(0.0079)),(2*(0.0020))+(2*(0.0079)),(3*(0.0020))+(3*(0.0079)),(4*(0.0020))+(4*(0.0079)),(5*(0.0020))+(5*(0.0079)))
        
        op = owc.OWC_Channel_absolute(2,2,[10,10,10,8,8,8],[0,0,-1,0,-1,-1],[2,2,2,3,4,4],[0,0,1,1,0,1],[2,3],[1,2],[1,1],[1,1],[90,90],[1,1],[1,1])
        self.help3_ff((src1_data, src2_data), (expected_result1, expected_result2), op)


if __name__ == '__main__':
    gr_unittest.run(qa_OWC_Channel_absolute)
