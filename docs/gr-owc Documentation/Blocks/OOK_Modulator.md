# OOK Modulator
Category: Signal Processing Blocks

Block Name: OOK Modulator

## Overview
The `OOK_Modulator` block implements On-Off Keying (OOK), a baseband modulation technique used in optical wireless communication. This simple modulation scheme switches between two levels—typically `max_mag` and `min_mag`—to represent binary data.

## Parameters

The `OOK_Modulator` block has the following configurable parameters:

| Parameter Name        | Description                                             | Default Value   | Data Type   | Condition                        |
|-----------------------|---------------------------------------------------------|-----------------|-------------|-----------------------------------|
| `max_mag`             | Maximum magnitude for the "On" state                    | `1.0`           | `Float`     | `max_mag > min_mag`              |
| `min_mag`             | Minimum magnitude for the "Off" state                   | `0.0`           | `Float`     | —                                 |
| `samples_per_symbol`  | Number of samples per symbol                            | `1`             | `Integer`   | `samples_per_symbol > 0`         |

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
* [gr-owc](https://github.com/UCaNLabUMB/gr-owc/tree/main)
*  Blocks:

| Sl No. | Block Name | Description |
|--------|------------|-------------|
| 1 | [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OWC_Channel_Model(Relative).md) | Models the optical channel using relative positioning between transmitter and receiver. |
| 2 | [OWC_Channel_Block(Absolute)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OWC_Channel_Block(Absolute).md) | Models the optical channel using absolute coordinates. |
| 3 | [OOK_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OOK_Modulator.md) | Implements On-Off Keying (OOK) modulation. |
| 4 | [OOK_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OOK_Demodulator.md) | Recovers binary data from OOK signals. |
| 5 | [PAM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/PAM_Modulator.md) | Implements Pulse Amplitude Modulation (PAM). |
| 6 | [PAM_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/PAM_Demodulator.md) | Recovers symbols from PAM signals using amplitude detection. |
| 7 | [VPPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/VPPM_Modulator.md) | Implements Variable Pulse Position Modulation (VPPM). |
| 8 | [VPPM_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/VPPM_Demodulator.md) | Recovers binary symbols by detecting pulse position in VPPM signals. |
| 9 | [PPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/PPM_Modulator.md) | Implements Pulse Position Modulation (PPM). |
| 10 | [PPM_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/PPM_Demodulator.md) | Recovers symbols by detecting pulse position in PPM signals. |
| 11 | [LED_Nonlinearity](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/LED_Nonlinearity.md) | Models LED non-linear behavior in optical systems. |
| 12 | [Hermitian Symmetry (Same Vec Size I/O)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/Hermitian_Symmetry_i_o_same_vec_size.md) | Ensures Hermitian symmetry in FFT vectors. |
