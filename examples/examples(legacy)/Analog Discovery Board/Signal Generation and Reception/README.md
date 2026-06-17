This folder contains basic GNU Radio flowgraphs for testing Analog Discovery Board transmit and receive functionality in OWC experiments.

## Flowgraphs

### OWC_SimpleTone
Generates a simple tone using the Analog Discovery Board waveform output. This is used for basic transmitter testing and verifying LED output.

### OWC_RandomSignal
Generates a test signal and sends it through the Analog Discovery Board output. This flowgraph is useful for checking signal generation, waveform playback, and basic OWC transmitter behavior.

### OWC_Rx
Receives a signal using the Analog Discovery Board analog input and displays it in GNU Radio using time, frequency, and waterfall plots.

## Purpose

These flowgraphs are mainly used for hardware verification before running more advanced experiments.

They help confirm:

- Analog Discovery output is working
- LED transmitter is receiving a signal
- Photodetector output can be captured
- GNU Radio can interface with the Analog Discovery Board

## Requirements

- Analog Discovery 2 or 3
- GNU Radio 3.10
- WaveForms Software
- Analog Discovery GNU Radio blocks

Some parameters such as sample rate, amplitude, frequency, and buffer size may need to be adjusted depending on the hardware setup.
