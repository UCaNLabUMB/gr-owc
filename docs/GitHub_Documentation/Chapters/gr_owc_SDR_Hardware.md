# gr-owc SDR Hardware

## Overview
This chapter provides an introduction to the SDR hardware used with `gr-owc`, including platform considerations, interfaces, and practical deployment aspects for optical wireless experiments.

**Tutorial Video:** _Coming Soon_


### Objective
_Coming Soon_


## SDR Platforms
The software installation to run the AD 2 & 3 board can be found in [Hardware Setup](/docs/Hardware_Setup/README_ADB.md)

### Transmitter
The goal is to use AD2 or AD3 to transmit a floating single-tone frequency using GNU Radio, an open-source tool for software-defined radios (SDRs), along with the
`gr-ad2` repository, which contains all the necessary packages for the AD2 and AD3. This, in turn, verifies that the AD2 or AD3 can be used as a transmitting device, which later helps in the OWC development.

**Components**
- Tektronix MDO3014 Mixed Domain Oscilloscope
- Digilent Analog Discovery Board 2 or 3
- Raspberry Pi 4 or 5 model B
- 5V/2.1A Battery pack
- Digilent Adapter Board Analog Discovery BNC
- 2 male-to-male (M-M) BNC cables
- USB-A to USB Type-C cable

**Setup**
- Connect the BNC adapter board → AD3 or AD2 Board.
- Use the M-M BNC cable to connect the output (W1) on the BNC adapter board → CH1 on the oscilloscope.
- Connect the USB-A → RPi → AD3 or AD2 Board.
- On the oscilloscope, press **Math**.

In GNU Radio, navigate to the designated directory in the terminal and run `OWC_RandomSignal.py` (i.e., `python3 OWC_RandomSignal.py`), or open VNC Viewer directly, connect the blocks as shown in the figure below, and run it for signal transmission (see Results section).

In our case, two amplitude settings affect the overall signal: the signal source amplitude, and the hardware amplitude (i.e., the AD2 AnalogOut Play Sink). For example, if the signal source is set to 0.5V and the hardware amplitude is set to 5V, the output signal is 2.5V. We can express this relationship in terms of $V_p$:

$$ V_p = A_{hw} \cdot A_{sig} \leq A_{hw} $$

where $A_{hw}$ is the hardware amplitude and $A_{sig}$ is the signal source amplitude. The hardware amplitude acts as the upper limit: for example, setting the signal source to 3V with a hardware amplitude of 5V would give $3\text{V} \times 5\text{V} = 15\text{V}$, which exceeds the hardware limit and clips the sine wave, something we want to avoid. In addition, the sampling rate ($f_s$) defines the frequency band within which we can send our tone frequency, based on the Nyquist theorem:

$$ f_N = \pm \frac{f_s}{2} $$

![Figure 1: OWC_RandomSignal](/docs/hardware_characterization/Images/OWC_RandomSignal.png)

(Note: For the channel in the AD2 AnalogOut Play Sink Block, "0" is associated with ch1, and "1" is associated with ch2 based on the port we used for the oscilloscope)


**Results** 

![Figure 2: OWC_RandomSignal Result](/docs/hardware_characterization/Images/OWC_RandomSignal_result.png)

When we observe the oscilloscope, we can see the sine wave signal that we remotely command the Pi to activate. The peak-to-peak voltage ($V_{pp}$) and peak voltage ($V_{p}$) match our expectations, measuring 5 $V_{pp}$ and 2.5 $V_{p}$. Additionally, by using the FFT mode in the Math function, we can analyze the frequency domain for the sine wave. In this case, based on the 12.5 kHz/div, we can see our peak around 1 kHz, which verifies that our transmitter is functioning correctly.

### Receiver
This section describes the configuration to use AD2 or AD3 as receiver hardware. The process is similar to the transmitter, a few modifications need to be made inside the GNURadio block to make this work.

**Components**
- Keysight 33500B Series Waveform Generator
- Digilent Analog Discovery Board 2 or 3
- Raspberry Pi 4 or 5 model B
- 5V/2.1A Battery pack
- Digilent Adapter Board Analog Discovery BNC
- 2 male-to-male (M-M) BNC cables
- USB-A to USB Type-C cable

**Setup**
- Connect the BNC adapter board → AD3 or AD2 Board.
- Use the M-M BNC cable to connect the output (W1) on the BNC adapter board → CH1 on the Function Generator (FG).
- Connect the USB-A → RPi → AD3 or AD2 Board.
- Turn on FG &rarr; Press 1 (for channel 1) &rarr; Press on Parameter &rarr; change frequency (e.g., 1kHz), amplitude (e.g., 1 $V_{pp}$), offset (e.g., 0 V).
- Press on Waveforms &rarr; sine. 
- Press 1 &rarr; Output On. 

To receive the signal on the Raspberry Pi, we used the AD2 Analog Record Source block. The range setting in the block needs to match the amplitude (e.g., $5\,V_{pp}$) set on the Function Generator (FG). In addition, since we wanted a clear visualization of the signal in the frequency domain in the GNU Radio flowgraph, we also adjusted the frequency of the sine wave to 100 kHz. To visualize this, we used a QT GUI Sink block with FFT size embedded. Since the FG sends a real sine wave signal, what we will see are mirrored spikes at $\pm 100\text{kHz}$.

