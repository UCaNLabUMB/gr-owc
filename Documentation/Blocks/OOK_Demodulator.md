# OOK Demodulator
Category: Signal Processing Blocks

Block Name: OOK Demodulator

## Overview
The `OOK_Demodulator` block implements On-Off Keying (OOK) demodulation, a method for converting an OOK-modulated signal back into binary data. It compares the average of a set of incoming signal values against a predefined threshold to determine the binary outcome.

## Parameters

The `OOK_Demodulator` block has the following configurable parameters:

| Parameter Name        | Description                                             | Default Value   | Data Type   |
|-----------------------|---------------------------------------------------------|-----------------|-------------|
| `threshold`           | Threshold value used for binary decision (0 or 1)       | 0.5             | `Float`     |
| `samples_per_symbol`  | Number of samples per symbol                            | 1               | `Integer`   |

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
...

# gr-owc
* [Overview](gr-owc_Overview.md)
* Blocks:

| Sl No.   | Block         | Description         |
|-----------------|-----------------|-----------------|
| 1 | [OWC_Channel Model (Relative)](OWC_Channel_Model(Relative).md) | Models the optical channel, considering DC channel gain from transmitter to receiver. |
| 2 | [OOK_Modulator](OOK_Modulator.md) | Implements On-Off Keying (OOK) baseband modulation scheme. |
| 3 | OOK_Demodulator | Recovers binary data by demodulating OOK-modulated signals. |
