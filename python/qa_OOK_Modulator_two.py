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

class qa_OOK_Modulator_two(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001_t(self):
    	src_data = (0,1,0,1,0)
    	expected_result = (-1,-1,3,3,-1,-1,3,3,-1,-1)
    	
    	src = blocks.vector_source_f(src_data)   	
    	blk = owc.OOK_Modulator_two(2,1,2)
    	dst = blocks.vector_sink_f()
    	
    	self.tb.connect(src, blk)
    	self.tb.connect(blk, dst)
    	self.tb.run()
    	
    	result_data = dst.data()
    	
    	print ("Source: ")
    	print (str(src_data).strip('[]'))
    	print ("Results")
    	print (str(result_data).strip('[]'))
    	self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def test_002_t(self):
    	src_data = (0,1,0,1,1)
    	expected_result = (0,0,0,10,10,10,0,0,0,10,10,10,10,10,10)
    	
    	src = blocks.vector_source_f(src_data)   	
    	blk = owc.OOK_Modulator_two(5,5,3)
    	dst = blocks.vector_sink_f()
    	
    	self.tb.connect(src, blk)
    	self.tb.connect(blk, dst)
    	self.tb.run()
    	
    	result_data = dst.data()
    	
    	print ("Source: ")
    	print (str(src_data).strip('[]'))
    	print ("Results")
    	print (str(result_data).strip('[]'))
    	self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)



if __name__ == '__main__':
    gr_unittest.run(qa_OOK_Modulator_two)
