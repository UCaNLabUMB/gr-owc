from xmlrpc.client import ServerProxy
import zmq
import numpy as np
import time

########### 0 for Singal & 1 for Tone
Signal_Selection = 0
############# Disabe Constant Value
DISABLED = 2
######## Time Delay in Seconds
time_delay = 1
time_delay_2 = 3
#####################

F_ENABLE = 1
F_BYPASS = 0

tx_1_settings = [DISABLED,Signal_Selection,DISABLED,Signal_Selection,DISABLED,Signal_Selection,DISABLED,Signal_Selection]
tx_2_settings = [DISABLED,Signal_Selection,Signal_Selection,DISABLED,DISABLED,Signal_Selection,Signal_Selection,DISABLED]
rx_1_settings = [F_ENABLE,F_ENABLE,F_ENABLE,F_ENABLE,F_BYPASS,F_BYPASS,F_BYPASS,F_BYPASS]
rx_2_settings = [F_ENABLE,F_ENABLE,F_ENABLE,F_ENABLE,F_BYPASS,F_BYPASS,F_BYPASS,F_BYPASS]

def power_measurement(socket):
    latest_msg = None
    try:
        while socket.poll(0):  # As long as there are messages in the buffer
            latest_msg = socket.recv(flags=zmq.NOBLOCK)  # Overwrite latest_msg with the new message
    except zmq.Again:
        pass  # Buffer is now drained, and latest_msg contains the last message
    
    if latest_msg is not None:  # If we got at least one message
        data = np.frombuffer(latest_msg, dtype=np.float32, count=-1)
        avg_power = np.average(data)
        return avg_power
    else:
        return None


# Initialize server proxies
STA2_control = ServerProxy('http://10.1.1.2:8080')
STA3_control = ServerProxy('http://10.1.1.3:8080')

# Set up ZMQ for Signal 1
context = zmq.Context()
socket1 = context.socket(zmq.SUB)
socket1.connect("tcp://10.1.1.3:55555")
socket1.setsockopt(zmq.SUBSCRIBE, b'')

# Set up ZMQ for Signal 2
context2 = zmq.Context()
socket2 = context2.socket(zmq.SUB)
socket2.connect("tcp://10.1.1.3:55556")
socket2.setsockopt(zmq.SUBSCRIBE, b'')


###########################################################
# Set the path for Signal 1 and Signal 2 before measurements
for j in range(len(tx_1_settings)):
    print(f"[Current TX Settings {tx_1_settings[j]} {tx_2_settings[j]}]")
    print(f"[Current RX Settings {rx_1_settings[j]} {rx_2_settings[j]}]")
    STA2_control.set_path_select_1(tx_1_settings[j])
    STA2_control.set_path_select_2(tx_2_settings[j])
    STA3_control.set_select_filter_1(rx_1_settings[j])
    STA3_control.set_select_filter_2(rx_2_settings[j])
    time.sleep(time_delay_2)
    avg_power1 = power_measurement(socket1)
    # Perform measurements
    for i in range(2):  # Repeat the measurement 3 times for demonstration purposes
        # Measure Signal 1
        time.sleep(time_delay)
        avg_power1 = power_measurement(socket1)
        avg_power2 = power_measurement(socket2)
        if avg_power1 is not None and  avg_power2 is not None: 
            print(f" Power 1: {avg_power1} Power 2: {avg_power2}")
        else:
            print("No message received")

