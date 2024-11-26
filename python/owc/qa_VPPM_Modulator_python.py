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
from gnuradio.owc import VPPM_Modulator_python

class qa_VPPM_Modulator_python(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_instance(self):
        instance = VPPM_Modulator_python(2,1,4,2)

    def test_001_VPPM(self):
        src_data = (0,1)
        expected_result = (2,2,1,1,1,1,2,2)
        
        src = blocks.vector_source_f(src_data)      
        blk = VPPM_Modulator_python(2,1,4,2)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()

        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

    def test_002_VPPM(self):
        src_data = (0,1,1)
        expected_result = (4,0,0,0,0,4,0,0,4)
        
        src = blocks.vector_source_f(src_data)      
        blk = VPPM_Modulator_python(4,0,3,1)
        dst = blocks.vector_sink_f()
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        
        result_data = dst.data()

        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)


if __name__ == '__main__':
    gr_unittest.run(qa_VPPM_Modulator_python)
