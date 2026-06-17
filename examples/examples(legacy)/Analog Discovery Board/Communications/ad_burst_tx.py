#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ad_burst_tx.py
#  
#  Copyright 2026  <ucanlab@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#!/usr/bin/env python3

#!/usr/bin/env python3

import time
import numpy as np
from ctypes import c_double, c_int, c_bool

from WF_SDK import device
from WF_SDK.device import constants


class ADBurstTX:
    def __init__(self, channel=0):
        self.dev = None
        self.dwf = None
        self.hdwf = None
        self.channel = c_int(channel)

        self.sample_rate = None
        self.amplitude = None
        self.offset = None

    def open(self):
        self.dev = device.open()
        self.dwf = device.dwf
        self.hdwf = self.dev.handle
        print("Opened:", self.dev.name)

    def configure(self, sample_rate, amplitude=1.0, offset=0.0):
        if self.dev is None:
            raise RuntimeError("Device is not open")

        self.sample_rate = float(sample_rate)
        self.amplitude = float(amplitude)
        self.offset = float(offset)

        if self.dwf.FDwfAnalogOutReset(self.hdwf, self.channel) == 0:
            device.check_error()

        if self.dwf.FDwfAnalogOutNodeEnableSet(
            self.hdwf,
            self.channel,
            constants.AnalogOutNodeCarrier,
            c_bool(True)
        ) == 0:
            device.check_error()

        # Use PLAY mode, not CUSTOM
        if self.dwf.FDwfAnalogOutNodeFunctionSet(
            self.hdwf,
            self.channel,
            constants.AnalogOutNodeCarrier,
            constants.funcPlay
        ) == 0:
            device.check_error()

        if self.dwf.FDwfAnalogOutNodeAmplitudeSet(
            self.hdwf,
            self.channel,
            constants.AnalogOutNodeCarrier,
            c_double(self.amplitude)
        ) == 0:
            device.check_error()

        if self.dwf.FDwfAnalogOutNodeOffsetSet(
            self.hdwf,
            self.channel,
            constants.AnalogOutNodeCarrier,
            c_double(self.offset)
        ) == 0:
            device.check_error()

        # One-shot burst
        if self.dwf.FDwfAnalogOutRepeatSet(
            self.hdwf,
            self.channel,
            c_int(1)
        ) == 0:
            device.check_error()

    def send_once(self, samples):
        if self.dev is None:
            raise RuntimeError("Device is not open")
        if self.sample_rate is None:
            raise RuntimeError("Device is not configured")

        samples = np.asarray(samples, dtype=np.float64)

        if len(samples) == 0:
            raise ValueError("samples is empty")

        peak = np.max(np.abs(samples))
        if peak > 1.0:
            samples = samples / peak

        n = len(samples)
        run_time = n / self.sample_rate

        print("N =", n)
        print("Desired Fs =", self.sample_rate)
        print("Run time =", run_time)

        buf = (c_double * n)(*samples)

        # In PLAY mode, frequency means sample rate
        if self.dwf.FDwfAnalogOutNodeFrequencySet(
            self.hdwf,
            self.channel,
            constants.AnalogOutNodeCarrier,
            c_double(self.sample_rate)
        ) == 0:
            device.check_error()

        if self.dwf.FDwfAnalogOutRunSet(
            self.hdwf,
            self.channel,
            c_double(run_time)
        ) == 0:
            device.check_error()

        if self.dwf.FDwfAnalogOutNodeDataSet(
            self.hdwf,
            self.channel,
            constants.AnalogOutNodeCarrier,
            buf,
            c_int(n)
        ) == 0:
            device.check_error()

        if self.dwf.FDwfAnalogOutConfigure(
            self.hdwf,
            self.channel,
            c_bool(True)
        ) == 0:
            device.check_error()

        time.sleep(run_time + 0.05)

        if self.dwf.FDwfAnalogOutConfigure(
            self.hdwf,
            self.channel,
            c_bool(False)
        ) == 0:
            device.check_error()

    def close(self):
        if self.dev is not None:
            device.close(self.dev)
            self.dev = None
            self.dwf = None
            self.hdwf = None
            print("Closed device")
