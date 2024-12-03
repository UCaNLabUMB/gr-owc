# VPPM Modulator
Category: Signal Processing Blocks

Block Name: VPPM Modulator

## Overview
The `VPPM_Modulator` block in the `gr-owc` module implements **Variable Pulse Position Modulation (VPPM)**, a modulation technique primarily used in optical wireless communication systems. VPPM combines pulse position modulation (PPM) with variable pulse width to control the brightness of LED. This makes it ideal for visible light communication (VLC) systems where transmission are integrated.

The `VPPM_Modulator` block is designed to process discrete symbols and generate a modulated signal by adjusting both the position and width of pulses within a symbol duration.

---

## Parameters

The `VPPM_Modulator`  block is designed with the following configurable parameters to simulate the VPPM effectively:

| Parameter Name         | Description                                                                 | Default Value | Data Type       | Example Input |
|------------------------|-----------------------------------------------------------------------------|---------------|-----------------|---------------|
| `max_magnitude`        | Magnitude of the pulse (signal high level).                                | `1.0`         | `Float`         | `2.0`         |
| `min_magnitude`        | Magnitude of the base signal (signal low level).                           | `0.0`         | `Float`         | `-1.0`        |
| `samples_per_symbol`   | Total number of samples in each symbol period.                             | `8`           | `Integer`       | `16`          |
| `samples_per_pulse`    | Number of consecutive samples representing the pulse width.                | `4`           | `Integer`       | `8`           |

---

## Description

### Variable Pulse Position Modulation (VPPM)
VPPM is a modulation technique that conveys data through the position of a pulse (like PPM) while varying the width of the pulse to adjust the brightness of LEDs in optical communication systems. This feature allows simultaneous control over the optical intensity and the transmission of information.

In VPPM:
- **Pulse Position**: The binary value of the input symbol determines whether the pulse appears at the beginning or end of the symbol duration.
- **Pulse Width**: The `samples_per_pulse` parameter defines the width of the pulse, directly affecting the LED's brightness.

**Pulse Generation**:
   - A pulse of `max_magnitude` is placed within the defined position for `samples_per_pulse` samples.
   - The remaining samples in the symbol period are filled with `min_magnitude`.

### LED Brightness Control
The brightness of LED, is controlled by the ratio of `samples_per_pulse` to `samples_per_symbol`. A larger pulse width results in a increased brightness. This allows VPPM to achieve simultaneous transmission and illumination in VLC systems.

## Summary

The `VPPM_Modulator` block generates Variable Pulse Position Modulation (VPPM) signals by combining pulse position with pulse width modulation. It supports configurable parameters such as pulse width, symbol duration, and signal amplitude to control both data encoding and LED brightness. This block is essential for implementing VPPM in communication systems, particularly for VLC applications where illumination and data transmission are integrated.

## Examples

(Comming soon)

# gr-owc
* [gr-owc](https://github.com/UCaNLabUMB/gr-owc/tree/main)
*  Blocks:
  
| Sl No. | Block Name                    | Description                                                                                               |
|--------|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1      | [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OWC_Channel_Model(Relative).md)    | Models the optical channel, considering DC channel gain from transmitter to receiver.                     |
| 2      | [OWC_Channel_Block(Absolute)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OWC_Channel_Block(Absolute).md)    | Models the optical channel using absolute coordinates of the transmitter and receiver, considering DC channel gain from transmitter to receiver. |
| 3      | [OOK_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OOK_Modulator.md)                  | Implements On-Off Keying (OOK) baseband modulation scheme.                                                |
| 4      | [OOK_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OOK_Demodulator.md)                | Demodulates On-Off Keying (OOK) baseband signals and defines the binary outcome.                          |
| 5      | [PAM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PAM_Modulator.md)                | Implements Pulse Amplitude Modulation (PAM), assigning varying amplitude levels based on symbols.           |
| 6      | VPPM_Modulator              | Implements Variable Pulse Position Modulation (VPPM).                          |
| 7      | [PPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PPM_Modulator.md)                | Implements Pulse Position Modulation (PPM), varying the position of pulse(s) within a symbol.                          |
