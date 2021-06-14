#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Combined
# Author: arsalan
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

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
from gnuradio import eng_notation
from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
import owc
import time
import threading

from gnuradio import qtgui

class combined(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Combined")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Combined")
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

        self.settings = Qt.QSettings("GNU Radio", "combined")

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
        self.threshold = threshold = 0
        self.Min = Min = 0
        self.Max = Max = 0.001
        self.window_size = window_size = 1000
        self.tx_psi_3_3 = tx_psi_3_3 = 0
        self.tx_psi_3_2 = tx_psi_3_2 = 90
        self.tx_psi_3_1 = tx_psi_3_1 = 90
        self.tx_psi_2_3 = tx_psi_2_3 = 90
        self.tx_psi_2_2 = tx_psi_2_2 = 0
        self.tx_psi_2_1 = tx_psi_2_1 = 90
        self.tx_psi_1_3 = tx_psi_1_3 = 90
        self.tx_psi_1_2 = tx_psi_1_2 = 90
        self.tx_psi_1_1 = tx_psi_1_1 = 0
        self.tx_phi_3_3 = tx_phi_3_3 = 0
        self.tx_phi_3_2 = tx_phi_3_2 = 90
        self.tx_phi_3_1 = tx_phi_3_1 = 90
        self.tx_phi_2_3 = tx_phi_2_3 = 90
        self.tx_phi_2_2 = tx_phi_2_2 = 0
        self.tx_phi_2_1 = tx_phi_2_1 = 90
        self.tx_phi_1_3 = tx_phi_1_3 = 90
        self.tx_phi_1_2 = tx_phi_1_2 = 90
        self.tx_phi_1_1 = tx_phi_1_1 = 0
        self.tx_m = tx_m = 0.5
        self.samples_per_symbol_tx3 = samples_per_symbol_tx3 = 5
        self.samples_per_symbol_tx2 = samples_per_symbol_tx2 = 10
        self.samples_per_symbol_tx1 = samples_per_symbol_tx1 = 5
        self.samples_per_pulse_tx3 = samples_per_pulse_tx3 = 1
        self.samp_rate = samp_rate = 2.5e6
        self.rx_A = rx_A = 75e-6
        self.packet_len = packet_len = 8
        self.modulation_order_tx2 = modulation_order_tx2 = 4
        self.min_magnitude_tx3 = min_magnitude_tx3 = 2
        self.min_magnitude_tx2 = min_magnitude_tx2 = 2
        self.min_magnitude_tx1 = min_magnitude_tx1 = 2
        self.max_magnitude_tx3 = max_magnitude_tx3 = 4
        self.max_magnitude_tx2 = max_magnitude_tx2 = 4
        self.max_magnitude_tx1 = max_magnitude_tx1 = 4
        self.len_tag_key = len_tag_key = "packet_len"
        self.fft_len = fft_len = 128
        self.d_3_3 = d_3_3 = 0.1
        self.d_3_2 = d_3_2 = 100
        self.d_3_1 = d_3_1 = 100
        self.d_2_3 = d_2_3 = 100
        self.d_2_2 = d_2_2 = 0.1
        self.d_2_1 = d_2_1 = 100
        self.d_1_3 = d_1_3 = 100
        self.d_1_2 = d_1_2 = 100
        self.d_1_1 = d_1_1 = 0.1
        self.averaging_window_size = averaging_window_size = 1000
        self.average_val = average_val = threshold
        self.Minimum_value = Minimum_value = Min
        self.Maximum_value = Maximum_value = Max

        ##################################################
        # Blocks
        ##################################################
        self.minimum = blocks.probe_signal_f()
        self.maximum = blocks.probe_signal_f()
        self.average = blocks.probe_signal_f()
        def _threshold_probe():
            while True:

                val = self.average.level()
                try:
                    self.set_threshold(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _threshold_thread = threading.Thread(target=_threshold_probe)
        _threshold_thread.daemon = True
        _threshold_thread.start()

        def _Min_probe():
            while True:

                val = self.minimum.level()
                try:
                    self.set_Min(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _Min_thread = threading.Thread(target=_Min_probe)
        _Min_thread.daemon = True
        _Min_thread.start()

        def _Max_probe():
            while True:

                val = self.maximum.level()
                try:
                    self.set_Max(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _Max_thread = threading.Thread(target=_Max_probe)
        _Max_thread.daemon = True
        _Max_thread.start()

        self.owc_decimal_to_binary_mapper_0 = owc.decimal_to_binary_mapper(modulation_order_tx2)
        self.owc_binary_to_decimal_mapper_0 = owc.binary_to_decimal_mapper(modulation_order_tx2)
        self.owc_VPPM_Modulator_one_0 = owc.VPPM_Modulator_one(max_magnitude_tx3, min_magnitude_tx3, samples_per_symbol_tx3, samples_per_pulse_tx3)
        self.owc_VPPM_Demodulator_0 = owc.VPPM_Demodulator(samples_per_symbol_tx3, samples_per_pulse_tx3, 1)
        self.owc_PAM_Modulator_one_0 = owc.PAM_Modulator_one(modulation_order_tx2, max_magnitude_tx2, min_magnitude_tx2, samples_per_symbol_tx2)
        self.owc_PAM_Demodulator_0 = owc.PAM_Demodulator(modulation_order_tx2, Max, Min, samples_per_symbol_tx2)
        self.owc_OWC_Channel_relative_0 = owc.OWC_Channel_relative(3, 3, [tx_phi_1_1, tx_phi_1_2, tx_phi_1_3,  tx_phi_2_1, tx_phi_2_2, tx_phi_2_3,  tx_phi_3_1, tx_phi_3_2, tx_phi_3_3], [tx_psi_1_1, tx_psi_1_2, tx_psi_1_3, tx_psi_2_1, tx_psi_2_2, tx_psi_2_3, tx_psi_3_1, tx_psi_3_2, tx_psi_3_3], [d_1_1, d_1_2, d_1_3, d_2_1, d_2_2, d_2_3,d_3_1, d_3_2, d_3_3], [tx_m, tx_m, tx_m], [rx_A, rx_A,  rx_A], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [90, 90, 90], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0])
        self.owc_OOK_Modulator_one_0 = owc.OOK_Modulator_one(max_magnitude_tx1, min_magnitude_tx1, samples_per_symbol_tx1)
        self.owc_OOK_Demodulator_0 = owc.OOK_Demodulator(threshold, samples_per_symbol_tx1)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_uchar_to_float_1_0 = blocks.uchar_to_float()
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, window_size)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, window_size)
        self.blocks_pack_k_bits_bb_0_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_char*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(averaging_window_size, 1/averaging_window_size, 4000, 1)
        self.blocks_min_xx_0 = blocks.min_ff(window_size,1)
        self.blocks_max_xx_0 = blocks.max_ff(window_size, 1)
        self.blocks_float_to_uchar_0_0_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_sink_0_0_1 = blocks.file_sink(gr.sizeof_char*1, '/home/arsalan/OOT_Modules/gr-owc/examples/VPPM_output.txt', False)
        self.blocks_file_sink_0_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/arsalan/OOT_Modules/gr-owc/examples/PAM_output.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/arsalan/OOT_Modules/gr-owc/examples/OOK_output.txt', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self._average_val_tool_bar = Qt.QToolBar(self)

        if None:
            self._average_val_formatter = None
        else:
            self._average_val_formatter = lambda x: eng_notation.num_to_str(x)

        self._average_val_tool_bar.addWidget(Qt.QLabel('average_val' + ": "))
        self._average_val_label = Qt.QLabel(str(self._average_val_formatter(self.average_val)))
        self._average_val_tool_bar.addWidget(self._average_val_label)
        self.top_grid_layout.addWidget(self._average_val_tool_bar)
        self._Minimum_value_tool_bar = Qt.QToolBar(self)

        if None:
            self._Minimum_value_formatter = None
        else:
            self._Minimum_value_formatter = lambda x: eng_notation.num_to_str(x)

        self._Minimum_value_tool_bar.addWidget(Qt.QLabel('Minimum_value' + ": "))
        self._Minimum_value_label = Qt.QLabel(str(self._Minimum_value_formatter(self.Minimum_value)))
        self._Minimum_value_tool_bar.addWidget(self._Minimum_value_label)
        self.top_grid_layout.addWidget(self._Minimum_value_tool_bar)
        self._Maximum_value_tool_bar = Qt.QToolBar(self)

        if None:
            self._Maximum_value_formatter = None
        else:
            self._Maximum_value_formatter = lambda x: eng_notation.num_to_str(x)

        self._Maximum_value_tool_bar.addWidget(Qt.QLabel('Maximum_value' + ": "))
        self._Maximum_value_label = Qt.QLabel(str(self._Maximum_value_formatter(self.Maximum_value)))
        self._Maximum_value_tool_bar.addWidget(self._Maximum_value_label)
        self.top_grid_layout.addWidget(self._Maximum_value_tool_bar)
        self.LSK = blocks.file_source(gr.sizeof_char*1, '/home/arsalan/OOT_Modules/gr-owc/examples/TestFile.txt', True, 0, 0)
        self.LSK.set_begin_tag(pmt.PMT_NIL)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.LSK, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_uchar_0_0, 0), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.blocks_float_to_uchar_0_0_0, 0), (self.blocks_pack_k_bits_bb_0_0_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.maximum, 0))
        self.connect((self.blocks_min_xx_0, 0), (self.minimum, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.average, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_0, 0), (self.blocks_file_sink_0_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_min_xx_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_uchar_to_float_1_0, 0), (self.owc_OOK_Modulator_one_0, 0))
        self.connect((self.blocks_uchar_to_float_1_0, 0), (self.owc_VPPM_Modulator_one_0, 0))
        self.connect((self.blocks_uchar_to_float_1_0, 0), (self.owc_binary_to_decimal_mapper_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_uchar_to_float_1_0, 0))
        self.connect((self.owc_OOK_Demodulator_0, 0), (self.blocks_float_to_uchar_0_0, 0))
        self.connect((self.owc_OOK_Modulator_one_0, 0), (self.owc_OWC_Channel_relative_0, 0))
        self.connect((self.owc_OWC_Channel_relative_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.owc_OWC_Channel_relative_0, 1), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.owc_OWC_Channel_relative_0, 1), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.owc_OWC_Channel_relative_0, 0), (self.owc_OOK_Demodulator_0, 0))
        self.connect((self.owc_OWC_Channel_relative_0, 1), (self.owc_PAM_Demodulator_0, 0))
        self.connect((self.owc_OWC_Channel_relative_0, 2), (self.owc_VPPM_Demodulator_0, 0))
        self.connect((self.owc_PAM_Demodulator_0, 0), (self.owc_decimal_to_binary_mapper_0, 0))
        self.connect((self.owc_PAM_Modulator_one_0, 0), (self.owc_OWC_Channel_relative_0, 1))
        self.connect((self.owc_VPPM_Demodulator_0, 0), (self.blocks_float_to_uchar_0_0_0, 0))
        self.connect((self.owc_VPPM_Modulator_one_0, 0), (self.owc_OWC_Channel_relative_0, 2))
        self.connect((self.owc_binary_to_decimal_mapper_0, 0), (self.owc_PAM_Modulator_one_0, 0))
        self.connect((self.owc_decimal_to_binary_mapper_0, 0), (self.blocks_float_to_uchar_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "combined")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.set_average_val(self._average_val_formatter(self.threshold))
        self.owc_OOK_Demodulator_0.set_threshold(self.threshold)

    def get_Min(self):
        return self.Min

    def set_Min(self, Min):
        self.Min = Min
        self.set_Minimum_value(self._Minimum_value_formatter(self.Min))
        self.owc_PAM_Demodulator_0.set_min_magnitude(self.Min)

    def get_Max(self):
        return self.Max

    def set_Max(self, Max):
        self.Max = Max
        self.set_Maximum_value(self._Maximum_value_formatter(self.Max))
        self.owc_PAM_Demodulator_0.set_max_magnitude(self.Max)

    def get_window_size(self):
        return self.window_size

    def set_window_size(self, window_size):
        self.window_size = window_size

    def get_tx_psi_3_3(self):
        return self.tx_psi_3_3

    def set_tx_psi_3_3(self, tx_psi_3_3):
        self.tx_psi_3_3 = tx_psi_3_3
        self.owc_OWC_Channel_relative_0.set_acceptance_angle_array([self.tx_psi_1_1, self.tx_psi_1_2, self.tx_psi_1_3, self.tx_psi_2_1, self.tx_psi_2_2, self.tx_psi_2_3, self.tx_psi_3_1, self.tx_psi_3_2, self.tx_psi_3_3])

    def get_tx_psi_3_2(self):
        return self.tx_psi_3_2

    def set_tx_psi_3_2(self, tx_psi_3_2):
        self.tx_psi_3_2 = tx_psi_3_2
        self.owc_OWC_Channel_relative_0.set_acceptance_angle_array([self.tx_psi_1_1, self.tx_psi_1_2, self.tx_psi_1_3, self.tx_psi_2_1, self.tx_psi_2_2, self.tx_psi_2_3, self.tx_psi_3_1, self.tx_psi_3_2, self.tx_psi_3_3])

    def get_tx_psi_3_1(self):
        return self.tx_psi_3_1

    def set_tx_psi_3_1(self, tx_psi_3_1):
        self.tx_psi_3_1 = tx_psi_3_1
        self.owc_OWC_Channel_relative_0.set_acceptance_angle_array([self.tx_psi_1_1, self.tx_psi_1_2, self.tx_psi_1_3, self.tx_psi_2_1, self.tx_psi_2_2, self.tx_psi_2_3, self.tx_psi_3_1, self.tx_psi_3_2, self.tx_psi_3_3])

    def get_tx_psi_2_3(self):
        return self.tx_psi_2_3

    def set_tx_psi_2_3(self, tx_psi_2_3):
        self.tx_psi_2_3 = tx_psi_2_3
        self.owc_OWC_Channel_relative_0.set_acceptance_angle_array([self.tx_psi_1_1, self.tx_psi_1_2, self.tx_psi_1_3, self.tx_psi_2_1, self.tx_psi_2_2, self.tx_psi_2_3, self.tx_psi_3_1, self.tx_psi_3_2, self.tx_psi_3_3])

    def get_tx_psi_2_2(self):
        return self.tx_psi_2_2

    def set_tx_psi_2_2(self, tx_psi_2_2):
        self.tx_psi_2_2 = tx_psi_2_2
        self.owc_OWC_Channel_relative_0.set_acceptance_angle_array([self.tx_psi_1_1, self.tx_psi_1_2, self.tx_psi_1_3, self.tx_psi_2_1, self.tx_psi_2_2, self.tx_psi_2_3, self.tx_psi_3_1, self.tx_psi_3_2, self.tx_psi_3_3])

    def get_tx_psi_2_1(self):
        return self.tx_psi_2_1

    def set_tx_psi_2_1(self, tx_psi_2_1):
        self.tx_psi_2_1 = tx_psi_2_1
        self.owc_OWC_Channel_relative_0.set_acceptance_angle_array([self.tx_psi_1_1, self.tx_psi_1_2, self.tx_psi_1_3, self.tx_psi_2_1, self.tx_psi_2_2, self.tx_psi_2_3, self.tx_psi_3_1, self.tx_psi_3_2, self.tx_psi_3_3])

    def get_tx_psi_1_3(self):
        return self.tx_psi_1_3

    def set_tx_psi_1_3(self, tx_psi_1_3):
        self.tx_psi_1_3 = tx_psi_1_3
        self.owc_OWC_Channel_relative_0.set_acceptance_angle_array([self.tx_psi_1_1, self.tx_psi_1_2, self.tx_psi_1_3, self.tx_psi_2_1, self.tx_psi_2_2, self.tx_psi_2_3, self.tx_psi_3_1, self.tx_psi_3_2, self.tx_psi_3_3])

    def get_tx_psi_1_2(self):
        return self.tx_psi_1_2

    def set_tx_psi_1_2(self, tx_psi_1_2):
        self.tx_psi_1_2 = tx_psi_1_2
        self.owc_OWC_Channel_relative_0.set_acceptance_angle_array([self.tx_psi_1_1, self.tx_psi_1_2, self.tx_psi_1_3, self.tx_psi_2_1, self.tx_psi_2_2, self.tx_psi_2_3, self.tx_psi_3_1, self.tx_psi_3_2, self.tx_psi_3_3])

    def get_tx_psi_1_1(self):
        return self.tx_psi_1_1

    def set_tx_psi_1_1(self, tx_psi_1_1):
        self.tx_psi_1_1 = tx_psi_1_1
        self.owc_OWC_Channel_relative_0.set_acceptance_angle_array([self.tx_psi_1_1, self.tx_psi_1_2, self.tx_psi_1_3, self.tx_psi_2_1, self.tx_psi_2_2, self.tx_psi_2_3, self.tx_psi_3_1, self.tx_psi_3_2, self.tx_psi_3_3])

    def get_tx_phi_3_3(self):
        return self.tx_phi_3_3

    def set_tx_phi_3_3(self, tx_phi_3_3):
        self.tx_phi_3_3 = tx_phi_3_3
        self.owc_OWC_Channel_relative_0.set_emission_angle_array([self.tx_phi_1_1, self.tx_phi_1_2, self.tx_phi_1_3,  self.tx_phi_2_1, self.tx_phi_2_2, self.tx_phi_2_3,  self.tx_phi_3_1, self.tx_phi_3_2, self.tx_phi_3_3])

    def get_tx_phi_3_2(self):
        return self.tx_phi_3_2

    def set_tx_phi_3_2(self, tx_phi_3_2):
        self.tx_phi_3_2 = tx_phi_3_2
        self.owc_OWC_Channel_relative_0.set_emission_angle_array([self.tx_phi_1_1, self.tx_phi_1_2, self.tx_phi_1_3,  self.tx_phi_2_1, self.tx_phi_2_2, self.tx_phi_2_3,  self.tx_phi_3_1, self.tx_phi_3_2, self.tx_phi_3_3])

    def get_tx_phi_3_1(self):
        return self.tx_phi_3_1

    def set_tx_phi_3_1(self, tx_phi_3_1):
        self.tx_phi_3_1 = tx_phi_3_1
        self.owc_OWC_Channel_relative_0.set_emission_angle_array([self.tx_phi_1_1, self.tx_phi_1_2, self.tx_phi_1_3,  self.tx_phi_2_1, self.tx_phi_2_2, self.tx_phi_2_3,  self.tx_phi_3_1, self.tx_phi_3_2, self.tx_phi_3_3])

    def get_tx_phi_2_3(self):
        return self.tx_phi_2_3

    def set_tx_phi_2_3(self, tx_phi_2_3):
        self.tx_phi_2_3 = tx_phi_2_3
        self.owc_OWC_Channel_relative_0.set_emission_angle_array([self.tx_phi_1_1, self.tx_phi_1_2, self.tx_phi_1_3,  self.tx_phi_2_1, self.tx_phi_2_2, self.tx_phi_2_3,  self.tx_phi_3_1, self.tx_phi_3_2, self.tx_phi_3_3])

    def get_tx_phi_2_2(self):
        return self.tx_phi_2_2

    def set_tx_phi_2_2(self, tx_phi_2_2):
        self.tx_phi_2_2 = tx_phi_2_2
        self.owc_OWC_Channel_relative_0.set_emission_angle_array([self.tx_phi_1_1, self.tx_phi_1_2, self.tx_phi_1_3,  self.tx_phi_2_1, self.tx_phi_2_2, self.tx_phi_2_3,  self.tx_phi_3_1, self.tx_phi_3_2, self.tx_phi_3_3])

    def get_tx_phi_2_1(self):
        return self.tx_phi_2_1

    def set_tx_phi_2_1(self, tx_phi_2_1):
        self.tx_phi_2_1 = tx_phi_2_1
        self.owc_OWC_Channel_relative_0.set_emission_angle_array([self.tx_phi_1_1, self.tx_phi_1_2, self.tx_phi_1_3,  self.tx_phi_2_1, self.tx_phi_2_2, self.tx_phi_2_3,  self.tx_phi_3_1, self.tx_phi_3_2, self.tx_phi_3_3])

    def get_tx_phi_1_3(self):
        return self.tx_phi_1_3

    def set_tx_phi_1_3(self, tx_phi_1_3):
        self.tx_phi_1_3 = tx_phi_1_3
        self.owc_OWC_Channel_relative_0.set_emission_angle_array([self.tx_phi_1_1, self.tx_phi_1_2, self.tx_phi_1_3,  self.tx_phi_2_1, self.tx_phi_2_2, self.tx_phi_2_3,  self.tx_phi_3_1, self.tx_phi_3_2, self.tx_phi_3_3])

    def get_tx_phi_1_2(self):
        return self.tx_phi_1_2

    def set_tx_phi_1_2(self, tx_phi_1_2):
        self.tx_phi_1_2 = tx_phi_1_2
        self.owc_OWC_Channel_relative_0.set_emission_angle_array([self.tx_phi_1_1, self.tx_phi_1_2, self.tx_phi_1_3,  self.tx_phi_2_1, self.tx_phi_2_2, self.tx_phi_2_3,  self.tx_phi_3_1, self.tx_phi_3_2, self.tx_phi_3_3])

    def get_tx_phi_1_1(self):
        return self.tx_phi_1_1

    def set_tx_phi_1_1(self, tx_phi_1_1):
        self.tx_phi_1_1 = tx_phi_1_1
        self.owc_OWC_Channel_relative_0.set_emission_angle_array([self.tx_phi_1_1, self.tx_phi_1_2, self.tx_phi_1_3,  self.tx_phi_2_1, self.tx_phi_2_2, self.tx_phi_2_3,  self.tx_phi_3_1, self.tx_phi_3_2, self.tx_phi_3_3])

    def get_tx_m(self):
        return self.tx_m

    def set_tx_m(self, tx_m):
        self.tx_m = tx_m
        self.owc_OWC_Channel_relative_0.set_lambertian_order_array([self.tx_m, self.tx_m, self.tx_m])

    def get_samples_per_symbol_tx3(self):
        return self.samples_per_symbol_tx3

    def set_samples_per_symbol_tx3(self, samples_per_symbol_tx3):
        self.samples_per_symbol_tx3 = samples_per_symbol_tx3

    def get_samples_per_symbol_tx2(self):
        return self.samples_per_symbol_tx2

    def set_samples_per_symbol_tx2(self, samples_per_symbol_tx2):
        self.samples_per_symbol_tx2 = samples_per_symbol_tx2

    def get_samples_per_symbol_tx1(self):
        return self.samples_per_symbol_tx1

    def set_samples_per_symbol_tx1(self, samples_per_symbol_tx1):
        self.samples_per_symbol_tx1 = samples_per_symbol_tx1

    def get_samples_per_pulse_tx3(self):
        return self.samples_per_pulse_tx3

    def set_samples_per_pulse_tx3(self, samples_per_pulse_tx3):
        self.samples_per_pulse_tx3 = samples_per_pulse_tx3

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_rx_A(self):
        return self.rx_A

    def set_rx_A(self, rx_A):
        self.rx_A = rx_A

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_modulation_order_tx2(self):
        return self.modulation_order_tx2

    def set_modulation_order_tx2(self, modulation_order_tx2):
        self.modulation_order_tx2 = modulation_order_tx2

    def get_min_magnitude_tx3(self):
        return self.min_magnitude_tx3

    def set_min_magnitude_tx3(self, min_magnitude_tx3):
        self.min_magnitude_tx3 = min_magnitude_tx3
        self.owc_VPPM_Modulator_one_0.set_min_magnitude(self.min_magnitude_tx3)

    def get_min_magnitude_tx2(self):
        return self.min_magnitude_tx2

    def set_min_magnitude_tx2(self, min_magnitude_tx2):
        self.min_magnitude_tx2 = min_magnitude_tx2
        self.owc_PAM_Modulator_one_0.set_min_magnitude(self.min_magnitude_tx2)

    def get_min_magnitude_tx1(self):
        return self.min_magnitude_tx1

    def set_min_magnitude_tx1(self, min_magnitude_tx1):
        self.min_magnitude_tx1 = min_magnitude_tx1
        self.owc_OOK_Modulator_one_0.set_min_magnitude(self.min_magnitude_tx1)

    def get_max_magnitude_tx3(self):
        return self.max_magnitude_tx3

    def set_max_magnitude_tx3(self, max_magnitude_tx3):
        self.max_magnitude_tx3 = max_magnitude_tx3
        self.owc_VPPM_Modulator_one_0.set_max_magnitude(self.max_magnitude_tx3)

    def get_max_magnitude_tx2(self):
        return self.max_magnitude_tx2

    def set_max_magnitude_tx2(self, max_magnitude_tx2):
        self.max_magnitude_tx2 = max_magnitude_tx2
        self.owc_PAM_Modulator_one_0.set_max_magnitude(self.max_magnitude_tx2)

    def get_max_magnitude_tx1(self):
        return self.max_magnitude_tx1

    def set_max_magnitude_tx1(self, max_magnitude_tx1):
        self.max_magnitude_tx1 = max_magnitude_tx1
        self.owc_OOK_Modulator_one_0.set_max_magnitude(self.max_magnitude_tx1)

    def get_len_tag_key(self):
        return self.len_tag_key

    def set_len_tag_key(self, len_tag_key):
        self.len_tag_key = len_tag_key

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len

    def get_d_3_3(self):
        return self.d_3_3

    def set_d_3_3(self, d_3_3):
        self.d_3_3 = d_3_3
        self.owc_OWC_Channel_relative_0.set_distance_array([self.d_1_1, self.d_1_2, self.d_1_3, self.d_2_1, self.d_2_2, self.d_2_3,self.d_3_1, self.d_3_2, self.d_3_3])

    def get_d_3_2(self):
        return self.d_3_2

    def set_d_3_2(self, d_3_2):
        self.d_3_2 = d_3_2
        self.owc_OWC_Channel_relative_0.set_distance_array([self.d_1_1, self.d_1_2, self.d_1_3, self.d_2_1, self.d_2_2, self.d_2_3,self.d_3_1, self.d_3_2, self.d_3_3])

    def get_d_3_1(self):
        return self.d_3_1

    def set_d_3_1(self, d_3_1):
        self.d_3_1 = d_3_1
        self.owc_OWC_Channel_relative_0.set_distance_array([self.d_1_1, self.d_1_2, self.d_1_3, self.d_2_1, self.d_2_2, self.d_2_3,self.d_3_1, self.d_3_2, self.d_3_3])

    def get_d_2_3(self):
        return self.d_2_3

    def set_d_2_3(self, d_2_3):
        self.d_2_3 = d_2_3
        self.owc_OWC_Channel_relative_0.set_distance_array([self.d_1_1, self.d_1_2, self.d_1_3, self.d_2_1, self.d_2_2, self.d_2_3,self.d_3_1, self.d_3_2, self.d_3_3])

    def get_d_2_2(self):
        return self.d_2_2

    def set_d_2_2(self, d_2_2):
        self.d_2_2 = d_2_2
        self.owc_OWC_Channel_relative_0.set_distance_array([self.d_1_1, self.d_1_2, self.d_1_3, self.d_2_1, self.d_2_2, self.d_2_3,self.d_3_1, self.d_3_2, self.d_3_3])

    def get_d_2_1(self):
        return self.d_2_1

    def set_d_2_1(self, d_2_1):
        self.d_2_1 = d_2_1
        self.owc_OWC_Channel_relative_0.set_distance_array([self.d_1_1, self.d_1_2, self.d_1_3, self.d_2_1, self.d_2_2, self.d_2_3,self.d_3_1, self.d_3_2, self.d_3_3])

    def get_d_1_3(self):
        return self.d_1_3

    def set_d_1_3(self, d_1_3):
        self.d_1_3 = d_1_3
        self.owc_OWC_Channel_relative_0.set_distance_array([self.d_1_1, self.d_1_2, self.d_1_3, self.d_2_1, self.d_2_2, self.d_2_3,self.d_3_1, self.d_3_2, self.d_3_3])

    def get_d_1_2(self):
        return self.d_1_2

    def set_d_1_2(self, d_1_2):
        self.d_1_2 = d_1_2
        self.owc_OWC_Channel_relative_0.set_distance_array([self.d_1_1, self.d_1_2, self.d_1_3, self.d_2_1, self.d_2_2, self.d_2_3,self.d_3_1, self.d_3_2, self.d_3_3])

    def get_d_1_1(self):
        return self.d_1_1

    def set_d_1_1(self, d_1_1):
        self.d_1_1 = d_1_1
        self.owc_OWC_Channel_relative_0.set_distance_array([self.d_1_1, self.d_1_2, self.d_1_3, self.d_2_1, self.d_2_2, self.d_2_3,self.d_3_1, self.d_3_2, self.d_3_3])

    def get_averaging_window_size(self):
        return self.averaging_window_size

    def set_averaging_window_size(self, averaging_window_size):
        self.averaging_window_size = averaging_window_size
        self.blocks_moving_average_xx_0.set_length_and_scale(self.averaging_window_size, 1/self.averaging_window_size)

    def get_average_val(self):
        return self.average_val

    def set_average_val(self, average_val):
        self.average_val = average_val
        Qt.QMetaObject.invokeMethod(self._average_val_label, "setText", Qt.Q_ARG("QString", self.average_val))

    def get_Minimum_value(self):
        return self.Minimum_value

    def set_Minimum_value(self, Minimum_value):
        self.Minimum_value = Minimum_value
        Qt.QMetaObject.invokeMethod(self._Minimum_value_label, "setText", Qt.Q_ARG("QString", self.Minimum_value))

    def get_Maximum_value(self):
        return self.Maximum_value

    def set_Maximum_value(self, Maximum_value):
        self.Maximum_value = Maximum_value
        Qt.QMetaObject.invokeMethod(self._Maximum_value_label, "setText", Qt.Q_ARG("QString", self.Maximum_value))





def main(top_block_cls=combined, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
