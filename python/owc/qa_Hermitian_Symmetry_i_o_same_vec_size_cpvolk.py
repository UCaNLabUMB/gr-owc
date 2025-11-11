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
    from gnuradio.owc import Hermitian_Symmetry_i_o_same_vec_size_cpvolk
except ImportError:
    import os
    import sys
    dirname, filename = os.path.split(os.path.abspath(__file__))
    sys.path.append(os.path.join(dirname, "bindings"))
    from gnuradio.owc import Hermitian_Symmetry_i_o_same_vec_size_cpvolk

class qa_Hermitian_Symmetry_i_o_same_vec_size_cpvolk(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_instance(self):
        instance = Hermitian_Symmetry_i_o_same_vec_size_cpvolk(32, False)

    def test_001_Hermitian_test(self):
        src_data = [2.0 + 1.0j, 4 + 6.0j, 2.0 + 0j, 0 + 5j, 1 + 4.0j, 3 + 7.0j, 3.0 + 8.0j, 5 + 2.0j, 4 + 3.0j, 3 + 1.0j, 7 + 8.0j, 2.0j, 3.0j, 4 + 6.0j, 2 + 3.0j, 1.0j]
        expected_result = [0j, (5-2j), (3-8j), (3-7j), 0j, (3+7j), (3+8j), (5+2j), 0j, -1j, (2-3j), (4-6j), 0j, (4+6j), (2+3j), 1j]

        src = blocks.vector_source_c(src_data)
        s2v = blocks.stream_to_vector(gr.sizeof_gr_complex, 8)
        blk = Hermitian_Symmetry_i_o_same_vec_size_cpvolk(8, True)
        v2s = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 8)
        dst = blocks.vector_sink_c()
        
        self.tb.connect(src, s2v)
        self.tb.connect(s2v, blk)
        self.tb.connect(blk, v2s)
        self.tb.connect(v2s, dst)
        self.tb.run()
        result_data = dst.data()
        print ("expected_result: ")
        print (str(expected_result).strip('[]'))
        print ("Results")
        print (str(result_data).strip('[]'))
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 1)

    def test_002_Hermitian_test(self):
        src_data = [2.0 + 1.0j, 4 + 6.0j, 2.0 + 0j, 0 + 5j, 1 + 4.0j, 3 + 7.0j, 3.0 + 8.0j, 5 + 2.0j, 4 + 3.0j, 3 + 1.0j, 7 + 8.0j, 2.0j, 3.0j, 4 + 6.0j, 2 + 3.0j, 1.0j]
        expected_result = [0j, -1j, (2-3j), (4-6j), -3j, -2j, (7-8j), (3-1j), 0j, (3+1j), (7+8j), 2j, 3j, (4+6j), (2+3j), 1j]

        src = blocks.vector_source_c(src_data)
        s2v = blocks.stream_to_vector(gr.sizeof_gr_complex, 16)
        blk = Hermitian_Symmetry_i_o_same_vec_size_cpvolk(16, True)
        v2s = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 16)
        dst = blocks.vector_sink_c()
        
        self.tb.connect(src, s2v)
        self.tb.connect(s2v, blk)
        self.tb.connect(blk, v2s)
        self.tb.connect(v2s, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 1)

    def test_003_Hermitian_test(self):
        src_data = [0, 4, 0j, 0 + 5j, 1 + 4.0j, 3 + 7.0j, 3.0 + 8.0j, 5 + 2.0j, 4 + 3.0j, 3 + 1.0j, 7 + 8.0j, 2.0j, 3.0j, 4 + 6.0j, 2 + 3.0j, 1.0j]
        expected_result = [0j, (4+0j), 0j, 5j, (1+4j), (3+7j), (3+8j), (5+2j), 0j, (5-2j), (3-8j), (3-7j), (1-4j), -5j, -0j, (4-0j)]

        src = blocks.vector_source_c(src_data)
        s2v = blocks.stream_to_vector(gr.sizeof_gr_complex, 16)
        blk = Hermitian_Symmetry_i_o_same_vec_size_cpvolk(16, False)
        v2s = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 16)
        dst = blocks.vector_sink_c()
        
        self.tb.connect(src, s2v)
        self.tb.connect(s2v, blk)
        self.tb.connect(blk, v2s)
        self.tb.connect(v2s, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 1)

    def test_004_Hermitian_test(self):
        src_data = [0, 4, 0j, 0 + 5j, 1 + 4.0j, 3 + 7.0j, 3.0 + 8.0j, 5 + 2.0j, 4 + 3.0j, 3 + 1.0j, 7 + 8.0j, 2.0j, 3.0j, 4 + 6.0j, 2 + 3.0j, 1.0j]
        expected_result = [0j, (4+0j), 0j, 5j, 0j, -5j, -0j, (4-0j), 0j, (3+1j), (7+8j), 2j, 0j, -2j, (7-8j), (3-1j)]

        src = blocks.vector_source_c(src_data)
        s2v = blocks.stream_to_vector(gr.sizeof_gr_complex, 8)
        blk = Hermitian_Symmetry_i_o_same_vec_size_cpvolk(8, False)
        v2s = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 8)
        dst = blocks.vector_sink_c()
        
        self.tb.connect(src, s2v)
        self.tb.connect(s2v, blk)
        self.tb.connect(blk, v2s)
        self.tb.connect(v2s, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 1)


if __name__ == '__main__':
    gr_unittest.run(qa_Hermitian_Symmetry_i_o_same_vec_size_cpvolk)
