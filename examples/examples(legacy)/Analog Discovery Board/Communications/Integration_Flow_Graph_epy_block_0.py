"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
import pmt
from gnuradio import gr
import sys
sys.path.append("/home/ucanlab/Downloads/WF_ADB/WaveForms-SDK-Getting-Started-PY-master")
from ad_burst_tx import ADBurstTX

class blk(gr.sync_block):
    def __init__(self,
                 samp_rate=250000,
                 amplitude=1.0,
                 len_tag_key="packet_len"):
        gr.sync_block.__init__(
            self,
            name="AD OFDM Burst Sink",
            in_sig=[np.float32],
            out_sig=None
        )

        self.len_tag_key = pmt.intern(len_tag_key)
        self.samp_rate = float(samp_rate)
        self.amplitude = float(amplitude)

        self.collecting = False
        self.expected_len = 0
        self.buffer = []

        self.tx = None

    def start(self):
        print("Opening AD device...")
        self.tx = ADBurstTX(channel=0)
        self.tx.open()
        self.tx.configure(
            sample_rate=self.samp_rate,
            amplitude=self.amplitude,
            offset=0.0
        )
        return True

    def work(self, input_items, output_items):
        in0 = input_items[0]
        nread = self.nitems_read(0)

        if self.tx is None:
            return len(in0)

        tags = self.get_tags_in_window(0, 0, len(in0))
        start_idx = 0

        for tag in tags:
            if pmt.equal(tag.key, self.len_tag_key):
                rel = int(tag.offset - nread)

                if rel < 0 or rel >= len(in0):
                    continue

                self.collecting = True
                self.expected_len = int(pmt.to_long(tag.value))
                self.buffer = []

                take = min(len(in0) - rel, self.expected_len)
                if take > 0:
                    self.buffer.extend(in0[rel:rel + take].tolist())

                start_idx = rel + take
                #print("Found packet_len tag:", self.expected_len)
                break

        if self.collecting and len(self.buffer) < self.expected_len:
            remaining = self.expected_len - len(self.buffer)
            if start_idx < len(in0):
                take = min(len(in0) - start_idx, remaining)
                self.buffer.extend(in0[start_idx:start_idx + take].tolist())

        if self.collecting and len(self.buffer) >= self.expected_len:
            burst = np.array(self.buffer[:self.expected_len], dtype=np.float64)

            #print("Transmitting OFDM burst with", len(burst), "samples")
            #print("burst min =", np.min(burst),
            #      "max =", np.max(burst),
            #      "peak =", np.max(np.abs(burst)))

            # optional safety normalization only if needed
            peak = np.max(np.abs(burst))
            if peak > 1.0:
                burst = burst / peak
                #print("Normalized burst to +/-1")

            self.tx.send_once(burst)

            self.collecting = False
            self.expected_len = 0
            self.buffer = []

        return len(in0)

    def stop(self):
        if self.tx is not None:
            try:
                self.tx.close()
            except Exception as e:
                print("Close error:", e)
            self.tx = None
        return True
