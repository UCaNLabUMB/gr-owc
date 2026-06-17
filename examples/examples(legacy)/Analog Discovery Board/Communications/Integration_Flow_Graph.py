#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: Jack Nguyen
# GNU Radio version: 3.10.5.1

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import gr, pdu
from gnuradio import owc
from gnuradio import uhd
import time
from xmlrpc.server import SimpleXMLRPCServer
import threading
import Integration_Flow_Graph_epy_block_0 as epy_block_0  # embedded python block
import Integration_Flow_Graph_epy_block_0_0 as epy_block_0_0  # embedded python block




class Integration_Flow_Graph(gr.top_block):

    def __init__(self, node_id='182'):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)

        ##################################################
        # Parameters
        ##################################################
        self.node_id = node_id

        ##################################################
        # Variables
        ##################################################
        self.carrier_list = carrier_list = (list(range(-12, -2)))
        self.payload_mod = payload_mod = digital.constellation_qpsk()
        self.occupied_carriers = occupied_carriers = (carrier_list,)
        self.len_tag_key = len_tag_key = "packet_len"
        self.header_mod = header_mod = digital.constellation_bpsk()
        self.fft_len = fft_len = 64
        self.carrier_list_rf = carrier_list_rf = (list(range(-7, -2)) + list(range(3, 8)))
        self.variable_pb = variable_pb = 0
        self.sync_word2 = sync_word2 = [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0]
        self.sync_word1 = sync_word1 = [0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.]
        self.selector = selector = 0
        self.samp_rate = samp_rate = 100000
        self.rolloff = rolloff = 0
        self.pilot_syms_rf = pilot_syms_rf = ((-1,1,-1,1),)
        self.pilot_symbols = pilot_symbols = ((-1, 1),)
        self.pilot_carriers_rf = pilot_carriers_rf = ((-10,-2,2,10),)
        self.pilot_carriers = pilot_carriers = ((-28, -1),)
        self.packet_len_rf = packet_len_rf = 96
        self.packet_len = packet_len = 9
        self.occupied_carriers_rf = occupied_carriers_rf = ((carrier_list_rf),)
        self.len_tag_key_rf = len_tag_key_rf = "packet_len_rf"
        self.header_ph = header_ph = digital.packet_header_ofdm(occupied_carriers, 1, len_tag_key, "frame_"+len_tag_key, bits_per_header_sym=header_mod.bits_per_symbol(), bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False)
        self.fc = fc = 915e6
        self.CP_len = CP_len = fft_len//4

        ##################################################
        # Blocks
        ##################################################

        self.xmlrpc_server_0_0 = SimpleXMLRPCServer(('10.1.1.' + node_id, 8080), allow_none=True)
        self.xmlrpc_server_0_0.register_instance(self)
        self.xmlrpc_server_0_0_thread = threading.Thread(target=self.xmlrpc_server_0_0.serve_forever)
        self.xmlrpc_server_0_0_thread.daemon = True
        self.xmlrpc_server_0_0_thread.start()
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(('', "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            '',
        )
        self.uhd_usrp_sink_0.set_samp_rate(1e6)
        # No synchronization enforced.

        self.uhd_usrp_sink_0.set_center_freq(fc, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_gain(65, 0)
        self.pdu_pdu_to_tagged_stream_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, len_tag_key)
        self.owc_Hermitian_Symmetry_i_o_same_vec_size_cplus_0 = owc.Hermitian_Symmetry_i_o_same_vec_size_cplus(fft_len, False)
        self.fft_vxx_0_0 = fft.fft_vcc(fft_len, False, (), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(fft_len, False, (), True, 1)
        self.epy_block_0_0 = epy_block_0_0.blk()
        self.epy_block_0 = epy_block_0.blk(samp_rate=samp_rate, amplitude=1, len_tag_key=len_tag_key)
        self.digital_packet_headergenerator_bb_0_0 = digital.packet_headergenerator_bb(header_ph, len_tag_key)
        self.digital_packet_headergenerator_bb_0 = digital.packet_headergenerator_bb(header_ph, len_tag_key)
        self.digital_ofdm_cyclic_prefixer_0_0 = digital.ofdm_cyclic_prefixer(
            fft_len,
            fft_len + CP_len,
            rolloff,
            len_tag_key)
        self.digital_ofdm_cyclic_prefixer_0 = digital.ofdm_cyclic_prefixer(
            fft_len,
            fft_len + CP_len,
            rolloff,
            len_tag_key)
        self.digital_ofdm_carrier_allocator_cvc_0_0 = digital.ofdm_carrier_allocator_cvc( fft_len, occupied_carriers_rf, pilot_carriers_rf, pilot_syms_rf, (sync_word1, sync_word2), len_tag_key, True)
        self.digital_ofdm_carrier_allocator_cvc_0 = digital.ofdm_carrier_allocator_cvc( fft_len, occupied_carriers, pilot_carriers, pilot_symbols, (sync_word1, sync_word2), len_tag_key, True)
        self.digital_crc32_bb_0_0 = digital.crc32_bb(False, len_tag_key, True)
        self.digital_crc32_bb_0 = digital.crc32_bb(False, len_tag_key, True)
        self.digital_chunks_to_symbols_xx_0_1 = digital.chunks_to_symbols_bc(payload_mod.points(), 1)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bc(header_mod.points(), 1)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc(header_mod.points(), 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(payload_mod.points(), 1)
        self.blocks_var_to_msg_0 = blocks.var_to_msg_pair('trigger')
        self.blocks_tagged_stream_mux_0_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, (len_tag_key), 0)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, (len_tag_key), 0)
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (499640,720,499640))
        self.blocks_selector_0 = blocks.selector(gr.sizeof_char*1,0,selector)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, payload_mod.bits_per_symbol(), len_tag_key, False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, payload_mod.bits_per_symbol(), len_tag_key, False, gr.GR_LSB_FIRST)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_cc(0.035)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(0.05)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_const_source_x_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_var_to_msg_0, 'msgout'), (self.epy_block_0_0, 'trigger'))
        self.msg_connect((self.epy_block_0_0, 'out'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_stream_mux_0, 2))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_1, 0))
        self.connect((self.blocks_selector_0, 0), (self.digital_crc32_bb_0, 0))
        self.connect((self.blocks_selector_0, 1), (self.digital_crc32_bb_0_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_ofdm_carrier_allocator_cvc_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0_0, 0), (self.digital_ofdm_carrier_allocator_cvc_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.blocks_tagged_stream_mux_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_1, 0), (self.blocks_tagged_stream_mux_0_0, 1))
        self.connect((self.digital_crc32_bb_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_crc32_bb_0, 0), (self.digital_packet_headergenerator_bb_0, 0))
        self.connect((self.digital_crc32_bb_0_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.digital_crc32_bb_0_0, 0), (self.digital_packet_headergenerator_bb_0_0, 0))
        self.connect((self.digital_ofdm_carrier_allocator_cvc_0, 0), (self.owc_Hermitian_Symmetry_i_o_same_vec_size_cplus_0, 0))
        self.connect((self.digital_ofdm_carrier_allocator_cvc_0_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.digital_ofdm_cyclic_prefixer_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.digital_packet_headergenerator_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.digital_packet_headergenerator_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.digital_ofdm_cyclic_prefixer_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.digital_ofdm_cyclic_prefixer_0_0, 0))
        self.connect((self.owc_Hermitian_Symmetry_i_o_same_vec_size_cplus_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_selector_0, 0))


    def get_node_id(self):
        return self.node_id

    def set_node_id(self, node_id):
        self.node_id = node_id

    def get_carrier_list(self):
        return self.carrier_list

    def set_carrier_list(self, carrier_list):
        self.carrier_list = carrier_list
        self.set_occupied_carriers((self.carrier_list,))

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_header_ph(digital.packet_header_ofdm(self.occupied_carriers, 1, self.len_tag_key, "frame_"+self.len_tag_key, bits_per_header_sym=header_mod.bits_per_symbol(), bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False))

    def get_len_tag_key(self):
        return self.len_tag_key

    def set_len_tag_key(self, len_tag_key):
        self.len_tag_key = len_tag_key
        self.set_header_ph(digital.packet_header_ofdm(self.occupied_carriers, 1, self.len_tag_key, "frame_"+self.len_tag_key, bits_per_header_sym=header_mod.bits_per_symbol(), bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False))
        self.epy_block_0.len_tag_key = self.len_tag_key

    def get_header_mod(self):
        return self.header_mod

    def set_header_mod(self, header_mod):
        self.header_mod = header_mod

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        self.set_CP_len(self.fft_len//4)

    def get_carrier_list_rf(self):
        return self.carrier_list_rf

    def set_carrier_list_rf(self, carrier_list_rf):
        self.carrier_list_rf = carrier_list_rf
        self.set_occupied_carriers_rf(((self.carrier_list_rf),))

    def get_variable_pb(self):
        return self.variable_pb

    def set_variable_pb(self, variable_pb):
        self.variable_pb = variable_pb
        self.blocks_var_to_msg_0.variable_changed(self.variable_pb)

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1

    def get_selector(self):
        return self.selector

    def set_selector(self, selector):
        self.selector = selector
        self.blocks_selector_0.set_output_index(self.selector)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.epy_block_0.samp_rate = self.samp_rate

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff

    def get_pilot_syms_rf(self):
        return self.pilot_syms_rf

    def set_pilot_syms_rf(self, pilot_syms_rf):
        self.pilot_syms_rf = pilot_syms_rf

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols

    def get_pilot_carriers_rf(self):
        return self.pilot_carriers_rf

    def set_pilot_carriers_rf(self, pilot_carriers_rf):
        self.pilot_carriers_rf = pilot_carriers_rf

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers

    def get_packet_len_rf(self):
        return self.packet_len_rf

    def set_packet_len_rf(self, packet_len_rf):
        self.packet_len_rf = packet_len_rf

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_occupied_carriers_rf(self):
        return self.occupied_carriers_rf

    def set_occupied_carriers_rf(self, occupied_carriers_rf):
        self.occupied_carriers_rf = occupied_carriers_rf

    def get_len_tag_key_rf(self):
        return self.len_tag_key_rf

    def set_len_tag_key_rf(self, len_tag_key_rf):
        self.len_tag_key_rf = len_tag_key_rf

    def get_header_ph(self):
        return self.header_ph

    def set_header_ph(self, header_ph):
        self.header_ph = header_ph
        self.digital_packet_headergenerator_bb_0.set_header_formatter(self.header_ph)
        self.digital_packet_headergenerator_bb_0_0.set_header_formatter(self.header_ph)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.uhd_usrp_sink_0.set_center_freq(self.fc, 0)

    def get_CP_len(self):
        return self.CP_len

    def set_CP_len(self, CP_len):
        self.CP_len = CP_len



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "-n", "--node-id", dest="node_id", type=str, default='182',
        help="Set Node Number [default=%(default)r]")
    return parser


def main(top_block_cls=Integration_Flow_Graph, options=None):
    if options is None:
        options = argument_parser().parse_args()
    tb = top_block_cls(node_id=options.node_id)

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
