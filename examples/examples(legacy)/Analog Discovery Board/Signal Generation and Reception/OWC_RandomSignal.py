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

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import ad2



from gnuradio import qtgui

class OWC_RandomSignal(gr.top_block, Qt.QWidget):

    def __init__(self, adb_amp=0, amp=0, buffer_size=32768, node='182', samp_rate=250000, tone_freq=0):
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

        self.settings = Qt.QSettings("GNU Radio", "OWC_RandomSignal")

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
        self.adb_amp = adb_amp
        self.amp = amp
        self.buffer_size = buffer_size
        self.node = node
        self.samp_rate = samp_rate
        self.tone_freq = tone_freq

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_sink_x_0 = qtgui.sink_f(
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
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 10e3, 0.5, 0, 0)
        self.ad2_AD2_AnalogOut_Play_f_0 = ad2.AD2_AnalogOut_Play_f(0, adb_amp, samp_rate , buffer_size)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.ad2_AD2_AnalogOut_Play_f_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.qtgui_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "OWC_RandomSignal")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_adb_amp(self):
        return self.adb_amp

    def set_adb_amp(self, adb_amp):
        self.adb_amp = adb_amp

    def get_amp(self):
        return self.amp

    def set_amp(self, amp):
        self.amp = amp

    def get_buffer_size(self):
        return self.buffer_size

    def set_buffer_size(self, buffer_size):
        self.buffer_size = buffer_size

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_tone_freq(self):
        return self.tone_freq

    def set_tone_freq(self, tone_freq):
        self.tone_freq = tone_freq



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "-b", "--adb-amp", dest="adb_amp", type=eng_float, default=eng_notation.num_to_str(float(0)),
        help="Set adb amp [default=%(default)r]")
    parser.add_argument(
        "-A", "--amp", dest="amp", type=eng_float, default=eng_notation.num_to_str(float(0)),
        help="Set amp [default=%(default)r]")
    parser.add_argument(
        "-z", "--buffer-size", dest="buffer_size", type=intx, default=32768,
        help="Set Buffer Size [default=%(default)r]")
    parser.add_argument(
        "-n", "--node", dest="node", type=str, default='182',
        help="Set Node Number [default=%(default)r]")
    parser.add_argument(
        "-a", "--samp-rate", dest="samp_rate", type=eng_float, default=eng_notation.num_to_str(float(250000)),
        help="Set Sample Rate [default=%(default)r]")
    parser.add_argument(
        "-f", "--tone-freq", dest="tone_freq", type=eng_float, default=eng_notation.num_to_str(float(0)),
        help="Set freq [default=%(default)r]")
    return parser


def main(top_block_cls=OWC_RandomSignal, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(adb_amp=options.adb_amp, amp=options.amp, buffer_size=options.buffer_size, node=options.node, samp_rate=options.samp_rate, tone_freq=options.tone_freq)

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
