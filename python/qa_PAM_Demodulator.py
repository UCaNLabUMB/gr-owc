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

class qa_PAM_Demodulator(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001_t(self):
    	src_data = (6,7)
    	expected_result = (6,7)
    	
    	src = blocks.vector_source_f(src_data)   	
    	blk = owc.PAM_Demodulator(8,7,0,1)
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
    	src_data = ((5/7),(5/7),(5/7),1,1,1)
    	expected_result = (5,7)
    	
    	src = blocks.vector_source_f(src_data)   	
    	blk = owc.PAM_Demodulator(8,1,0,3)
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
    	
    def test_003_t(self):
    	src_data = (10,10,10,10,5*(10/15),5*(10/15),5*(10/15),5*(10/15))
    	expected_result = (15,5)
    	
    	src = blocks.vector_source_f(src_data)   	
    	blk = owc.PAM_Demodulator(16,10,0,4)
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
    gr_unittest.run(qa_PAM_Demodulator)
