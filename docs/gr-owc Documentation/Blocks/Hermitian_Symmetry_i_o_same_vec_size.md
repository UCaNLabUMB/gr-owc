# Hermitian Symmetry (Same Vec Size I/O)
**Category:** Signal Processing Blocks  
**Block Name:** Hermitian Symmetry (Same Vec Size I/O)

## Overview

The `Hermitian_Symmetry_i_o_same_vec_size` block in the `gr-owc` module ensures that the output vector has Hermitian symmetry. This is required when generating real-valued signals in the time domain via IFFT from frequency-domain data. The key aspect of this block is that **the input and output vectors have the same length**, and it inserts or enforces symmetry in-place.

## Parameters

| Parameter Name             | Description                                         | Default Value | Data Type | Example Input | Condition                  |
|----------------------------|-----------------------------------------------------|----------------|------------|----------------|-----------------------------|
| `fft_len`                  | Length of the FFT vector                    | `32`           | `Integer`  | `64`           | > 0, Even number |
| `use_negative_coefficients`| Switch whether to use positive or negative coefficents values to generate symmetry   | `False`        | `Bool`     | `True`         | —                           |

---

## Description

In frequency-domain signal processing, to produce **real-valued time-domain signals** via IFFT, the frequency-domain vector must satisfy Hermitian symmetry.

## Summary

The `Hermitian Symmetry (Same Vec Size I/O)` block transforms a complex vector into its Hermitian-symmetric version in-place. It is primarily used to prepare frequency-domain signals for real-valued IFFT.

# gr-owc
* [gr-owc](https://github.com/UCaNLabUMB/gr-owc/tree/main)
*  Blocks:
  
| Sl No. | Block Name                    | Description                                                                                               |
|--------|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1      | [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OWC_Channel_Model(Relative).md)    | Models the optical channel, considering DC channel gain from transmitter to receiver.                     |
| 2      | [OWC_Channel_Block(Absolute)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OWC_Channel_Block(Absolute).md)    | Models the optical channel using absolute coordinates of the transmitter and receiver, considering DC channel gain from transmitter to receiver. |
| 3      | [OOK_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OOK_Modulator.md)                  | Implements On-Off Keying (OOK) baseband modulation scheme.                                                |
| 4      | [OOK_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OOK_Demodulator.md)                | Demodulates On-Off Keying (OOK) baseband signals and defines the binary outcome.                          |
| 5      | [PAM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/PAM_Modulator.md)                | Implements Pulse Amplitude Modulation (PAM), assigning varying amplitude levels based on symbols.           |
| 6      | [VPPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/VPPM_Modulator.md)                | Implements Variable Pulse Position Modulation (VPPM).                          |
| 7      | [PPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/PPM_Modulator.md)                | Implements Pulse Position Modulation (PPM), varying the position of pulse(s) within a symbol.                          |
| 8      | [LED_Nonlinearity](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/LED_Nonlinearity.md)            | Models the non-linear function of an LED  |
| 9      | Hermitian Symmetry (Same Vec Size I/O) | Ensures Hermitian symmetry in complex-valued FFT vectors, keeping input and output vector sizes equal.    |
