# VPPM Demodulator
Category: Signal Processing Blocks

Block Name: VPPM Demodulator

## Overview
The `VPPM_Demodulator` block in the `gr-owc` module implements **Variable Pulse Position Modulation (VPPM) demodulation**. It recovers binary symbols from a received VPPM waveform by analyzing the position of pulses within each symbol period.

This block performs the inverse operation of the [`VPPM_Modulator`](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/VPPM_Modulator.md). It processes incoming samples representing pulse-shaped symbols and determines whether the pulse occurs in the early or late portion of the symbol interval.

---

## Parameters

The `VPPM_Demodulator` block includes the following configurable parameters:

| Parameter Name        | Description                                                                 | Default Value | Data Type   | Example Input | Condition                        |
|------------------------|-----------------------------------------------------------------------------|---------------|-------------|----------------|-----------------------------------|
| `samples_per_symbol`   | Number of samples representing one symbol duration                          | `1`           | `Integer`   | `32`           | `samples_per_symbol > 0`         |
| `samples_per_pulse`    | Number of samples used to represent the pulse width                         | `1`           | `Integer`   | `8`            | `samples_per_pulse ≤ samples_per_symbol` |

---

## Description

### Variable Pulse Position Demodulation
**Variable Pulse Position Modulation (VPPM)** encodes data using the position of a pulse within a symbol interval while allowing adjustable pulse widths. In optical wireless systems, this enables both communication and dimming control.

The demodulator reconstructs transmitted bits by identifying where the pulse occurs within each symbol period.

The block operates as a decimator, consuming `samples_per_symbol` input samples for each output bit. For every symbol window, the received samples are grouped and evaluated using a matched-filter-style comparison.

Two reference pulse templates are internally constructed:

- **Case 0 (early pulse)**: Pulse located at the beginning of the symbol interval  
- **Case 1 (late pulse)**: Pulse located at the end of the symbol interval  

The received samples are compared against both templates using correlation. The template that produces the higher correlation determines the detected symbol.

This matched-filter approach improves robustness to noise and timing variations by evaluating the overall pulse shape rather than relying on a single threshold.

To ensure accurate demodulation, the demodulator parameters should match those used by the corresponding modulator.

---

## Summary
The `VPPM_Demodulator` block recovers binary data from a Variable Pulse Position Modulated signal by detecting the relative position of pulses within each symbol period. It supports configurable symbol duration and pulse width, making it suitable for optical wireless communication systems that combine data transmission with illumination control.

---

## Examples
(Coming soon)

# gr-owc
* [gr-owc](https://github.com/UCaNLabUMB/gr-owc/tree/main)
* Blocks:

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