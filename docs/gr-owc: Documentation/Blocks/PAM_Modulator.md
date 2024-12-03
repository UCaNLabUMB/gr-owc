# PAM Modulator
Category: Signal Processing Blocks

Block Name: PAM Modulator

## Overview
The `PAM_Modulator` block in the `gr-owc` module implements **Pulse Amplitude Modulation (PAM)**. PAM modulates discrete symbols by assigning each one to a unique amplitude level in the domain. This process generates a signal suitable for transmission over communication channels.

This block works with the `Chunk to Symbols` block, which maps input data (typically bits or bytes) into integer symbols. The `PAM_Modulator` then converts these symbols into amplitude levels.

---

## Parameters

The `PAM_Modulator` block is designed with the following configurable parameters to simulate the PAM effectively:

| Parameter Name         | Description                                                                 | Default Value | Data Type       | Example Input |
|------------------------|-----------------------------------------------------------------------------|---------------|-----------------|---------------|
| `modulation_order`     | Number of distinct amplitude levels.  | `2`           | `Integer`       | `4`           |
| `max_magnitude`        | Maximum amplitude of the modulated signal.                                  | `1.0`         | `Float`         | `2.0`         |
| `min_magnitude`        | Minimum amplitude of the modulated signal.                                  | `0.0`         | `Float`         | `-1.0`        |
| `samples_per_symbol`   | Number of output samples per symbol (symbol duration).                      | `1`           | `Integer`       | `4`           |

---

## Description

### Pulse Amplitude Modulation (PAM) for Signal Processing
**Pulse Amplitude Modulation (PAM)** represents data as discrete amplitude levels of a pulse waveform. Each symbol is mapped to one of $\( M \)$ amplitude levels, where $\( M \)$ is the modulation order. PAM is an efficient way to transmit data over channels and is used in applications like optical wireless communications. The amplitude levels are distributed linearly between the `min_magnitude` and `max_magnitude` parameters.

In PAM, the amplitude levels directly affect the brightness of the LED in optical communication systems. Higher amplitude levels correspond to higher optical intensity, allowing PAM to modulate the brightness of the LED for the channel model. By varying the amplitude, the LED can emit light at different intensities, transmission. This feature makes PAM particularly suitable for visible light communication, where brightness modulation translates directly into optical signal variations.

The `PAM_Modulator` works in along with the `Chunk to Symbols` block. This block converts input data into integer symbols, where each symbol corresponds to one amplitude level in the PAM block. The `Chunk to Symbols` block outputs a stream of symbols, which are then fed to the `PAM_Modulator` for amplitude mapping and signal generation.

The `PAM_Modulator` translates input symbols into linearly spaced amplitude levels. The number of levels is determined by the `modulation_order` parameter $\( M \)$, and the range of amplitudes is defined by `min_magnitude` and `max_magnitude`. The duration of each symbol in the output signal is controlled by `samples_per_symbol`.

## Summary

The `PAM_Modulator` block generates Pulse Amplitude Modulation (PAM) signals by mapping discrete symbols to corresponding amplitude levels based on the specified modulation order. It supports configurable parameters such as the number of amplitude levels, amplitude range, and symbol duration. This block is essential for simulating and implementing PAM in communication systems, providing flexibility for modulation schemes and transmission requirements.

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
| 5      | PAM_Modulator               | Implements Pulse Amplitude Modulation (PAM), assigning varying amplitude levels based on symbols.           |
| 6      | [VPPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/VPPM_Modulator.md)                | Implements Variable Pulse Position Modulation (VPPM).                          |
| 7      | [PPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PPM_Modulator.md)                | Implements Pulse Position Modulation (PPM), varying the position of pulse(s) within a symbol.                          |
