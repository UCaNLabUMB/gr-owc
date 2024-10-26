from xmlrpc.client import ServerProxy
import zmq
import numpy as np
import time
######## Time Delay in Seconds
time_delay = 8
#####################
LOW = 0
HIGH = 1
MIXED = 2
#Second Audio Control
ON = 1
OFF = 0
#######
tx_1_settings = [LOW,LOW,HIGH]
rx_1_settings = [LOW,LOW,HIGH]
#####Second Audio Settings
ch2_settings = [OFF,ON,ON]






# Initialize server proxies
STA_TX1control = ServerProxy('http://10.1.1.2:8080')
STA_RX1control = ServerProxy('http://10.1.1.3:8080')




###########################################################
# Set the path for Signal 1 and Signal 2 before measurements
for j in range(len(tx_1_settings)):
    print(f"[Current TX Settings {tx_1_settings[j]}]")
    print(f"[Current RX Settings {rx_1_settings[j]}]")
    print(f"[Current CH_2 Settings {ch2_settings[j]}]")
    print()  
    STA_TX1control.set_path_select(tx_1_settings[j])
    STA_RX1control.set_path_select(rx_1_settings[j])
    STA_TX1control.set_ch2_enable(ch2_settings[j])
    time.sleep(time_delay)

    