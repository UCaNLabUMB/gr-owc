#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.5.1

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from xmlrpc.server import SimpleXMLRPCServer
import threading
import ad2




class OWC_SimpleTone(gr.top_block):

    def __init__(self, adb_amp=5, node='182', samp_rate=300000, sig_freq=1000):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)

        ##################################################
        # Parameters
        ##################################################
        self.adb_amp = adb_amp
        self.node = node
        self.samp_rate = samp_rate
        self.sig_freq = sig_freq

        ##################################################
        # Blocks
        ##################################################

        self.xmlrpc_server_0 = SimpleXMLRPCServer(("10.1.1." + node, 8080), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_int*1, samp_rate,True)
        self.analog_const_source_x_0 = analog.sig_source_i(0, analog.GR_CONST_WAVE, 0, 0, sig_freq)
        self.ad2_AD2_AnalogOut_Sine_i_0 = ad2.AD2_AnalogOut_Sine_i(0, adb_amp, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.ad2_AD2_AnalogOut_Sine_i_0, 0))


    def get_adb_amp(self):
        return self.adb_amp

    def set_adb_amp(self, adb_amp):
        self.adb_amp = adb_amp

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_sig_freq(self):
        return self.sig_freq

    def set_sig_freq(self, sig_freq):
        self.sig_freq = sig_freq
        self.analog_const_source_x_0.set_offset(self.sig_freq)



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "-n", "--adb-amp", dest="adb_amp", type=intx, default=5,
        help="Set Analog Discovery Board Ampltiude [default=%(default)r]")
    parser.add_argument(
        "-n", "--node", dest="node", type=str, default='182',
        help="Set Node Number [default=%(default)r]")
    parser.add_argument(
        "-a", "--samp-rate", dest="samp_rate", type=eng_float, default=eng_notation.num_to_str(float(300000)),
        help="Set Sample Rate [default=%(default)r]")
    parser.add_argument(
        "-f", "--sig-freq", dest="sig_freq", type=intx, default=1000,
        help="Set Signal Frequency [default=%(default)r]")
    return parser


def main(top_block_cls=OWC_SimpleTone, options=None):
    if options is None:
        options = argument_parser().parse_args()
    tb = top_block_cls(adb_amp=options.adb_amp, node=options.node, samp_rate=options.samp_rate, sig_freq=options.sig_freq)

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
