# PAM Demodulator
Category: Signal Processing Blocks

Block Name: PAM Demodulator

## Overview
The `PAM_Demodulator` block in the `gr-owc` module implements **Pulse Amplitude Modulation (PAM) demodulation**. It recovers discrete symbols from an incoming amplitude-modulated signal by identifying the closest predefined amplitude level for each received symbol period.

This block performs the inverse operation of the [`PAM_Modulator`](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/PAM_Modulator.md). It processes a stream of amplitude samples and converts them back into symbols.

---

## Parameters

The `PAM_Demodulator` block uses the same configuration parameters as the PAM modulator to ensure correct symbol reconstruction:

| Parameter Name        | Description                                                                 | Default Value | Data Type   | Example Input | Condition                        |
|------------------------|-----------------------------------------------------------------------------|---------------|-------------|----------------|-----------------------------------|
| `modulation_order`     | Number of amplitude levels used in PAM                                     | `2`           | `Integer`   | `4`            | —            |
| `max_magnitude`        | Maximum expected amplitude of the received signal                          | `1.0`         | `Float`     | `2.0`          | `max_magnitude > min_magnitude`         |
| `min_magnitude`        | Minimum expected amplitude of the received signal                          | `0.0`         | `Float`     | `-1.0`         | —                                 |
| `samples_per_symbol`   | Number of samples representing one symbol period                           | `1`           | `Integer`   | `4`            | `samples_per_symbol > 0`         |

---

## Description

### Pulse Amplitude Demodulation
**Pulse Amplitude Modulation (PAM)** encodes data using discrete amplitude levels. The demodulator reconstructs transmitted symbols by analyzing the amplitude of the received signal over each symbol period.

The block operates as a decimator, consuming `samples_per_symbol` input samples for every output symbol. For each symbol interval, the incoming samples are grouped and averaged to small amplitude variations.

The averaged value is then compared against a predefined set of amplitude levels generated using:
- `modulation_order`
- `min_magnitude`
- `max_magnitude`

The closest matching level determines the recovered symbol index, which is emitted as the output.

To ensure accurate demodulation, the demodulator parameters should match those used by the corresponding modulator.

## Summary
The `PAM_Demodulator` block reconstructs symbols from a Pulse Amplitude Modulated signal by averaging samples over each symbol period and mapping the result to the nearest predefined amplitude level. It supports configurable modulation order, amplitude range, and symbol duration, making it suitable for simulation and experimental optical wireless communication systems.

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