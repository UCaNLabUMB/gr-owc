# LED-Nonlinearity
**Category:** LED 

**Block Name:** LED Non-Linearity

## Overview
The `LED Non-Linearity` block in the `gr-owc` module simulates the non-linear behavior of a Light Emitting Diode (LED) using a sigmoid-like transfer function. This is useful for modeling practical limitations of LEDs in optical wireless communication systems where the output intensity does not linearly follow the input signal.

## Parameters

| Parameter Name     | Description                                              | Default Value | Data Type | Example Input | Condition     |
|--------------------|----------------------------------------------------------|----------------|------------|----------------|----------------|
| `L`                | Maximum output level of the LED                         | `1.0`          | `Float`    | `2.0`          | —            |
| `k`                | Steepness of the non-linear transition                   | `1.0`          | `Float`    | `5.0`          | —            |
| `x0`               | Inflection point of the sigmoid curve                    | `0.0`          | `Float`    | `0.5`          | —              |

## Description

The block transforms an input signal $\( x(t) \)$ using the following sigmoid function:

$$
y(t) = \frac{L}{1 + e^{-k(x(t) - x_0)}}
$$

- $\( L \)$: The maximum value the LED can output (saturation level).
- $\( k \)$: Determines how sharp the transition from low to high output is.
- $\( x_0 \)$: The center of the transition or the inflection point.

## Summary

The `LED_Nonlinearity` block introduces realistic LED non-linear behavior into your optical system simulation.

## Examples:
(Comming soon)

# gr-owc
* [gr-owc](https://github.com/UCaNLabUMB/gr-owc/tree/main)
*  Blocks:

| Sl No. | Block Name                    | Description                                                                                               |
|--------|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1      | [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OWC_Channel_Model(Relative).md)    | Models the optical channel, considering DC channel gain from transmitter to receiver.                     |
| 2      | [OWC_Channel_Block(Absolute)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OWC_Channel_Block(Absolute).md)   | Models the optical channel using absolute coordinates of the transmitter and receiver, considering DC channel gain from transmitter to receiver. |
| 3      | [OOK_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OOK_Modulator.md)                  | Implements On-Off Keying (OOK) baseband modulation scheme.                                                |
| 4      | [OOK_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OOK_Demodulator.md)                | Demodulates On-Off Keying (OOK) baseband signals and defines the binary outcome.                          |
| 5      | [PAM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PAM_Modulator.md)                | Implements Pulse Amplitude Modulation (PAM), assigning varying amplitude levels based on symbols.           |
| 6      | [VPPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/VPPM_Modulator.md)                | Implements Variable Pulse Position Modulation (VPPM).                          |
| 7      | [PPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PPM_Modulator.md)                | Implements Pulse Position Modulation (PPM), varying the position of pulse(s) within a symbol.                          |
| 8      | LED_Nonlinearity           | Models the non-linear function of an LED  |
| 9      | [Hermitian Symmetry (Same Vec Size I/O)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/Hermitian_Symmetry_i_o_same_vec_size.md) | Ensures Hermitian symmetry in complex-valued FFT vectors, keeping input and output vector sizes equal.    |
