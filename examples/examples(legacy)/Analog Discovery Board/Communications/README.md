# Communication Flowgraphs

## Overview

This folder contains GNU Radio flowgraphs used to implement Optical Wireless Communication (OWC) and hybrid RF/OWC communication systems using Orthogonal Frequency Division Multiplexing (OFDM).

The flowgraphs were developed as part of the UCaN Laboratory research effort to investigate software-defined optical communication systems using the Digilent Analog Discovery platform.

## Features

- File transmission over OWC links
- OFDM packet generation
- QPSK payload modulation
- BPSK header modulation
- CRC packet protection
- Hermitian symmetry for IM/DD optical transmission
- Analog Discovery waveform generation
- Hybrid RF/OWC experimentation
- Pluto SDR integration
- Packet recovery and file reconstruction

## Hardware

- Analog Discovery 2 / 3
- LED transmitter
- Photodetector receiver
- GNU Radio 3.10
- WaveForms SDK
- Optional Pluto SDR

## Flowgraphs

### OWC_Push_Button
Single-path OFDM transmitter using Analog Discovery hardware.

### Integration_Flow_Graph
Integrated communication framework supporting both OWC and RF packet generation using USRP B200 Mini for RF transmission.

### T4_Comms_Pluto
Hybrid communication flowgraph utilizing a Pluto SDR for RF transmission.

### Integrated_Comms_Rx
OFDM receiver used to recover transmitted packets and reconstruct transmitted files.

## Supporting Scripts

### ad_burst_tx.py
WaveForms SDK interface used to transmit OFDM bursts through the Analog Discovery waveform generator.

### epy_block_0.py
Custom GNU Radio sink used to detect packet boundaries and send bursts through the Analog Discovery.

### epy_block_0_0.py
Trigger-based file loader that converts file contents into GNU Radio PDUs.
