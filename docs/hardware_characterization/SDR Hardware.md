# Analog Discovery Board 2 & 3
This document explains the process of configuring the Analog Discovery (AD) Board 2 & 3 as a transmitter and receiver for a Visible Light Positioning (VLP) system within
our overall Optical Wireless Communication (OWC) framework.

The software installation to run the AD 2 & 3 board can be found in [Hardware Setup](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc/docs/Hardware_Setup/README_ADB.md).

## Transmitter
The goal is to use AD2 or AD3 to transmit a floating single-tone frequency using GNU Radio, an open-source tool for software-defined radios (SDRs), along with the
`gr-ad2` repository, which contains all the necessary packages for the AD2 and AD3. This, in turn, verifies that the AD2 or AD3 can be used as a transmitting device, which later helps in the OWC development.

**Components**
- Tektronix MDO3014 Mixed Domain Oscilloscope
- Digilent Analog Discovery Board 2 or 3
- Raspberry Pi 4 or 5 model B
- Digilent Adapter Board Analog Discovery BNC
- 2 male-to-male (M-M) BNC cables
- USB-A to USB Type-C cable

**Setup**
- Connect the BNC adapter board → AD3 or AD2 Board.
- Use the M-M BNC cable to connect the output (W1) on the BNC adapter board → CH1 on the oscilloscope.
- Connect the USB-A → RPi → AD3 or AD2 Board.
- On the oscilloscope, press **Math**.

In GNU Radio, navigate to the designated directory in the terminal and run `OWC_RandomSignal.py` (i.e., `python3 OWC_RandomSignal.py`), or open VNC Viewer directly, load the `.grc` file, and run it for signal transmission (see image below). 

In our case, two amplitude settings affect the overall signal: the signal source amplitude, and the hardware amplitude (i.e., the AD2 AnalogOut Play Sink). For
example, if the signal source is set to 0.5V and the hardware amplitude is set to 5V, the output signal is 2.5V. We can express this relationship in terms of $V_p$:

$$ V_p = A_{hw} \cdot A_{sig} \leq A_{hw} $$

where $A_{hw}$ is the hardware amplitude and $A_{sig}$ is the signal source amplitude. The hardware amplitude acts as the upper limit: for example, setting the signal source to 3V with a hardware amplitude of 5V would give $3\text{V} \times 5\text{V} = 15\text{V}$, which exceeds the hardware limit and clips the sine wave , something we want to avoid.

![Figure 1: OWC_RandomSignal](/docs/hardware_characterization/Images/OWC_RandomSignal.png)
(Note: For the channel in the AD2 AnalogOut Play Sink, 0 is associated with ch1, and 1 is associated with ch2 based on the port we used for the oscilloscope)


**Results** 
[...]

## Receiver
This section describes the configuration to use AD2 or AD3 as receiver hardware. The process is similar to the transmitter, a few modifications need to be made inside the GNURadio block to make this work.

**Components**
- Keysight 33500B Series Waveform Generator
- Digilent Analog Discovery Board 2 or 3
- Raspberry Pi 4 or 5 model B
- Digilent Adapter Board Analog Discovery BNC
- 2 male-to-male (M-M) BNC cables
- USB-A to USB Type-C cable

**Setup**
- Connect the BNC adapter board → AD3 or AD2 Board.
- Use the M-M BNC cable to connect the output (W1) on the BNC adapter board → CH1 on the Function Generator (FG).
- Connect the USB-A → RPi → AD3 or AD2 Board.
- Turn on FG &rarr; 
- On the oscilloscope, press **Math**.

**Results** 


