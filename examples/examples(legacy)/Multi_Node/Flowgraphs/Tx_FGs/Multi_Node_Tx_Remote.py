#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Multi-node transmitter with remote control
# Author: UCanLab
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
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
from xmlrpc.server import SimpleXMLRPCServer
import threading



from gnuradio import qtgui

class Multi_Node_Tx_Remote(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Multi-node transmitter with remote control", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Multi-node transmitter with remote control")
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

        self.settings = Qt.QSettings("GNU Radio", "Multi_Node_Tx_Remote")

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
        self.sig_freq_2 = sig_freq_2 = 500000
        self.sig_freq_1 = sig_freq_1 = 1000000
        self.samp_rate = samp_rate = 5000000
        self.scale = scale = 0.5
        self.path_select_2 = path_select_2 = 0
        self.path_select_1 = path_select_1 = 0
        self.interp_2 = interp_2 = int(samp_rate/sig_freq_2)
        self.interp_1 = interp_1 = int(samp_rate/sig_freq_1)

        ##################################################
        # Blocks
        ##################################################
        self._sig_freq_2_range = Range(500000, 2000000, 500000, 500000, 200)
        self._sig_freq_2_win = RangeWidget(self._sig_freq_2_range, self.set_sig_freq_2, "Signal Frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._sig_freq_2_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._sig_freq_1_range = Range(500000, 2000000, 500000, 1000000, 200)
        self._sig_freq_1_win = RangeWidget(self._sig_freq_1_range, self.set_sig_freq_1, "Signal Frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._sig_freq_1_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._path_select_2_options = [0, 1, 2]
        # Create the labels list
        self._path_select_2_labels = ['Signal', 'Tone', 'OFF']
        # Create the combo box
        self._path_select_2_tool_bar = Qt.QToolBar(self)
        self._path_select_2_tool_bar.addWidget(Qt.QLabel("Source Signal" + ": "))
        self._path_select_2_combo_box = Qt.QComboBox()
        self._path_select_2_tool_bar.addWidget(self._path_select_2_combo_box)
        for _label in self._path_select_2_labels: self._path_select_2_combo_box.addItem(_label)
        self._path_select_2_callback = lambda i: Qt.QMetaObject.invokeMethod(self._path_select_2_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._path_select_2_options.index(i)))
        self._path_select_2_callback(self.path_select_2)
        self._path_select_2_combo_box.currentIndexChanged.connect(
            lambda i: self.set_path_select_2(self._path_select_2_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._path_select_2_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._path_select_1_options = [0, 1, 2]
        # Create the labels list
        self._path_select_1_labels = ['Signal', 'Tone', 'OFF']
        # Create the combo box
        self._path_select_1_tool_bar = Qt.QToolBar(self)
        self._path_select_1_tool_bar.addWidget(Qt.QLabel("Source Signal" + ": "))
        self._path_select_1_combo_box = Qt.QComboBox()
        self._path_select_1_tool_bar.addWidget(self._path_select_1_combo_box)
        for _label in self._path_select_1_labels: self._path_select_1_combo_box.addItem(_label)
        self._path_select_1_callback = lambda i: Qt.QMetaObject.invokeMethod(self._path_select_1_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._path_select_1_options.index(i)))
        self._path_select_1_callback(self.path_select_1)
        self._path_select_1_combo_box.currentIndexChanged.connect(
            lambda i: self.set_path_select_1(self._path_select_1_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._path_select_1_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.xmlrpc_server_0 = SimpleXMLRPCServer(('10.1.1.2', 8080), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            '',
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        # No synchronization enforced.

        self.uhd_usrp_sink_0.set_center_freq(0, 0)
        self.uhd_usrp_sink_0.set_antenna('AB', 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self.blocks_selector_0_0 = blocks.selector(gr.sizeof_float*1,path_select_2,0)
        self.blocks_selector_0_0.set_enabled(True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_float*1,path_select_1,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_float*1, interp_2)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, interp_1)
        self.blocks_null_source_0_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_int_to_float_0_0 = blocks.int_to_float(1, 1/scale)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1/scale)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_add_const_vxx_1_0 = blocks.add_const_ff(-(scale/2))
        self.blocks_add_const_vxx_1 = blocks.add_const_ff(-(scale/2))
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sig_freq_2, 0.5, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sig_freq_1, 0.5, 0, 0)
        self.analog_random_source_x_0_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 2, 1000))), True)
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 2, 1000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.analog_random_source_x_0_0, 0), (self.blocks_int_to_float_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_selector_0_0, 1))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_selector_0, 0))
        self.connect((self.blocks_add_const_vxx_1_0, 0), (self.blocks_selector_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_int_to_float_0_0, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0, 2))
        self.connect((self.blocks_null_source_0_0, 0), (self.blocks_selector_0_0, 2))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_add_const_vxx_1, 0))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_add_const_vxx_1_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_selector_0_0, 0), (self.blocks_float_to_complex_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Multi_Node_Tx_Remote")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sig_freq_2(self):
        return self.sig_freq_2

    def set_sig_freq_2(self, sig_freq_2):
        self.sig_freq_2 = sig_freq_2
        self.set_interp_2(int(self.samp_rate/self.sig_freq_2))
        self.analog_sig_source_x_0_0.set_frequency(self.sig_freq_2)

    def get_sig_freq_1(self):
        return self.sig_freq_1

    def set_sig_freq_1(self, sig_freq_1):
        self.sig_freq_1 = sig_freq_1
        self.set_interp_1(int(self.samp_rate/self.sig_freq_1))
        self.analog_sig_source_x_0.set_frequency(self.sig_freq_1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_interp_1(int(self.samp_rate/self.sig_freq_1))
        self.set_interp_2(int(self.samp_rate/self.sig_freq_2))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale
        self.blocks_add_const_vxx_1.set_k(-(self.scale/2))
        self.blocks_add_const_vxx_1_0.set_k(-(self.scale/2))
        self.blocks_int_to_float_0.set_scale(1/self.scale)
        self.blocks_int_to_float_0_0.set_scale(1/self.scale)

    def get_path_select_2(self):
        return self.path_select_2

    def set_path_select_2(self, path_select_2):
        self.path_select_2 = path_select_2
        self._path_select_2_callback(self.path_select_2)
        self.blocks_selector_0_0.set_input_index(self.path_select_2)

    def get_path_select_1(self):
        return self.path_select_1

    def set_path_select_1(self, path_select_1):
        self.path_select_1 = path_select_1
        self._path_select_1_callback(self.path_select_1)
        self.blocks_selector_0.set_input_index(self.path_select_1)

    def get_interp_2(self):
        return self.interp_2

    def set_interp_2(self, interp_2):
        self.interp_2 = interp_2
        self.blocks_repeat_0_0.set_interpolation(self.interp_2)

    def get_interp_1(self):
        return self.interp_1

    def set_interp_1(self, interp_1):
        self.interp_1 = interp_1
        self.blocks_repeat_0.set_interpolation(self.interp_1)




def main(top_block_cls=Multi_Node_Tx_Remote, options=None):

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
