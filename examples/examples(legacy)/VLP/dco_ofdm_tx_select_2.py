#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Two channel DCO-OFDM Tx with Subcarrier - Select
# Author: ucanlab
# Description: (modified from Arsalan's DCO-OFDM Flowgraph in gr-owc)
# GNU Radio version: 3.10.1.1

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

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from xmlrpc.server import SimpleXMLRPCServer
import threading



from gnuradio import qtgui

class dco_ofdm_tx_select_2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Two channel DCO-OFDM Tx with Subcarrier - Select", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Two channel DCO-OFDM Tx with Subcarrier - Select")
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

        self.settings = Qt.QSettings("GNU Radio", "dco_ofdm_tx_select_2")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.sync_word2 = sync_word2 = [0j, 0j, 0j, 0j, 0j, 0j, (-1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1 +0j), (1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), 0j, (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), 0j, 0j, 0j, 0j, 0j]
        self.sync_word1 = sync_word1 = [0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.]
        self.select4 = select4 = 0
        self.select3 = select3 = 0
        self.select2 = select2 = 0
        self.select1 = select1 = 0
        self.samp_rate_usrp = samp_rate_usrp = 1000000
        self.samp_rate = samp_rate = 5000000
        self.packet_len = packet_len = 96
        self.length_tag_key = length_tag_key = "packet_len"
        self.freq_8 = freq_8 = 500000
        self.freq_7 = freq_7 = 1000000
        self.freq_6 = freq_6 = 500000
        self.freq_5 = freq_5 = 1000000
        self.freq_4 = freq_4 = 500000
        self.freq_3 = freq_3 = 1000000
        self.freq_2 = freq_2 = 500000
        self.freq_1 = freq_1 = 1000000
        self.fft_len = fft_len = 64
        self.amp_8 = amp_8 = 0.3
        self.amp_7 = amp_7 = 0.3
        self.amp_6 = amp_6 = 0.35
        self.amp_5 = amp_5 = 0.35
        self.amp_4 = amp_4 = 0.2
        self.amp_3 = amp_3 = 0.2
        self.amp_2 = amp_2 = 0.25
        self.amp_1 = amp_1 = 0.25
        self.Mode_C2_TXB = Mode_C2_TXB = 0
        self.Mode_C2_TXA = Mode_C2_TXA = 0
        self.Mode_C1_TXB = Mode_C1_TXB = 0
        self.Mode_C1_TXA = Mode_C1_TXA = 0

        ##################################################
        # Blocks
        ##################################################
        self.xmlrpc_server_0 = SimpleXMLRPCServer(('localhost', 8080), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("addr=192.168.10.2", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
            '',
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate_usrp)
        # No synchronization enforced.

        self.uhd_usrp_sink_0.set_center_freq(0, 0)
        self.uhd_usrp_sink_0.set_antenna('AB', 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)

        self.uhd_usrp_sink_0.set_center_freq(0, 1)
        self.uhd_usrp_sink_0.set_antenna('AB', 1)
        self.uhd_usrp_sink_0.set_gain(0, 1)
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.blocks_selector_0_1 = blocks.selector(gr.sizeof_float*1,select3,0)
        self.blocks_selector_0_1.set_enabled(True)
        self.blocks_selector_0_0_0 = blocks.selector(gr.sizeof_float*1,select4,0)
        self.blocks_selector_0_0_0.set_enabled(True)
        self.blocks_selector_0_0 = blocks.selector(gr.sizeof_float*1,select2,0)
        self.blocks_selector_0_0.set_enabled(True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_float*1,select1,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_ff(1/2)
        self.blocks_multiply_const_vxx_1_0_0 = blocks.multiply_const_ff(1/2)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_ff(1/2)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(1/2)
        self.blocks_float_to_complex_2_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_2 = blocks.float_to_complex(1)
        self.blocks_add_xx_0_1 = blocks.add_vff(1)
        self.blocks_add_xx_0_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1_3_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq_5, amp_5, 0, 0)
        self.analog_sig_source_x_1_3 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq_1, amp_1, 0, 0)
        self.analog_sig_source_x_1_2_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq_6, amp_6, 0, 0)
        self.analog_sig_source_x_1_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq_2, amp_2, 0, 0)
        self.analog_sig_source_x_1_1_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq_7, amp_7, 0, 0)
        self.analog_sig_source_x_1_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq_3, amp_3, 0, 0)
        self.analog_sig_source_x_1_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq_8, amp_8, 0, 0)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq_4, amp_4, 0, 0)
        # Create the options list
        self._Mode_C2_TXB_options = [0, 1]
        # Create the labels list
        self._Mode_C2_TXB_labels = ['Single', 'Double']
        # Create the combo box
        self._Mode_C2_TXB_tool_bar = Qt.QToolBar(self)
        self._Mode_C2_TXB_tool_bar.addWidget(Qt.QLabel("'Mode_C2_TXB'" + ": "))
        self._Mode_C2_TXB_combo_box = Qt.QComboBox()
        self._Mode_C2_TXB_tool_bar.addWidget(self._Mode_C2_TXB_combo_box)
        for _label in self._Mode_C2_TXB_labels: self._Mode_C2_TXB_combo_box.addItem(_label)
        self._Mode_C2_TXB_callback = lambda i: Qt.QMetaObject.invokeMethod(self._Mode_C2_TXB_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._Mode_C2_TXB_options.index(i)))
        self._Mode_C2_TXB_callback(self.Mode_C2_TXB)
        self._Mode_C2_TXB_combo_box.currentIndexChanged.connect(
            lambda i: self.set_Mode_C2_TXB(self._Mode_C2_TXB_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._Mode_C2_TXB_tool_bar)
        # Create the options list
        self._Mode_C2_TXA_options = [0, 1]
        # Create the labels list
        self._Mode_C2_TXA_labels = ['Single ', 'Double']
        # Create the combo box
        self._Mode_C2_TXA_tool_bar = Qt.QToolBar(self)
        self._Mode_C2_TXA_tool_bar.addWidget(Qt.QLabel("'Mode_C2_TXA'" + ": "))
        self._Mode_C2_TXA_combo_box = Qt.QComboBox()
        self._Mode_C2_TXA_tool_bar.addWidget(self._Mode_C2_TXA_combo_box)
        for _label in self._Mode_C2_TXA_labels: self._Mode_C2_TXA_combo_box.addItem(_label)
        self._Mode_C2_TXA_callback = lambda i: Qt.QMetaObject.invokeMethod(self._Mode_C2_TXA_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._Mode_C2_TXA_options.index(i)))
        self._Mode_C2_TXA_callback(self.Mode_C2_TXA)
        self._Mode_C2_TXA_combo_box.currentIndexChanged.connect(
            lambda i: self.set_Mode_C2_TXA(self._Mode_C2_TXA_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._Mode_C2_TXA_tool_bar)
        # Create the options list
        self._Mode_C1_TXB_options = [0, 1]
        # Create the labels list
        self._Mode_C1_TXB_labels = ['Single', 'Double']
        # Create the combo box
        self._Mode_C1_TXB_tool_bar = Qt.QToolBar(self)
        self._Mode_C1_TXB_tool_bar.addWidget(Qt.QLabel("'Mode_C1_TXB'" + ": "))
        self._Mode_C1_TXB_combo_box = Qt.QComboBox()
        self._Mode_C1_TXB_tool_bar.addWidget(self._Mode_C1_TXB_combo_box)
        for _label in self._Mode_C1_TXB_labels: self._Mode_C1_TXB_combo_box.addItem(_label)
        self._Mode_C1_TXB_callback = lambda i: Qt.QMetaObject.invokeMethod(self._Mode_C1_TXB_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._Mode_C1_TXB_options.index(i)))
        self._Mode_C1_TXB_callback(self.Mode_C1_TXB)
        self._Mode_C1_TXB_combo_box.currentIndexChanged.connect(
            lambda i: self.set_Mode_C1_TXB(self._Mode_C1_TXB_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._Mode_C1_TXB_tool_bar)
        # Create the options list
        self._Mode_C1_TXA_options = [0, 1]
        # Create the labels list
        self._Mode_C1_TXA_labels = ['Single', 'Double']
        # Create the combo box
        self._Mode_C1_TXA_tool_bar = Qt.QToolBar(self)
        self._Mode_C1_TXA_tool_bar.addWidget(Qt.QLabel("'Mode_C1_TXA'" + ": "))
        self._Mode_C1_TXA_combo_box = Qt.QComboBox()
        self._Mode_C1_TXA_tool_bar.addWidget(self._Mode_C1_TXA_combo_box)
        for _label in self._Mode_C1_TXA_labels: self._Mode_C1_TXA_combo_box.addItem(_label)
        self._Mode_C1_TXA_callback = lambda i: Qt.QMetaObject.invokeMethod(self._Mode_C1_TXA_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._Mode_C1_TXA_options.index(i)))
        self._Mode_C1_TXA_callback(self.Mode_C1_TXA)
        self._Mode_C1_TXA_combo_box.currentIndexChanged.connect(
            lambda i: self.set_Mode_C1_TXA(self._Mode_C1_TXA_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._Mode_C1_TXA_tool_bar)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_1_0_0, 0), (self.blocks_add_xx_0_0_0, 1))
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_selector_0_0, 0))
        self.connect((self.analog_sig_source_x_1_1_0, 0), (self.blocks_add_xx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_1_1_0, 0), (self.blocks_selector_0_0_0, 0))
        self.connect((self.analog_sig_source_x_1_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_1_2_0, 0), (self.blocks_add_xx_0_1, 1))
        self.connect((self.analog_sig_source_x_1_3, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_1_3, 0), (self.blocks_selector_0, 0))
        self.connect((self.analog_sig_source_x_1_3_0, 0), (self.blocks_add_xx_0_1, 0))
        self.connect((self.analog_sig_source_x_1_3_0, 0), (self.blocks_selector_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_add_xx_0_0_0, 0), (self.blocks_multiply_const_vxx_1_0_0, 0))
        self.connect((self.blocks_add_xx_0_1, 0), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.blocks_float_to_complex_2, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_2, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_float_to_complex_2_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.blocks_float_to_complex_2_0, 0), (self.uhd_usrp_sink_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_selector_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_selector_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_0, 0), (self.blocks_selector_0_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.blocks_selector_0_1, 1))
        self.connect((self.blocks_selector_0, 0), (self.blocks_float_to_complex_2, 0))
        self.connect((self.blocks_selector_0_0, 0), (self.blocks_float_to_complex_2, 1))
        self.connect((self.blocks_selector_0_0_0, 0), (self.blocks_float_to_complex_2_0, 1))
        self.connect((self.blocks_selector_0_1, 0), (self.blocks_float_to_complex_2_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dco_ofdm_tx_select_2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1

    def get_select4(self):
        return self.select4

    def set_select4(self, select4):
        self.select4 = select4
        self.blocks_selector_0_0_0.set_input_index(self.select4)

    def get_select3(self):
        return self.select3

    def set_select3(self, select3):
        self.select3 = select3
        self.blocks_selector_0_1.set_input_index(self.select3)

    def get_select2(self):
        return self.select2

    def set_select2(self, select2):
        self.select2 = select2
        self.blocks_selector_0_0.set_input_index(self.select2)

    def get_select1(self):
        return self.select1

    def set_select1(self, select1):
        self.select1 = select1
        self.blocks_selector_0.set_input_index(self.select1)

    def get_samp_rate_usrp(self):
        return self.samp_rate_usrp

    def set_samp_rate_usrp(self, samp_rate_usrp):
        self.samp_rate_usrp = samp_rate_usrp
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate_usrp)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_2_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_3_0.set_sampling_freq(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key

    def get_freq_8(self):
        return self.freq_8

    def set_freq_8(self, freq_8):
        self.freq_8 = freq_8
        self.analog_sig_source_x_1_0_0.set_frequency(self.freq_8)

    def get_freq_7(self):
        return self.freq_7

    def set_freq_7(self, freq_7):
        self.freq_7 = freq_7
        self.analog_sig_source_x_1_1_0.set_frequency(self.freq_7)

    def get_freq_6(self):
        return self.freq_6

    def set_freq_6(self, freq_6):
        self.freq_6 = freq_6
        self.analog_sig_source_x_1_2_0.set_frequency(self.freq_6)

    def get_freq_5(self):
        return self.freq_5

    def set_freq_5(self, freq_5):
        self.freq_5 = freq_5
        self.analog_sig_source_x_1_3_0.set_frequency(self.freq_5)

    def get_freq_4(self):
        return self.freq_4

    def set_freq_4(self, freq_4):
        self.freq_4 = freq_4
        self.analog_sig_source_x_1_0.set_frequency(self.freq_4)

    def get_freq_3(self):
        return self.freq_3

    def set_freq_3(self, freq_3):
        self.freq_3 = freq_3
        self.analog_sig_source_x_1_1.set_frequency(self.freq_3)

    def get_freq_2(self):
        return self.freq_2

    def set_freq_2(self, freq_2):
        self.freq_2 = freq_2
        self.analog_sig_source_x_1_2.set_frequency(self.freq_2)

    def get_freq_1(self):
        return self.freq_1

    def set_freq_1(self, freq_1):
        self.freq_1 = freq_1
        self.analog_sig_source_x_1_3.set_frequency(self.freq_1)

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len

    def get_amp_8(self):
        return self.amp_8

    def set_amp_8(self, amp_8):
        self.amp_8 = amp_8
        self.analog_sig_source_x_1_0_0.set_amplitude(self.amp_8)

    def get_amp_7(self):
        return self.amp_7

    def set_amp_7(self, amp_7):
        self.amp_7 = amp_7
        self.analog_sig_source_x_1_1_0.set_amplitude(self.amp_7)

    def get_amp_6(self):
        return self.amp_6

    def set_amp_6(self, amp_6):
        self.amp_6 = amp_6
        self.analog_sig_source_x_1_2_0.set_amplitude(self.amp_6)

    def get_amp_5(self):
        return self.amp_5

    def set_amp_5(self, amp_5):
        self.amp_5 = amp_5
        self.analog_sig_source_x_1_3_0.set_amplitude(self.amp_5)

    def get_amp_4(self):
        return self.amp_4

    def set_amp_4(self, amp_4):
        self.amp_4 = amp_4
        self.analog_sig_source_x_1_0.set_amplitude(self.amp_4)

    def get_amp_3(self):
        return self.amp_3

    def set_amp_3(self, amp_3):
        self.amp_3 = amp_3
        self.analog_sig_source_x_1_1.set_amplitude(self.amp_3)

    def get_amp_2(self):
        return self.amp_2

    def set_amp_2(self, amp_2):
        self.amp_2 = amp_2
        self.analog_sig_source_x_1_2.set_amplitude(self.amp_2)

    def get_amp_1(self):
        return self.amp_1

    def set_amp_1(self, amp_1):
        self.amp_1 = amp_1
        self.analog_sig_source_x_1_3.set_amplitude(self.amp_1)

    def get_Mode_C2_TXB(self):
        return self.Mode_C2_TXB

    def set_Mode_C2_TXB(self, Mode_C2_TXB):
        self.Mode_C2_TXB = Mode_C2_TXB
        self._Mode_C2_TXB_callback(self.Mode_C2_TXB)

    def get_Mode_C2_TXA(self):
        return self.Mode_C2_TXA

    def set_Mode_C2_TXA(self, Mode_C2_TXA):
        self.Mode_C2_TXA = Mode_C2_TXA
        self._Mode_C2_TXA_callback(self.Mode_C2_TXA)

    def get_Mode_C1_TXB(self):
        return self.Mode_C1_TXB

    def set_Mode_C1_TXB(self, Mode_C1_TXB):
        self.Mode_C1_TXB = Mode_C1_TXB
        self._Mode_C1_TXB_callback(self.Mode_C1_TXB)

    def get_Mode_C1_TXA(self):
        return self.Mode_C1_TXA

    def set_Mode_C1_TXA(self, Mode_C1_TXA):
        self.Mode_C1_TXA = Mode_C1_TXA
        self._Mode_C1_TXA_callback(self.Mode_C1_TXA)




def main(top_block_cls=dco_ofdm_tx_select_2, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

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