![Figure 3: OWC_Rx](/docs/hardware_characterization/Images/OWC_Rx.png)

**Results** 

![Figure 4: OWC_Rx Result](/docs/hardware_characterization/Images/OWC_Rx_result.png)

As discussed, when running the GNURadio flowgraph (i.e., the block diagrams above), we observe harmonic spikes at $\pm 100\text{kHz}$. This confirms that our hardware is correctly receiving the transmitted signal from the FG.


## Hardware Integration
After testing the AD2 and AD3 from the above section, we will utilize the knowledge we learned from the [Hardware Characterization](/docs/hardware_characterization/Electrical to Optical.md) and integrate it into our overall setup for modularity, since devices such as AD2 and AD3 are easy to configure using their software Waveforms or GNURadio. 

**Components**
- Keysight 33500B Series Waveform Generator
- 2x Digilent Analog Discovery Board 2 or 3
- 2x Raspberry Pi 4 or 5 model B
- 2x 5V/2.1A Battery pack
- 2x Digilent Adapter Board Analog Discovery BNC
- 2x male-to-male (M-M) BNC cables
- 2x USB-A to USB Type-C cable
- **Mini-Circuits Bias-Tee ZFBT-6GW+** 
- **Thorlabs ADP120A2 Photo-detector, optical lens & blue filter**
- **Small LED panel (e.g., circle, rectangular, etc.)**
- **female (F) jumper wires with female (F) BNC cable, male (M) BNC with female (F) connector**
- **Mini-Circuits 15542 SLP-5+ Low Pass Filter (LPF)** & **Mini-Circuits DC Block 50&Omega BLK-89-S+**
- **Other accessories (e.g., Thorlabs screws and hardware kit)**

**Setup** 

Tx side: 
- Connect the BNC adapter board &rarr; AD3 or AD2 Board.
- Use the M-M BNC cable to connect the output (W1) on the BNC adapter board and ch1 on the oscilloscope &rarr;   Bias-Tee &rarr; LED male jumping wires.
- Connect the USB-A &rarr; RPi &rarr; AD3 or AD2 Board.
- Turn on FG, press 1 (for channel 1) &rarr; Output Load &rarr; Set To High Z. 
- Press on Waveforms &rarr; More &rarr; DC (e.g., 8.5$V_{pp}$). 
- Press 1 &rarr; Output On.
- Open Waveforms in the RPi &rarr; Wavegen &rarr; Amplitude (e.g., 1V) &rarr; Offset (e.g., 0V). 
- Click Run (top left). 

Rx side: 
- Connect the BNC adapter board &rarr; AD3 or AD2 Board.
- Use the M-M BNC cable to connect the channel 1 input (CH1) on the BNC adapter board &rarr; LPF & DC Block &rarr; Photo-detector. 
- Connect the USB-A &rarr; RPi &rarr; AD3 or AD2 Board. 
- Open Waveforms in the RPi &rarr; Scope &rarr; Disable channel 2 (check off ch2) &rarr; Adjust the Range (e.g., 20mV/div for 1V). 
- Click Run (top left). 

In this section, instead of using GNURadio with .grc files to run the AD2 or AD3 for transmit and receive, we take a step back and use the Waveform software to send a sine wave signal and receive it at the other end. One thing to note is that because the Waveform software caps at 5V for voltage offset, we will use a **Bias-Tee**, which we can hook up to another voltage supply and supply voltage offset to the AD2 or AD3 with their already configured $V_{pp}$ to drive the LED to its associated driven voltage (i.e., linear voltage range). 

![Figure 5: SDR_Integration](/docs/hardware_characterization/Images/SDR_Integration.png)

**Results** 

![Figure 6: SDR_Integration](/docs/hardware_characterization/Images/SDR_result.png)

The figure above displays the sine wave transmitted and received in real time. There's some noise from the receiving part, and in our case, we can see that the $V_{pp}$ is about 120 mV based on the 20 mV/div scale on ch1.


# References
* GNURadio: [https://www.gnuradio.org/about/](https://www.gnuradio.org/about/)


# Tutorial Chapters

* **Next Chapter:** 

| Chapter | Topic | Summary |
| --- | --- | --- |
| 1    | [Background](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Chapters/gr_owc_Overview.md)  | Overview of Software Defined Radio and an introduction to `gr-owc`, including its motivation and role in OWC.         |
| 2    | [Setup and Installation](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Chapters/gr_owc_Install.md)     | Installation instructions for GNURadio and gr-owc.         |
| 3    | [Channel Modeling](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Chapters/gr_owc_ChannelModel.md)      | Different channel modeling approaches for OWC, including their characteristics, types, and applications in various OWC scenarios. |
| 4    | [Hardware Characterization](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Chapters/gr_owc_Hardware_Characterization.md)     | Detailed analysis of hardware components and their characteristics used for OWC, such as Transmitter, Receiver, USRP, and their suitability for OWC. |
| 5    | [SDR Hardware](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Chapters/gr_owc_SDR_Hardware.md) | Overview of SDR hardware platforms and their integration with `gr-owc` for optical wireless experiments. |
| 6    | [Modulators & Demodulators](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Chapters/gr_owc_Modulators_Demodulators.md) | Modulation and demodulation techniques supported by `gr-owc`, along with their applications and implementation considerations. |
