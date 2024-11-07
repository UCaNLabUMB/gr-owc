# OOK Modulator
Category: Signal Processing Blocks

Block Name: OOK Modulator

## Overview
The `OOK_Modulator` block implements On-Off Keying (OOK), a baseband modulation technique used in optical wireless communication. This simple modulation scheme switches between two levels—typically `max_mag` and `min_mag`—to represent binary data.

## Parameters

The `OOK_Modulator` block has the following configurable parameters:

| Parameter Name        | Description                                             | Default Value   | Data Type   |
|-----------------------|---------------------------------------------------------|-----------------|-------------|
| `max_mag`             | Maximum magnitude for the "On" state                    | 1.0             | `Float`     |
| `min_mag`             | Minimum magnitude for the "Off" state                   | 0.0             | `Float`     |
| `samples_per_symbol`  | Number of samples per symbol                            | 1               | `Integer`       |

## Description
### OOK: Two-Level Modulation
The `OOK_Modulator` block generates a 2-level OOK waveform from an input bit stream for the given minimum (`min_mag`) and maximum (`max_mag`) values. The modulator translates binary data into amplitude levels, where the maximum value (`max_mag`) represents a binary "1", and the minimum value (`min_mag`) represents a binary "0".

### Samples Per Symbol
The `samples_per_symbol` parameter allows for the definition of the desired number of samples representing each symbol. This enables the control of the modulation's symbol rate and bandwidth usage.

## Summary
The `OOK_Modulator` block provides a effective way to implement binary amplitude modulation in OWC systems, allowing for efficient data transmission using basic on-off keying. Its adjustable parameters, including `min_mag`, `max_mag`, and `samples_per_symbol`, make it suitable for a variety of communication scenarios.

## Examples:
(Comming soon)

# gr-owc
* Blocks:
  
| Sl No. | Block Name                    | Description                                                                                               |
|--------|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1      | [OWC_Channel_Block(Relative)](https://github.com/kunal2431/gr-owc/blob/main/Documentation/OWC_Channel_Model(Relative).md)   | Models the optical channel, considering DC channel gain from transmitter to receiver.                     |
| 2      | [OWC_Channel_Block(Absolute)](https://github.com/kunal2431/gr-owc/blob/main/Documentation/OWC_Channel_Block(Absolute).md)    | Models the optical channel using absolute coordinates of the transmitter and receiver, considering DC channel gain from transmitter to receiver. |
| 3      | OOK_Modulator                  | Implements On-Off Keying (OOK) baseband modulation scheme.                                                |
| 4      | [OOK_Demodulator](https://github.com/kunal2431/gr-owc/blob/main/Documentation/OOK_Demodulator.md)                | Demodulates On-Off Keying (OOK) baseband signals and defines the binary outcome.                          |


* Chapters:
  
| Chapter | Topic                | Summary                                                                                                               |
|---------|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1       | Background            | Overview of Software Defined Radio and an introduction to `gr-owc`, including its motivation and role in OWC.         |
| 2       | Channel Modeling      | Different channel modeling approaches for OWC, including their characteristics, types, and applications in various OWC scenarios. |
| 3       | SDR; OWC Hardware     | Detailed analysis of hardware components and their characteristics used for OWC, such as Transmitter, Receiver, USRP, and their suitability for OWC. |
| 4       | Modulator & Demodulator | Modulation and demodulation techniques supported by `gr-owc`, along with their applications and implementation considerations. |
