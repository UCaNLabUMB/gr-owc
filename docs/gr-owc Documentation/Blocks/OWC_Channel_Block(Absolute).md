# OWC Channel Model (Absolute)

**Category:** Channel Models  

**Block Name:** OWC Channel Model(Absolute)

## Overview
The `OWC_Channel_Model(Absolute)` block in the `gr-owc` module provides an optical channel model for Optical Wireless Communication (OWC) systems. This block calculates the Line of Sight (LOS) path characteristics between multiple transmitters and receivers based on their respective 3D coordinates and orientations. Unlike the relative model, which requires explicit emission, acceptance angles and distance, this model derives these angles through the dot product of orientation vectors and coordinates vectors, thereby calculating the distances, emission angles, and acceptance angles.

## Parameters

The `OWC_Channel_Model(Absolute)` block is designed with the following configurable parameters to simulate the optical channel effectively:

| Parameter Name                   | Description                                                                                   | Default Value     | Data Type           | Example Input                                  | Condition                                                                 |
|----------------------------------|-----------------------------------------------------------------------------------------------|-------------------|---------------------|------------------------------------------------|---------------------------------------------------------------------------|
| `num_inputs`                     | Number of Transmitter(s)                                                                      | `1`               | Integer              | `2`                                            | > 0                                                                       |
| `num_outputs`                    | Number of Receiver(s)                                                                         | `1`               | Integer              | `3`                                            | > 0                                                                       |
| `tx_coordinates_array`          | 3D coordinates of each transmitter                                                            | `[1.0, 2.0, 5.0]`  | Float array/vector   | `[x₁, y₁, z₁, x₂, y₂, z₂]`                     | `len = num_inputs × 3`                                                   |
| `tx_orientation_array`          | 3D orientation vectors for each transmitter                                                   | `[0.0, 0.0, -1.0]` | Float array/vector   | `[x₁, y₁, z₁, x₂, y₂, z₂]`                     | `len = num_inputs × 3`, not all-zero vectors                             |
| `rx_coordinates_array`          | 3D coordinates of each receiver                                                               | `[2.0, 2.0, 0.0]`  | Float array/vector   | `[x₁, y₁, z₁, x₂, y₂, z₂]`                     | `len = num_outputs × 3`                                                  |
| `rx_orientation_array`          | 3D orientation vectors for each receiver                                                      | `[0.0, 0.0, 1.0]`  | Float array/vector   | `[x₁, y₁, z₁, x₂, y₂, z₂]`                     | `len = num_outputs × 3`, not all-zero vectors                            |
| `tx_lambertian_order_array`     | Lambertian order $\( m \)$ for each transmitter                                                 | `[2.0]`           | Float array/vector   | `[1.0, 2.0]`                                   | `len = num_inputs`                                                       |
| `rx_photosensor_area_array`     | Photosensor area $\( A_T \)$ of each receiver                                                   | `[1.0]`           | Float array/vector   | `[0.5, 1.0]`                                   | `len = num_outputs`                                                      |
| `optical_filter_transmittance_array` | Optical filter transmittance $\( T_s \)$ for each receiver                               | `[1.0]`           | Float array/vector   | `[1.0, 1.5]`                                   | `len = num_outputs`                                                      |
| `refractive_index_array`        | Refractive index $\( n \)$ of the concentrator for each receiver                                | `[1.0]`           | Float array/vector   | `[1.0, 1.5]`                                   | `len = num_outputs`                                                      |
| `clip_neg`                      | Clip negative received optical power values                                                   | `True`            | Bool                 | `True`                                         | —                                                                         |
| `shot_noise`                    | Enable shot noise simulation                                                                  | `False`           | Bool                 | `False`                                        | —                                                                         |
| `sample_rate`                   | Sample rate of the system                                                                     | `samp_rate`       | Float                | `1e6`                                          | —                                                                         |
| `responsivity`                  | Photodiode responsivity $\( R \)$ (A/W)                                                         | `1.0`             | Float                | `0.8`                                          | `≥ 0`                                                                     |
| `concentrator_FOV_array`        | Field-of-view $\( \Psi_C \)$ for each receiver's concentrator                                   | `[90.0]`          | Float array/vector   | `[60.0, 45.0]`                                 | `0 ≤ values ≤ 90`, `len = num_outputs`                                   |
| `E2O_conversion_factor_array`   | Electrical-to-optical conversion factors $\( C_T \)$ for each transmitter                       | `[1.0]`           | Float array/vector   | `[1.0, 2.0]`                                   | `len = num_inputs`                                                       |
| `O2E_conversion_factor_array`   | Optical-to-electrical conversion factors $\( C_R \)$ for each receiver                          | `[1.0]`           | Float array/vector   | `[1.0, 1.5]`                                   | `len = num_outputs`                                                      |


## Description

The `OWC_Channel_Model(Absolute)` block calculates the emission, acceptance angles, and distances between transmitters and receivers based on the provided 3D coordinates and orientation vectors. 

The remaining calculations for channel gain and other related logic follow the same methodology as outlined in the OWC_Channel_model(Relative) block. For full details on the channel gain computations functions, refer to [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OWC_Channel_Model(Relative).md).

## Summary
The `OWC_Channel_Model(Absolute)` block simulates the optical wireless communication channel based on the spatial and angular configuration of transmitters and receivers. Using 3D coordinates and orientations, it dynamically calculates emission and acceptance angles, providing a tool for optical channel modeling.

## Examples:
(Comming soon)

# gr-owc
* [gr-owc](https://github.com/UCaNLabUMB/gr-owc/tree/main)
*  Blocks:
  
| Sl No. | Block Name                    | Description                                                                                               |
|--------|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1      | [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OWC_Channel_Model(Relative).md)    | Models the optical channel, considering DC channel gain from transmitter to receiver.                     |
| 2      | OWC_Channel_Block(Absolute)   | Models the optical channel using absolute coordinates of the transmitter and receiver, considering DC channel gain from transmitter to receiver. |
| 3      | [OOK_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OOK_Modulator.md)                  | Implements On-Off Keying (OOK) baseband modulation scheme.                                                |
| 4      | [OOK_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/OOK_Demodulator.md)                | Demodulates On-Off Keying (OOK) baseband signals and defines the binary outcome.                          |
| 5      | [PAM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/PAM_Modulator.md)                | Implements Pulse Amplitude Modulation (PAM), assigning varying amplitude levels based on symbols.           |
| 6      | [VPPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/VPPM_Modulator.md)                | Implements Variable Pulse Position Modulation (VPPM).                          |
| 7      | [PPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/PPM_Modulator.md)                | Implements Pulse Position Modulation (PPM), varying the position of pulse(s) within a symbol.                          |
| 8      | [LED_Nonlinearity](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/LED_Nonlinearity.md)            | Models the non-linear function of an LED  |
| 9      | [Hermitian Symmetry (Same Vec Size I/O)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%20Documentation/Blocks/Hermitian_Symmetry_i_o_same_vec_size.md) | Ensures Hermitian symmetry in complex-valued FFT vectors, keeping input and output vector sizes equal.    |
