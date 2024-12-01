# OWC Channel Model (Absolute)

**Category:** Channel Models  

**Block Name:** OWC Channel Model(Absolute)

## Overview
The `OWC_Channel_Model(Absolute)` block in the `gr-owc` module provides an optical channel model for Optical Wireless Communication (OWC) systems. This block calculates the Line of Sight (LOS) path characteristics between multiple transmitters and receivers based on their respective 3D coordinates and orientations. Unlike the relative model, which requires explicit emission, acceptance angles and distance, this model derives these angles through the dot product of orientation vectors and coordinates vectors, thereby calculating the distances, emission angles, and acceptance angles.

## Parameters

The `OWC_Channel_Model(Absolute)` block is designed with the following configurable parameters to simulate the optical channel effectively:

| Parameter Name               | Description                                                                                     | Default Value  | Data Type        | Example Input                      |
|------------------------------|-------------------------------------------------------------------------------------------------|----------------------|------------------|-------------------------------------|
| `num_inputs`                 | Number of Transmitter(s)                                                                        | 1                   | `Integer`        | `2`                                 |
| `num_outputs`                | Number of Receiver(s)                                                                           | 1                   | `Integer`        | `3`                                 |
| `tx_coordinates_array`       | Array of 3D coordinates for each transmitter                                                    | `[0, 0, 0]`           | `Float array/vector` | For Tx₁(x₁, y₁, z₁) and Tx₂(x₂, y₂, z₂):   <br> `[x₁, y₁, z₁, x₂, y₂, z₂]` |
| `tx_orientation_array`       | Array of 3D orientation vectors for each transmitter                                            | `[0, 0, 1]`           | `Float array/vector` | For Tx₁(x₁, y₁, z₁) and Tx₂(x₂, y₂, z₂): <br> `[x₁, y₁, z₁, x₂, y₂, z₂]` |
| `rx_coordinates_array`       | Array of 3D coordinates for each receiver                                                       | `[1, 1, 1]`           | `Float array/vector` | For Rx₁(x₁, y₁, z₁) and Rx₂(x₂, y₂, z₂): <br>`[x₁, y₁, z₁, x₂, y₂, z₂]` |
| `rx_orientation_array`       | Array of 3D orientation vectors for each receiver                                               | `[0, 0, -1]`          | `Float array/vector` | For Rx₁(x₁, y₁, z₁) and Rx₂(x₂, y₂, z₂): <br>`[x₁, y₁, z₁, x₂, y₂, z₂]` |
| `tx_lambertian_order_array`  | Lambertian order for each transmitter $\( m \)$                                                          | `[1.0]`               | `Float array/vector` | For Tx₁ = 1.0 & Tx₂ = 2.0 : <br> `[1.0, 2.0]`                |
| `rx_photosensor_area_array`  | Photosensor area of each receiver $\( A_T \)$                                                              | `[1.0]`               | `Float array/vector` | For Rx₁ = 0.5, Rx₂ = 1.0: <br> `[0.5, 1.0]`|
| `optical_filter_transmittance_array` | Optical filter transmittance of each receiver $\( T_s \)$                                        | `[1.0]`               | `Float array/vector` | For Rx₁ = 1.0, Rx₂ = 1.5: <br> `[1.0, 1.5]` |
| `refractive_index_array`     | Refractive index of the concentrator lens for each receiver $\( n \)$                                    | `[1.0]`               | `Float array/vector` | For Rx₁ = 1.0, Rx₂ = 1.5: <br> `[1.0, 1.5]` |
| `concentrator_FOV_array`     | Field-of-view (FOV) $\( \Psi_C \)$ of the concentrator lens for each receiver                                 | `[90]`                | `Float array/vector` | For $\ \Psi_{C1} = 60, \Psi_{C2} = 45 \$: `[60, 45]`  |
| `E2O_conversion_factor_array` | Electrical-to-optical conversion factors for each transmitter $\( C_T \)$                               | `[1.0]`               | `Float array/vector` | For Tx₁ = 1.0 & Tx₂ = 2.0 : <br> `[1.0, 2.0]`  |
| `O2E_conversion_factor_array` | Optical-to-electrical conversion factors for each receiver $\( C_R \)$                                    | `[1.0]`               | `Float array/vector` | For Rx₁ = 1.0, Rx₂ = 1.5: <br> `[1.0, 1.5]`  |


## Description

The `OWC_Channel_Model(Absolute)` block calculates the emission, acceptance angles, and distances between transmitters and receivers based on the provided 3D coordinates and orientation vectors. 

The remaining calculations for channel gain and other related logic follow the same methodology as outlined in the OWC_Channel_model(Relative) block. For full details on the channel gain computations functions, refer to [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OWC_Channel_Model(Relative).md).

## Summary
The `OWC_Channel_Model(Absolute)` block simulates the optical wireless communication channel based on the spatial and angular configuration of transmitters and receivers. Using 3D coordinates and orientations, it dynamically calculates emission and acceptance angles, providing a tool for optical channel modeling.

## Examples:
(Comming soon)

# gr-owc
* [gr-owc](https://github.com/UCaNLabUMB/gr-owc/tree/main)
*  Blocks:
  
| Sl No. | Block Name                    | Description                                                                                               |
|--------|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1      | [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OWC_Channel_Model(Relative).md)    | Models the optical channel, considering DC channel gain from transmitter to receiver.                     |
| 2      | OWC_Channel_Block(Absolute)   | Models the optical channel using absolute coordinates of the transmitter and receiver, considering DC channel gain from transmitter to receiver. |
| 3      | [OOK_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OOK_Modulator.md)                  | Implements On-Off Keying (OOK) baseband modulation scheme.                                                |
| 4      | [OOK_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OOK_Demodulator.md)                | Demodulates On-Off Keying (OOK) baseband signals and defines the binary outcome.                          |
| 5      | [PAM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PAM_Modulator.md)                | Implements Pulse Amplitude Modulation (PAM), assigning varying amplitude levels based on symbols.           |
| 6      | [VPPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/VPPM_Modulator.md)                | Implements Variable Pulse Position Modulation (VPPM).                          |
| 7      | [PPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PPM_Modulator.md)                | Implements Pulse Position Modulation (PPM), varying the position of pulse(s) within a symbol.                          |
