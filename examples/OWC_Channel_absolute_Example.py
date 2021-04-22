#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Example of the absolute channel model
# Author: Arsalan Ahmed
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
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import owc

from gnuradio import qtgui

class OWC_Channel_absolute_Example(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Example of the absolute channel model")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Example of the absolute channel model")
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

        self.settings = Qt.QSettings("GNU Radio", "OWC_Channel_absolute_Example")

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
        self.tx_z_2 = tx_z_2 = 0
        self.tx_z_1 = tx_z_1 = 0
        self.tx_y_2 = tx_y_2 = 0
        self.tx_y_1 = tx_y_1 = 0
        self.tx_x_2 = tx_x_2 = 5
        self.tx_x_1 = tx_x_1 = 0
        self.tx_u_z_2 = tx_u_z_2 = 1
        self.tx_u_z_1 = tx_u_z_1 = 1
        self.tx_u_y_2 = tx_u_y_2 = 0
        self.tx_u_y_1 = tx_u_y_1 = 0
        self.tx_u_x_2 = tx_u_x_2 = 0
        self.tx_u_x_1 = tx_u_x_1 = 0
        self.tx_m_2 = tx_m_2 = 0.5
        self.tx_m_1 = tx_m_1 = 0.5
        self.tx_C_t_2 = tx_C_t_2 = 1
        self.tx_C_t_1 = tx_C_t_1 = 1
        self.samp_rate = samp_rate = 100000
        self.rx_z_2 = rx_z_2 = 1
        self.rx_z_1 = rx_z_1 = 1
        self.rx_y_2 = rx_y_2 = 0
        self.rx_y_1 = rx_y_1 = 0
        self.rx_x_2 = rx_x_2 = 5
        self.rx_x_1 = rx_x_1 = 0
        self.rx_u_z_2 = rx_u_z_2 = -1
        self.rx_u_z_1 = rx_u_z_1 = -1
        self.rx_u_y_2 = rx_u_y_2 = 0
        self.rx_u_y_1 = rx_u_y_1 = 0
        self.rx_u_x_2 = rx_u_x_2 = 0
        self.rx_u_x_1 = rx_u_x_1 = 0
        self.rx_psi_c_2 = rx_psi_c_2 = 90
        self.rx_psi_c_1 = rx_psi_c_1 = 90
        self.rx_n_2 = rx_n_2 = 1
        self.rx_n_1 = rx_n_1 = 1
        self.rx_Ts_2 = rx_Ts_2 = 1
        self.rx_Ts_1 = rx_Ts_1 = 1
        self.rx_C_r_2 = rx_C_r_2 = 1
        self.rx_C_r_1 = rx_C_r_1 = 1
        self.rx_A_2 = rx_A_2 = 1e-6
        self.rx_A_1 = rx_A_1 = 1e-6

        ##################################################
        # Blocks
        ##################################################
        self._tx_z_2_range = Range(0, 10, 0.1, 0, 200)
        self._tx_z_2_win = RangeWidget(self._tx_z_2_range, self.set_tx_z_2, 'tx_z_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_z_2_win)
        self._tx_z_1_range = Range(0, 10, 0.1, 0, 200)
        self._tx_z_1_win = RangeWidget(self._tx_z_1_range, self.set_tx_z_1, 'tx_z_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_z_1_win)
        self._tx_y_2_range = Range(0, 10, 0.1, 0, 200)
        self._tx_y_2_win = RangeWidget(self._tx_y_2_range, self.set_tx_y_2, 'tx_y_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_y_2_win)
        self._tx_y_1_range = Range(0, 10, 0.1, 0, 200)
        self._tx_y_1_win = RangeWidget(self._tx_y_1_range, self.set_tx_y_1, 'tx_y_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_y_1_win)
        self._tx_x_2_range = Range(0, 10, 0.1, 5, 200)
        self._tx_x_2_win = RangeWidget(self._tx_x_2_range, self.set_tx_x_2, 'tx_x_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_x_2_win)
        self._tx_x_1_range = Range(0, 10, 0.1, 0, 200)
        self._tx_x_1_win = RangeWidget(self._tx_x_1_range, self.set_tx_x_1, 'tx_x_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_x_1_win)
        self._tx_u_z_2_range = Range(-1, 1, 0.01, 1, 200)
        self._tx_u_z_2_win = RangeWidget(self._tx_u_z_2_range, self.set_tx_u_z_2, 'tx_u_z_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_u_z_2_win)
        self._tx_u_z_1_range = Range(-1, 1, 0.01, 1, 200)
        self._tx_u_z_1_win = RangeWidget(self._tx_u_z_1_range, self.set_tx_u_z_1, 'tx_u_z_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_u_z_1_win)
        self._tx_u_y_2_range = Range(-1, 1, 0.01, 0, 200)
        self._tx_u_y_2_win = RangeWidget(self._tx_u_y_2_range, self.set_tx_u_y_2, 'tx_u_y_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_u_y_2_win)
        self._tx_u_y_1_range = Range(-1, 1, 0.01, 0, 200)
        self._tx_u_y_1_win = RangeWidget(self._tx_u_y_1_range, self.set_tx_u_y_1, 'tx_u_y_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_u_y_1_win)
        self._tx_u_x_2_range = Range(-1, 1, 0.01, 0, 200)
        self._tx_u_x_2_win = RangeWidget(self._tx_u_x_2_range, self.set_tx_u_x_2, 'tx_u_x_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_u_x_2_win)
        self._tx_u_x_1_range = Range(-1, 1, 0.01, 0, 200)
        self._tx_u_x_1_win = RangeWidget(self._tx_u_x_1_range, self.set_tx_u_x_1, 'tx_u_x_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_u_x_1_win)
        self._rx_z_2_range = Range(0, 10, 0.1, 1, 200)
        self._rx_z_2_win = RangeWidget(self._rx_z_2_range, self.set_rx_z_2, 'rx_z_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_z_2_win)
        self._rx_z_1_range = Range(0, 10, 0.1, 1, 200)
        self._rx_z_1_win = RangeWidget(self._rx_z_1_range, self.set_rx_z_1, 'rx_z_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_z_1_win)
        self._rx_y_2_range = Range(0, 10, 0.1, 0, 200)
        self._rx_y_2_win = RangeWidget(self._rx_y_2_range, self.set_rx_y_2, 'rx_y_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_y_2_win)
        self._rx_y_1_range = Range(0, 10, 0.1, 0, 200)
        self._rx_y_1_win = RangeWidget(self._rx_y_1_range, self.set_rx_y_1, 'rx_y_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_y_1_win)
        self._rx_x_2_range = Range(0, 10, 0.1, 5, 200)
        self._rx_x_2_win = RangeWidget(self._rx_x_2_range, self.set_rx_x_2, 'rx_x_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_x_2_win)
        self._rx_x_1_range = Range(0, 10, 0.1, 0, 200)
        self._rx_x_1_win = RangeWidget(self._rx_x_1_range, self.set_rx_x_1, 'rx_x_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_x_1_win)
        self._rx_u_z_2_range = Range(-1, 1, 0.01, -1, 200)
        self._rx_u_z_2_win = RangeWidget(self._rx_u_z_2_range, self.set_rx_u_z_2, 'rx_u_z_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_u_z_2_win)
        self._rx_u_z_1_range = Range(-1, 1, 0.01, -1, 200)
        self._rx_u_z_1_win = RangeWidget(self._rx_u_z_1_range, self.set_rx_u_z_1, 'rx_u_z_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_u_z_1_win)
        self._rx_u_y_2_range = Range(-1, 1, 0.01, 0, 200)
        self._rx_u_y_2_win = RangeWidget(self._rx_u_y_2_range, self.set_rx_u_y_2, 'rx_u_y_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_u_y_2_win)
        self._rx_u_y_1_range = Range(-1, 1, 0.01, 0, 200)
        self._rx_u_y_1_win = RangeWidget(self._rx_u_y_1_range, self.set_rx_u_y_1, 'rx_u_y_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_u_y_1_win)
        self._rx_u_x_2_range = Range(-1, 1, 0.01, 0, 200)
        self._rx_u_x_2_win = RangeWidget(self._rx_u_x_2_range, self.set_rx_u_x_2, 'rx_u_x_2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_u_x_2_win)
        self._rx_u_x_1_range = Range(-1, 1, 0.01, 0, 200)
        self._rx_u_x_1_win = RangeWidget(self._rx_u_x_1_range, self.set_rx_u_x_1, 'rx_u_x_1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_u_x_1_win)
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "Tx 2", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['green', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "Tx 1", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['red', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "Rx 2", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "Rx 1", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Rx 2 Frequency Domain", #name
            1
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)


        self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["yellow", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Rx 1 Frequency Domain", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            "Rx XY location coordinates", #name
            2 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-10, 10)
        self.qtgui_const_sink_x_0_0.set_x_axis(-10, 10)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["green", "black", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "Tx XY location coordinates", #name
            2 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-10, 10)
        self.qtgui_const_sink_x_0.set_x_axis(-10, 10)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.owc_OWC_Channel_absolute_0 = owc.OWC_Channel_absolute(2, 2, [tx_x_1, tx_y_1, tx_z_1 , tx_x_2, tx_y_2, tx_z_2], [tx_u_x_1, tx_u_y_1, tx_u_z_1 , tx_u_x_2, tx_u_y_2, tx_u_z_2], [rx_x_1, rx_y_1, rx_z_1 , rx_x_2, rx_y_2, rx_z_2], [rx_u_x_1, rx_u_y_1, rx_u_z_1 , rx_u_x_2, rx_u_y_2, rx_u_z_2], [tx_m_1, tx_m_2], [rx_A_1, rx_A_2], [rx_Ts_1, rx_Ts_2], [rx_n_1, rx_n_2], [rx_psi_c_1, rx_psi_c_2], [tx_C_t_1, tx_C_t_2], [rx_C_r_1, rx_C_r_2])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_float_to_complex_0_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 1e3, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 10e3, 1, 0, 0)
        self.analog_const_source_x_0_2 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, rx_y_1)
        self.analog_const_source_x_0_1_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, rx_y_2)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, tx_y_2)
        self.analog_const_source_x_0_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, rx_x_1)
        self.analog_const_source_x_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, rx_x_2)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, tx_x_2)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, tx_x_1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, tx_y_1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.analog_const_source_x_0_0_0_0, 0), (self.blocks_float_to_complex_0_0_0_0, 0))
        self.connect((self.analog_const_source_x_0_0_1, 0), (self.blocks_float_to_complex_0_0_0, 0))
        self.connect((self.analog_const_source_x_0_1, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.analog_const_source_x_0_1_0, 0), (self.blocks_float_to_complex_0_0_0_0, 1))
        self.connect((self.analog_const_source_x_0_2, 0), (self.blocks_float_to_complex_0_0_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.owc_OWC_Channel_absolute_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.qtgui_const_sink_x_0, 1))
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.blocks_float_to_complex_0_0_0_0, 0), (self.qtgui_const_sink_x_0_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.owc_OWC_Channel_absolute_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.owc_OWC_Channel_absolute_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.owc_OWC_Channel_absolute_0, 1), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.owc_OWC_Channel_absolute_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.owc_OWC_Channel_absolute_0, 1), (self.qtgui_time_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "OWC_Channel_absolute_Example")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tx_z_2(self):
        return self.tx_z_2

    def set_tx_z_2(self, tx_z_2):
        self.tx_z_2 = tx_z_2
        self.owc_OWC_Channel_absolute_0.set_tx_coordinates_array([self.tx_x_1, self.tx_y_1, self.tx_z_1 , self.tx_x_2, self.tx_y_2, self.tx_z_2])

    def get_tx_z_1(self):
        return self.tx_z_1

    def set_tx_z_1(self, tx_z_1):
        self.tx_z_1 = tx_z_1
        self.owc_OWC_Channel_absolute_0.set_tx_coordinates_array([self.tx_x_1, self.tx_y_1, self.tx_z_1 , self.tx_x_2, self.tx_y_2, self.tx_z_2])

    def get_tx_y_2(self):
        return self.tx_y_2

    def set_tx_y_2(self, tx_y_2):
        self.tx_y_2 = tx_y_2
        self.analog_const_source_x_0_1.set_offset(self.tx_y_2)
        self.owc_OWC_Channel_absolute_0.set_tx_coordinates_array([self.tx_x_1, self.tx_y_1, self.tx_z_1 , self.tx_x_2, self.tx_y_2, self.tx_z_2])

    def get_tx_y_1(self):
        return self.tx_y_1

    def set_tx_y_1(self, tx_y_1):
        self.tx_y_1 = tx_y_1
        self.analog_const_source_x_0.set_offset(self.tx_y_1)
        self.owc_OWC_Channel_absolute_0.set_tx_coordinates_array([self.tx_x_1, self.tx_y_1, self.tx_z_1 , self.tx_x_2, self.tx_y_2, self.tx_z_2])

    def get_tx_x_2(self):
        return self.tx_x_2

    def set_tx_x_2(self, tx_x_2):
        self.tx_x_2 = tx_x_2
        self.analog_const_source_x_0_0_0.set_offset(self.tx_x_2)
        self.owc_OWC_Channel_absolute_0.set_tx_coordinates_array([self.tx_x_1, self.tx_y_1, self.tx_z_1 , self.tx_x_2, self.tx_y_2, self.tx_z_2])

    def get_tx_x_1(self):
        return self.tx_x_1

    def set_tx_x_1(self, tx_x_1):
        self.tx_x_1 = tx_x_1
        self.analog_const_source_x_0_0.set_offset(self.tx_x_1)
        self.owc_OWC_Channel_absolute_0.set_tx_coordinates_array([self.tx_x_1, self.tx_y_1, self.tx_z_1 , self.tx_x_2, self.tx_y_2, self.tx_z_2])

    def get_tx_u_z_2(self):
        return self.tx_u_z_2

    def set_tx_u_z_2(self, tx_u_z_2):
        self.tx_u_z_2 = tx_u_z_2
        self.owc_OWC_Channel_absolute_0.set_tx_orientation_array([self.tx_u_x_1, self.tx_u_y_1, self.tx_u_z_1 , self.tx_u_x_2, self.tx_u_y_2, self.tx_u_z_2])

    def get_tx_u_z_1(self):
        return self.tx_u_z_1

    def set_tx_u_z_1(self, tx_u_z_1):
        self.tx_u_z_1 = tx_u_z_1
        self.owc_OWC_Channel_absolute_0.set_tx_orientation_array([self.tx_u_x_1, self.tx_u_y_1, self.tx_u_z_1 , self.tx_u_x_2, self.tx_u_y_2, self.tx_u_z_2])

    def get_tx_u_y_2(self):
        return self.tx_u_y_2

    def set_tx_u_y_2(self, tx_u_y_2):
        self.tx_u_y_2 = tx_u_y_2
        self.owc_OWC_Channel_absolute_0.set_tx_orientation_array([self.tx_u_x_1, self.tx_u_y_1, self.tx_u_z_1 , self.tx_u_x_2, self.tx_u_y_2, self.tx_u_z_2])

    def get_tx_u_y_1(self):
        return self.tx_u_y_1

    def set_tx_u_y_1(self, tx_u_y_1):
        self.tx_u_y_1 = tx_u_y_1
        self.owc_OWC_Channel_absolute_0.set_tx_orientation_array([self.tx_u_x_1, self.tx_u_y_1, self.tx_u_z_1 , self.tx_u_x_2, self.tx_u_y_2, self.tx_u_z_2])

    def get_tx_u_x_2(self):
        return self.tx_u_x_2

    def set_tx_u_x_2(self, tx_u_x_2):
        self.tx_u_x_2 = tx_u_x_2
        self.owc_OWC_Channel_absolute_0.set_tx_orientation_array([self.tx_u_x_1, self.tx_u_y_1, self.tx_u_z_1 , self.tx_u_x_2, self.tx_u_y_2, self.tx_u_z_2])

    def get_tx_u_x_1(self):
        return self.tx_u_x_1

    def set_tx_u_x_1(self, tx_u_x_1):
        self.tx_u_x_1 = tx_u_x_1
        self.owc_OWC_Channel_absolute_0.set_tx_orientation_array([self.tx_u_x_1, self.tx_u_y_1, self.tx_u_z_1 , self.tx_u_x_2, self.tx_u_y_2, self.tx_u_z_2])

    def get_tx_m_2(self):
        return self.tx_m_2

    def set_tx_m_2(self, tx_m_2):
        self.tx_m_2 = tx_m_2

    def get_tx_m_1(self):
        return self.tx_m_1

    def set_tx_m_1(self, tx_m_1):
        self.tx_m_1 = tx_m_1

    def get_tx_C_t_2(self):
        return self.tx_C_t_2

    def set_tx_C_t_2(self, tx_C_t_2):
        self.tx_C_t_2 = tx_C_t_2

    def get_tx_C_t_1(self):
        return self.tx_C_t_1

    def set_tx_C_t_1(self, tx_C_t_1):
        self.tx_C_t_1 = tx_C_t_1

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.samp_rate)

    def get_rx_z_2(self):
        return self.rx_z_2

    def set_rx_z_2(self, rx_z_2):
        self.rx_z_2 = rx_z_2
        self.owc_OWC_Channel_absolute_0.set_rx_coordinates_array([self.rx_x_1, self.rx_y_1, self.rx_z_1 , self.rx_x_2, self.rx_y_2, self.rx_z_2])

    def get_rx_z_1(self):
        return self.rx_z_1

    def set_rx_z_1(self, rx_z_1):
        self.rx_z_1 = rx_z_1
        self.owc_OWC_Channel_absolute_0.set_rx_coordinates_array([self.rx_x_1, self.rx_y_1, self.rx_z_1 , self.rx_x_2, self.rx_y_2, self.rx_z_2])

    def get_rx_y_2(self):
        return self.rx_y_2

    def set_rx_y_2(self, rx_y_2):
        self.rx_y_2 = rx_y_2
        self.analog_const_source_x_0_1_0.set_offset(self.rx_y_2)
        self.owc_OWC_Channel_absolute_0.set_rx_coordinates_array([self.rx_x_1, self.rx_y_1, self.rx_z_1 , self.rx_x_2, self.rx_y_2, self.rx_z_2])

    def get_rx_y_1(self):
        return self.rx_y_1

    def set_rx_y_1(self, rx_y_1):
        self.rx_y_1 = rx_y_1
        self.analog_const_source_x_0_2.set_offset(self.rx_y_1)
        self.owc_OWC_Channel_absolute_0.set_rx_coordinates_array([self.rx_x_1, self.rx_y_1, self.rx_z_1 , self.rx_x_2, self.rx_y_2, self.rx_z_2])

    def get_rx_x_2(self):
        return self.rx_x_2

    def set_rx_x_2(self, rx_x_2):
        self.rx_x_2 = rx_x_2
        self.analog_const_source_x_0_0_0_0.set_offset(self.rx_x_2)
        self.owc_OWC_Channel_absolute_0.set_rx_coordinates_array([self.rx_x_1, self.rx_y_1, self.rx_z_1 , self.rx_x_2, self.rx_y_2, self.rx_z_2])

    def get_rx_x_1(self):
        return self.rx_x_1

    def set_rx_x_1(self, rx_x_1):
        self.rx_x_1 = rx_x_1
        self.analog_const_source_x_0_0_1.set_offset(self.rx_x_1)
        self.owc_OWC_Channel_absolute_0.set_rx_coordinates_array([self.rx_x_1, self.rx_y_1, self.rx_z_1 , self.rx_x_2, self.rx_y_2, self.rx_z_2])

    def get_rx_u_z_2(self):
        return self.rx_u_z_2

    def set_rx_u_z_2(self, rx_u_z_2):
        self.rx_u_z_2 = rx_u_z_2
        self.owc_OWC_Channel_absolute_0.set_rx_orientation_array([self.rx_u_x_1, self.rx_u_y_1, self.rx_u_z_1 , self.rx_u_x_2, self.rx_u_y_2, self.rx_u_z_2])

    def get_rx_u_z_1(self):
        return self.rx_u_z_1

    def set_rx_u_z_1(self, rx_u_z_1):
        self.rx_u_z_1 = rx_u_z_1
        self.owc_OWC_Channel_absolute_0.set_rx_orientation_array([self.rx_u_x_1, self.rx_u_y_1, self.rx_u_z_1 , self.rx_u_x_2, self.rx_u_y_2, self.rx_u_z_2])

    def get_rx_u_y_2(self):
        return self.rx_u_y_2

    def set_rx_u_y_2(self, rx_u_y_2):
        self.rx_u_y_2 = rx_u_y_2
        self.owc_OWC_Channel_absolute_0.set_rx_orientation_array([self.rx_u_x_1, self.rx_u_y_1, self.rx_u_z_1 , self.rx_u_x_2, self.rx_u_y_2, self.rx_u_z_2])

    def get_rx_u_y_1(self):
        return self.rx_u_y_1

    def set_rx_u_y_1(self, rx_u_y_1):
        self.rx_u_y_1 = rx_u_y_1
        self.owc_OWC_Channel_absolute_0.set_rx_orientation_array([self.rx_u_x_1, self.rx_u_y_1, self.rx_u_z_1 , self.rx_u_x_2, self.rx_u_y_2, self.rx_u_z_2])

    def get_rx_u_x_2(self):
        return self.rx_u_x_2

    def set_rx_u_x_2(self, rx_u_x_2):
        self.rx_u_x_2 = rx_u_x_2
        self.owc_OWC_Channel_absolute_0.set_rx_orientation_array([self.rx_u_x_1, self.rx_u_y_1, self.rx_u_z_1 , self.rx_u_x_2, self.rx_u_y_2, self.rx_u_z_2])

    def get_rx_u_x_1(self):
        return self.rx_u_x_1

    def set_rx_u_x_1(self, rx_u_x_1):
        self.rx_u_x_1 = rx_u_x_1
        self.owc_OWC_Channel_absolute_0.set_rx_orientation_array([self.rx_u_x_1, self.rx_u_y_1, self.rx_u_z_1 , self.rx_u_x_2, self.rx_u_y_2, self.rx_u_z_2])

    def get_rx_psi_c_2(self):
        return self.rx_psi_c_2

    def set_rx_psi_c_2(self, rx_psi_c_2):
        self.rx_psi_c_2 = rx_psi_c_2

    def get_rx_psi_c_1(self):
        return self.rx_psi_c_1

    def set_rx_psi_c_1(self, rx_psi_c_1):
        self.rx_psi_c_1 = rx_psi_c_1

    def get_rx_n_2(self):
        return self.rx_n_2

    def set_rx_n_2(self, rx_n_2):
        self.rx_n_2 = rx_n_2

    def get_rx_n_1(self):
        return self.rx_n_1

    def set_rx_n_1(self, rx_n_1):
        self.rx_n_1 = rx_n_1

    def get_rx_Ts_2(self):
        return self.rx_Ts_2

    def set_rx_Ts_2(self, rx_Ts_2):
        self.rx_Ts_2 = rx_Ts_2

    def get_rx_Ts_1(self):
        return self.rx_Ts_1

    def set_rx_Ts_1(self, rx_Ts_1):
        self.rx_Ts_1 = rx_Ts_1

    def get_rx_C_r_2(self):
        return self.rx_C_r_2

    def set_rx_C_r_2(self, rx_C_r_2):
        self.rx_C_r_2 = rx_C_r_2

    def get_rx_C_r_1(self):
        return self.rx_C_r_1

    def set_rx_C_r_1(self, rx_C_r_1):
        self.rx_C_r_1 = rx_C_r_1

    def get_rx_A_2(self):
        return self.rx_A_2

    def set_rx_A_2(self, rx_A_2):
        self.rx_A_2 = rx_A_2

    def get_rx_A_1(self):
        return self.rx_A_1

    def set_rx_A_1(self, rx_A_1):
        self.rx_A_1 = rx_A_1





def main(top_block_cls=OWC_Channel_absolute_Example, options=None):

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
