# OOK Demodulator
Category: Signal Processing Blocks

Block Name: OOK Demodulator

## Overview
The `OOK_Demodulator` block implements On-Off Keying (OOK) demodulation, a method for converting an OOK-modulated signal back into binary data. It compares the average of a set of incoming signal values against a predefined threshold to determine the binary outcome.

## Parameters

The `OOK_Demodulator` block has the following configurable parameters:

| Parameter Name        | Description                                             | Default Value   | Data Type   | Condition           |
|-----------------------|---------------------------------------------------------|-----------------|-------------|----------------------|
| `threshold`           | Threshold value used for binary decision (0 or 1)       | `0.5`           | `Float`     | —                    |
| `samples_per_symbol`  | Number of samples per symbol                            | `1`             | `Integer`   | `> 0`                |

## Description
### OOK: Demodulation Process
The `OOK_Demodulator` block recovers binary data from the OOK-modulated signals by comparing the average value of incoming signal samples for each symbol with the `threshold` parameter. If the average value of the samples is greater than the threshold, the block outputs a binary "1". Otherwise, it outputs a binary "0".

### Samples Per Symbol
The `samples_per_symbol` parameter defines the number of samples used to represent each symbol. This parameter must match the `samples_per_symbol` value used in the modulator block for proper demodulation.

### Threshold
The `threshold` parameter allows users to set the decision threshold for demodulation. It defines the boundary between the "On" and "Off" states.

## Summary
The `OOK_Demodulator` block provides a way to recover binary data from an OOK-modulated signal, making it ideal for OWC systems. With adjustable parameters such as `threshold` and `samples_per_symbol`, this block offers flexibility for various communication scenarios.

## Examples:
(Comming soon)

# gr-owc
* [gr-owc](https://github.com/UCaNLabUMB/gr-owc/tree/main)
*  Blocks:
  
| Sl No. | Block Name                    | Description                                                                                               |
|--------|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1      | [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OWC_Channel_Model(Relative).md)   | Models the optical channel, considering DC channel gain from transmitter to receiver.                     |
| 2      | [OWC_Channel_Block(Absolute)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OWC_Channel_Block(Absolute).md)    | Models the optical channel using absolute coordinates of the transmitter and receiver, considering DC channel gain from transmitter to receiver. |
| 3      | [OOK_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OOK_Modulator.md)                  | Implements On-Off Keying (OOK) baseband modulation scheme.                                                |
| 4      | OOK_Demodulator               | Demodulates On-Off Keying (OOK) baseband signals and defines the binary outcome.                          |
| 5      | [PAM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PAM_Modulator.md)                | Implements Pulse Amplitude Modulation (PAM), assigning varying amplitude levels based on symbols.           |
| 6      | [VPPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/VPPM_Modulator.md)                | Implements Variable Pulse Position Modulation (VPPM).                          |
| 7      | [PPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PPM_Modulator.md)                | Implements Pulse Position Modulation (PPM), varying the position of pulse(s) within a symbol.                          |
| 8      | [LED_Nonlinearity](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/LED_Nonlinearity.md)            | Models the non-linear function of an LED  |
| 9      | [Hermitian Symmetry (Same Vec Size I/O)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/Hermitian_Symmetry_i_o_same_vec_size.md) | Ensures Hermitian symmetry in complex-valued FFT vectors, keeping input and output vector sizes equal.    |
