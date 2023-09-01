#!/usr/bin/env python3
#Author: UCaN Lab UMB
#Umass Boston, MA,USA
import argparse
from xmlrpc.client import ServerProxy
import zmq
import time
import numpy as np
import csv


noise_measurement = []
sig_measurements = []
interference_measurements = []

# Set up ZMQ
context = zmq.Context()
socket = context.socket(zmq.SUB)
# Change the ZMQ connection to use the Linux computer's IP
socket.connect("tcp://10.1.1.3:55555")
socket.setsockopt(zmq.SUBSCRIBE, b'')

# Initialize server proxies
STA2_control = ServerProxy('http://10.1.1.2:8080')
STA3_control = ServerProxy('http://10.1.1.3:8080')



def step_through_code():
    while True:
        choice = input("Press any key to continue, or 'q' to quit: ")
        if choice == 'q':
            print("Exiting.")
            break

        STA2_control.set_path_select_1(1)
        print('Tone Set')
        time.sleep(2)

        choice = input("Press any key to continue, or 'q' to quit: ")
        if choice == 'q':
            print("Exiting.")
            break

        STA2_control.set_path_select_1(2)
        print('Off Set')
        time.sleep(2)

        choice = input("Press any key to continue, or 'q' to quit: ")
        if choice == 'q':
            print("Exiting.")
            break

        STA2_control.set_path_select_1(0)
        print('Signal Set')

        choice = input("Press any key to continue, or 'q' to quit: ")
        if choice == 'q':
            print("Exiting.")
            break

        STA2_control.set_path_select_2(1)
        print('Signal 2 Tone Set')
        time.sleep(2)

        choice = input("Press any key to continue, or 'q' to quit: ")
        if choice == 'q':
            print("Exiting.")
            break

        STA2_control.set_path_select_2(2)
        print('Signal 2 Off Set')
        time.sleep(2)

        choice = input("Press any key to continue, or 'q' to quit: ")
        if choice == 'q':
            print("Exiting.")
            break

        STA2_control.set_path_select_2(0)
        print('Signal 2 Signal Set')

if __name__ == "__main__":
    step_through_code()









        


    







