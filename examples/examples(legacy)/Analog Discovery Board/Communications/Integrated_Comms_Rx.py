#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time



from gnuradio import qtgui

class Integrated_Comms_Rx(gr.top_block, Qt.QWidget):

    def __init__(self, node='182'):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Integrated_Comms_Rx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.node = node

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
        self.sync_word2 = sync_word2 = [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0]
        self.sync_word1 = sync_word1 = [0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.]
        self.samp_rate = samp_rate = 500000
        self.rolloff = rolloff = 0
        self.pilot_syms_rf = pilot_syms_rf = ((-1,1,-1,1),)
        self.pilot_symbols = pilot_symbols = ((-1, 1,),)
        self.pilot_carriers_rf = pilot_carriers_rf = ((-10,-2,2,10),)
        self.pilot_carriers = pilot_carriers = ((-28, -1),)
        self.packet_len = packet_len = 28
        self.occupied_carriers_rf = occupied_carriers_rf = ((carrier_list_rf),)
        self.header_ph = header_ph = digital.packet_header_ofdm(occupied_carriers, 1, len_tag_key, "frame_"+len_tag_key, bits_per_header_sym=header_mod.bits_per_symbol(), bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False)
        self.filename = filename = "/home/ucanlab/Downloads/Ep"
        self.CP_len = CP_len = fft_len//4

        ##################################################
        # Blocks
        ##################################################

        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_samp_rate(1e6)
        # No synchronization enforced.

        self.uhd_usrp_source_0.set_center_freq(915e6, 0)
        self.uhd_usrp_source_0.set_gain(40, 0)
        self.digital_ofdm_rx_0_0 = digital.ofdm_rx(
            fft_len=fft_len, cp_len=CP_len,
            frame_length_tag_key='frame_'+len_tag_key,
            packet_length_tag_key=len_tag_key,
            occupied_carriers=occupied_carriers_rf,
            pilot_carriers=pilot_carriers_rf,
            pilot_symbols=pilot_syms_rf,
            sync_word1=sync_word1,
            sync_word2=sync_word2,
            bps_header=1,
            bps_payload=2,
            debug_log=False,
            scramble_bits=False)
        self.blocks_tag_gate_0_0 = blocks.tag_gate(gr.sizeof_char * 1, False)
        self.blocks_tag_gate_0_0.set_single_key("")
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/ucanlab/Downloads/test_96_outcome.txt', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_tag_gate_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.digital_ofdm_rx_0_0, 0), (self.blocks_tag_gate_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_ofdm_rx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Integrated_Comms_Rx")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

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

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

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

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_occupied_carriers_rf(self):
        return self.occupied_carriers_rf

    def set_occupied_carriers_rf(self, occupied_carriers_rf):
        self.occupied_carriers_rf = occupied_carriers_rf

    def get_header_ph(self):
        return self.header_ph

    def set_header_ph(self, header_ph):
        self.header_ph = header_ph

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def get_CP_len(self):
        return self.CP_len

    def set_CP_len(self, CP_len):
        self.CP_len = CP_len



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "-n", "--node", dest="node", type=str, default='182',
        help="Set Node Number [default=%(default)r]")
    return parser


def main(top_block_cls=Integrated_Comms_Rx, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(node=options.node)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
