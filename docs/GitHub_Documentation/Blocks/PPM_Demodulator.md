# PPM Demodulator
Category: Signal Processing Blocks

Block Name: PPM Demodulator

## Overview
The `PPM_Demodulator` block in the `gr-owc` module implements **Pulse Position Modulation (PPM) demodulation**, where symbols are recovered by detecting the position of pulses within a symbol duration. This block is commonly used in optical wireless communication systems and other digital communication applications using position-based modulation schemes.

The `PPM_Demodulator` performs the inverse operation of the [`PPM_Modulator`](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/PAM_Modulator.md), reconstructing transmitted symbols by analyzing the received waveform and determining the pulse location within each symbol period.

## Parameters

The `PPM_Demodulator` block is designed with the following configurable parameters to correctly decode PPM signals:

| Parameter Name        | Description                                                                 | Default Value | Data Type   | Example Input | Condition                                     |
|------------------------|-----------------------------------------------------------------------------|---------------|-------------|----------------|-----------------------------------------------|
| `samples_per_symbol`   | Total number of samples in each symbol period                               | `8`           | `Integer`   | `16`           | `> 0`                                         |
| `samples_per_pulse`    | Number of consecutive samples representing the pulse width                 | `1`           | `Integer`   | `4`            | `> 0 and < samples_per_symbol`               |
| `modulation_order`     | Number of possible pulse positions (symbol levels)                          | `2`           | `Integer`   | `4`            | `> 1`                                         |


## Description

### Pulse Position Demodulation
Pulse Position Modulation (PPM) encodes information using the position of a pulse within a fixed symbol duration. The demodulator reconstructs transmitted symbols by determining which pulse position contains the highest signal energy.

The received input stream is divided into segments of length `samples_per_symbol`, where each segment represents one symbol interval.

### Pulse Position Detection
For a given modulation order $\( M \)$, there are $\( M \)$ possible pulse locations within each symbol. The demodulator evaluates all possible pulse positions and identifies the position that best matches the received signal.

This approach allows robust detection even in the presence of noise or slight waveform distortions by analyzing the entire symbol duration rather than relying on a single sample.

### Symbol Reconstruction
- The detected pulse position directly corresponds to the recovered symbol value.
- The output is an symbol in the range $\( 0 \)$ to $\( M - 1 \)$.

To ensure correct decoding, the demodulator parameters should match those used during modulation, particularly the symbol duration and pulse width.

---

## Summary

The `PPM_Demodulator` block reconstructs symbols from Pulse Position Modulated signals by detecting the position of pulses within each symbol duration. It supports configurable symbol length, pulse width, and modulation order, making it suitable for optical wireless communication systems and other applications using position-based modulation schemes.

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
