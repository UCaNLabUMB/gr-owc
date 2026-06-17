from gnuradio import gr
import pmt
import time

# EDIT THIS PATH
FILENAME = "/home/ucanlab/Downloads/test.txt"

# If True, re-read the file every time you trigger
RELOAD_ON_TRIGGER = False


class blk(gr.basic_block):
    def __init__(self):
        gr.basic_block.__init__(
            self,
            name="trigger_send_file",
            in_sig=None,
            out_sig=None,
        )

        self.filename = FILENAME
        self.reload_on_trigger = RELOAD_ON_TRIGGER

        # Trigger input
        self.message_port_register_in(pmt.intern("trigger"))
        self.set_msg_handler(pmt.intern("trigger"), self.handle_trigger)

        # Output PDU
        self.message_port_register_out(pmt.intern("out"))

        self._tx_count = 0
        self._payload_bytes = b""

        # Load file once at start
        self._load_file()

    def _load_file(self):
        try:
            with open(self.filename, "rb") as f:
                self._payload_bytes = f.read()

            if len(self._payload_bytes) == 0:
                print(f"[WARN] Loaded '{self.filename}' but it is empty.")
            else:
                print(f"Loaded '{self.filename}' ({len(self._payload_bytes)} bytes)")

        except Exception as e:
            self._payload_bytes = b""
            print(f"[ERROR] Could not load '{self.filename}': {e}")

    def handle_trigger(self, msg):
        # Extract trigger value cleanly
        value_pmt = pmt.cdr(msg) if pmt.is_pair(msg) else msg
        try:
            value = pmt.to_python(value_pmt)
        except:
            print("Invalid TRIGGER PMT:", msg)
            return

        # Only fire on real trigger
        if value != 1:
            return

        # Reload file if desired
        if self.reload_on_trigger:
            self._load_file()

        if not self._payload_bytes:
            print("Triggered, but file is empty or not loaded.")
            return

        # Metadata generated ONLY on trigger
        meta = pmt.make_dict()

        timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        meta = pmt.dict_add(meta, pmt.intern("timestamp"), pmt.intern(timestamp_str))

        self._tx_count += 1
        meta = pmt.dict_add(meta, pmt.intern("tx_count"), pmt.from_long(self._tx_count))

        # Payload: file bytes
        data = pmt.init_u8vector(len(self._payload_bytes), list(self._payload_bytes))

        # Publish PDU
        self.message_port_pub(pmt.intern("out"), pmt.cons(meta, data))

        print(f"Triggered -> sent '{self.filename}' (tx_count={self._tx_count})")

    def stop(self):
        return True
