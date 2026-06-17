# Communications

This folder contains GNU Radio flowgraphs and supporting Python scripts developed for OFDM-based Optical Wireless Communication (OWC) and hybrid RF/OWC communication experiments using the Analog Discovery Board.

## Flowgraphs

### OWC_Push_Button
Basic OFDM transmitter that sends the contents of a text file when triggered. Uses the Analog Discovery Board to generate and transmit the waveform through an optical transmitter.

### Integration_Flow_Graph
Integrated communication framework supporting both OWC and RF transmission paths. Uses the Analog Discovery Board for optical transmission and a USRP B200 Mini for RF transmission.

### T4_Comms_Pluto
Hybrid OWC/RF communication flowgraph that replaces the USRP RF path with an ADALM-PLUTO SDR.

### Integrated_Comms_Rx
OFDM receiver used to recover transmitted packets and reconstruct received files.

## Supporting Python Files

### *_epy_block_0_0.py
Custom GNU Radio embedded Python blocks that load a file and generate a PDU when a transmission trigger occurs.

### *_epy_block_0.py
Custom GNU Radio embedded Python blocks that collect OFDM bursts and transmit them through the Analog Discovery waveform generator.

### ad_burst_tx.py
Provides the interface between GNU Radio and the Analog Discovery Board using the Digilent WaveForms SDK. This script is responsible for configuring the waveform generator and transmitting burst waveforms.

## Dependencies

The Analog Discovery transmission blocks require:

- WaveForms Software
- WaveForms SDK
- WaveForms-SDK-Getting-Started-PY

Repository:
https://github.com/Digilent/WaveForms-SDK-Getting-Started-PY

Several embedded Python blocks contain local file paths and SDK locations that may need to be updated before running on a different system.

## Notes

The `ad_burst_tx.py` script and the `WaveForms-SDK-Getting-Started-PY` repository should be located in the same directory as the communication flowgraphs, or the Python paths within the embedded blocks must be updated accordingly.
