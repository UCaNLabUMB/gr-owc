# gr-owc Modulators & Demodulators

## Overview
This chapter introduces the modulation and demodulation blocks available in gr-owc for Optical Wireless Communications (OWC). It highlights common optical modulation schemes, how they are implemented in GNU Radio, and the role of demodulators in recovering transmitted information.

**Tutorial Video:** _Coming Soon_


### Objective
This chapter provides an overview of the core modulation and demodulation capabilities supported by gr-owc, including practical considerations for OWC systems.


## Supported Modulation Techniques
gr-owc includes blocks for several optical modulation schemes commonly used in OWC systems:

- **OOK Modulator / Demodulator**: On-Off Keying for simple binary signaling.
- **PAM Modulator / Demodulator**: Pulse Amplitude Modulation for multi-level signaling.
- **PPM Modulator / Demodulator**: Pulse Position Modulation for symbol-based transmission.
- **VPPM Modulator / Demodulator**: Variable Pulse Position Modulation for enhanced flexibility.

These blocks can be combined with other gr-owc components to build complete transmit and receive chains for experimental OWC systems.


## Design Considerations
When selecting a modulation scheme for an OWC system, factors such as:

- bandwidth efficiency,
- implementation complexity,
- robustness to channel impairments,
- compatibility with optical hardware constraints,

should be considered. In practice, the chosen scheme depends on the target application, available hardware, and desired performance trade-offs.


## Example Workflow
A typical workflow in gr-owc involves:

1. Generating or loading source data.
2. Passing the data through a modulation block such as OOK, PAM, PPM, or VPPM.
3. Transmitting the modulated signal through the system chain.
4. Recovering the information using the corresponding demodulation block.


# References
* GNURadio: [https://www.gnuradio.org/about/](https://www.gnuradio.org/about/)
* gr-owc Block Documentation: [https://github.com/UCaNLabUMB/gr-owc/tree/main/docs/GitHub_Documentation/Blocks](https://github.com/UCaNLabUMB/gr-owc/tree/main/docs/GitHub_Documentation/Blocks)


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
