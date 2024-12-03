# PPM Modulator
Category: Signal Processing Blocks

Block Name: PPM Modulator

## Overview
The `PPM_Modulator` block in the `gr-owc` module implements **Pulse Position Modulation (PPM)**, a technique where discrete symbols are represented by the position of a pulse within a symbol duration. This block is widely used in optical communication systems and other digital communication applications that require efficient modulation schemes.

This block is designed to work with the `Chunk to Symbols` block, which preprocesses input data into integer symbols. The output of the `Chunk to Symbols` block is directly connected to the input of the `PPM_Modulator`, enabling the modulation process.

---

## Parameters

The `PPM_Modulator` block is designed with the following configurable parameters to simulate the PPM effectively

| Parameter Name         | Description                                                                 | Default Value | Data Type       | Example Input |
|------------------------|-----------------------------------------------------------------------------|---------------|-----------------|---------------|
| `modulation_order`     | Number of pulse positions       | `2`           | `Integer`       | `4`           |
| `max_magnitude`        | Magnitude of the pulse (signal high level).                                | `1.0`         | `Float`         | `2.0`         |
| `min_magnitude`        | Magnitude of the base signal (signal low level).                           | `0.0`         | `Float`         | `-1.0`        |
| `samples_per_symbol`   | Total number of samples in each symbol period.                             | `8`           | `Integer`       | `16`          |
| `samples_per_pulse`    | Number of consecutive samples representing the pulse(High level).                      | `1`           | `Integer`       | `4`           |

---

## Description

### Pulse Position Modulation (PPM)
Pulse Position Modulation (PPM) is a modulation scheme where the position of a pulse within a fixed symbol duration encodes the transmitted symbol. For Modulation order $\( M \)$, there are $\( M \)$ possible positions for the pulse.

The ratio of the pulse width (`samples_per_pulse`) to the symbol duration (`samples_per_symbol`) determines how long the LED remains in the "ON" state at a high level during each symbol period. A larger pulse width relative to the symbol duration increases the LED's "ON" time, resulting in greater optical intensity and power output. This relationship is crucial in optical communication systems, where the LED's duty cycle directly affects the transmitted signal. This property makes PPM ideal for optical wireless communication systems(visible light communication (VLC)).

The `PPM_Modulator` generates a signal with:
- A `samples_per_pulse`(Number of consecutive samples representing the pulse) of amplitude `max_magnitude` located at the position corresponding to the input symbol.
- All other samples in the symbol period set to `min_magnitude`.

The `PPM_Modulator` block relies on the `Chunk to Symbols` block to preprocess input data. The `Chunk to Symbols` block maps input bits into integer symbols (ranging from $\( 0 \)$ to $\( M-1 \))$, which the `PPM_Modulator` then uses to determine pulse positions.

## Summary

PPM efficiently encodes data by using pulse positions instead of amplitude or frequency variations. The block allows users to control the total symbol duration (`samples_per_symbol`), pulse width (`samples_per_pulse`), and modulation order (`modulation_order`).

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
| 6      | [VPPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/VPPM_Modulator.md)                | Implements Variable Pulse Position Modulation (VPPM).                          |
| 7      | PPM_Modulator             | Implements Pulse Position Modulation (PPM), varying the position of pulse(s) within a symbol.                          |
