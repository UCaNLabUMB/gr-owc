# OWC Channel Model(Relative)
Category: Channel Models

Block Name: OWC Channel Model(Relative)

## Overview
The `OWC_Channel_Model(Relative)` block in the `gr-owc` module simulates the optical channel's behavior in optical wireless communication (OWC) systems. This block models the relationship between the electrical signals from 𝑁 transmitters and the corresponding electrical signals received at 𝑀 receivers. It accounts for emission and acceptance angles, as well as distances between each of the 𝑁 𝑀 transmitter-receiver pairs. The Lambertian orders, which describe the directional emission characteristics of the 𝑁 transmitters, are parameterized. On the receiver side, parameters such as the photosensor area, optical filter gain, refractive index, and concentrator field-of-view (FOV) are defined for each of the 𝑀 receivers. Additionally, conversion factors for both electrical-to-optical and optical-to-electrical processes are specified for all 𝑁 transmitters and 𝑀 receivers.

## Parameters

The `OWC_Channel_Model(Relative)` block is designed with the following configurable parameters to simulate the optical channel effectively:

| Parameter Name                   | Description                                                                                          | Default Value       | Data Type           | Example Input                            | Condition                                      |
|----------------------------------|------------------------------------------------------------------------------------------------------|---------------------|---------------------|------------------------------------------|-------------------------------------------------|
| `num_inputs`                     | Number of Transmitter(s)                                                                             | `1`                 | Integer              | `2`                                      | > 0                                             |
| `num_outputs`                    | Number of Receiver(s)                                                                                | `1`                 | Integer              | `3`                                      | > 0                                             |
| `acceptance_angle_array`         | Acceptance angles $\( \psi_{ij} \)$ of the receivers (degrees)                                         | `[1.0]`             | Float array          | `[20.0, 25.0]`                           | len = num_inputs × num_outputs                 |
| `emission_angle_array`           | Emission angles $\( \phi_{ij} \)$ from transmitters to receivers (degrees)                            | `[1.0]`             | Float array          | `[20.0, 25.0]`                           | len = num_inputs × num_outputs                 |
| `distance_array`                 | Distances $\( d_{ij} \)$ between transmitter-receiver pairs                                           | `[1.0]`             | Float array          | `[2.0, 2.5]`                             | len = num_inputs × num_outputs                 |
| `lambertian_order_array`         | Lambertian emission orders $\( m \)$                                                                   | `[1.0]`             | Float array          | `[1.0, 2.0]`                             | len = num_inputs                               |
| `photosensor_area_array`         | Photosensor areas $\( A_T \)$                                                                          | `[1.0]`             | Float array          | `[0.5, 1.0]`                             | len = num_outputs                              |
| `optical_filter_transmittance_array` | Optical filter transmittances $\( T_s \)$                                                        | `[1.0]`             | Float array          | `[1.0, 1.5]`                             | len = num_outputs                              |
| `refractive_index_array`         | Refractive index $\( n \)$ of the concentrator lens                                                  | `[1.0]`             | Float array          | `[1.0, 1.5]`                             | len = num_outputs                              |
| `clip_neg`                       | Clip negative received optical power values                                                          | `True`              | Bool                 | `True`                                   | —                                               |
| `shot_noise`                     | Enable shot noise simulation                                                                         | `False`             | Bool                 | `False`                                  | —                                               |
| `sample_rate`                    | Sample rate of the system                                                                            | `samp_rate`         | Float                | `1e6`                                    | —                                               |
| `responsivity`                   | Photodiode responsivity $\( R \)$ (A/W)                                                               | `1.0`               | Float                | `0.8`                                    | ≥ 0                                             |
| `concentrator_FOV_array`         | Field-of-view $\( \Psi_C \)$ of the concentrator lens                                                 | `[90]`              | Float array          | `[60, 45]`                               | 0 ≤ values ≤ 90, len = num_outputs             |
| `E2O_conversion_factor_array`    | Electrical-to-optical conversion factors $\( C_T \)$                                                 | `[1.0]`             | Float array          | `[1.0, 2.0]`                             | len = num_inputs                               |
| `O2E_conversion_factor_array`    | Optical-to-electrical conversion factors $\( C_R \)$                                                 | `[1.0]`             | Float array          | `[1.0, 1.5]`                             | len = num_outputs                              |


## Description

### DC Channel Gain Formula
The DC channel gain from transmitter \( i \) to receiver \( j \) is given by:

$$
H_{ij} = \frac{G_T(\phi_{ij}) \cdot G_R(\psi_{ij})}{d_{ij}^2}
$$

where:
- $\( \phi_{ij} \)$ is the emission angle from transmitter i to receiver j.
- $\( \psi_{ij} \)$ is the acceptance angle of receiver j.
- $\( d_{ij} \)$ is the distance between transmitter i and receiver j.
- $\( G_T(\phi_{ij}) \)$ and $\( G_R(\psi_{ij}) \)$ are the transmit and receive gains as functions of the emission and reception angles, respectively.

### Transmit and Receive Gain Functions
For the commonly used point source model with Lambertian emission, the gain functions are defined as follows:

- **Transmit Gain $\( G_T(\phi_{ij}) \)$**:

$$
G_T(\phi) = \frac{m + 1}{2 \pi} \cdot \cos^m(\phi)
$$

where \( m \) is the Lambertian order.

- **Receive Gain $\( G_R(\psi_{ij}) \)$**:

$$
G_R(\psi) = A_T \cdot T_s \cdot g(\psi) \cdot \cos(\psi)
$$

where:
- $\( A_T \)$ is the photosensor area.
- $\( T_s \)$ is the optical filter transmittance.
- $\( g(\psi) \)$ is the gain function for a concentrator lens, given by:

$$
g(\psi) = \frac{n^2}{\sin^2(\Psi_C)} \text{ for } 0 \leq \psi \leq \Psi_C
$$

and 0 otherwise, where \( n \) is the refractive index and $\( \Psi_C \)$ is the field-of-view (FOV) of the lens.

### Signal Power and Conversion Factors
In a system with multiple transmitters and receivers, the total optical signal power incident on a given receiver’s photosensor is the sum of the received power from all transmitters. To account for the conversion between electrical and optical domains, we assume that the conversion factors $\( C_T \)$ (electrical to optical) and $\( C_R \)$ (optical to electrical) are constants. The received electrical signal is related to the transmitted signal by the constant factor $\( C_T \cdot C_R \cdot H_{ij} \)$.

The received signal at receiver \( j \) is:

$$
y(t) = \sum_i C_T^{(i)} \cdot C_R^{(j)} \cdot H_{ij} \cdot x(t)
$$

where $\( x(t) \)$ is the transmitted signal.

### Shot Noise Modeling
When `shot_noise = True`, the block simulates **photon shot noise** by adding random noise proportional to the received signal power. This provides a more realistic model of optical receptions.


## Summary
The `OWC_Channel_Model(Relative)` block in the `gr-owc` module provides a detailed simulation of the optical channel by focusing on the dominant LOS path and modeling its impact using DC channel gain and angle-dependent gain functions. This block helps in understanding and predicting the behavior of optical wireless communication systems in various scenarios.

## Examples:
(Comming soon)

# gr-owc
* [gr-owc](https://github.com/UCaNLabUMB/gr-owc/tree/main)
*  Blocks:
  
| Sl No. | Block Name                    | Description                                                                                               |
|--------|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1      | OWC_Channel_Block(Relative)   | Models the optical channel, considering DC channel gain from transmitter to receiver.                     |
| 2      | [OWC_Channel_Block(Absolute)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OWC_Channel_Block(Absolute).md)    | Models the optical channel using absolute coordinates of the transmitter and receiver, considering DC channel gain from transmitter to receiver. |
| 3      | [OOK_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OOK_Modulator.md)                  | Implements On-Off Keying (OOK) baseband modulation scheme.                                                |
| 4      | [OOK_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/OOK_Demodulator.md)                | Demodulates On-Off Keying (OOK) baseband signals and defines the binary outcome.                          |
| 5      | [PAM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PAM_Modulator.md)                | Implements Pulse Amplitude Modulation (PAM), assigning varying amplitude levels based on symbols.           |
| 6      | [VPPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/VPPM_Modulator.md)                | Implements Variable Pulse Position Modulation (VPPM).                          |
| 7      | [PPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/PPM_Modulator.md)                | Implements Pulse Position Modulation (PPM), varying the position of pulse(s) within a symbol.                          |
| 8      | [LED_Nonlinearity](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/LED_Nonlinearity.md)            | Models the non-linear function of an LED  |
| 9      | [Hermitian Symmetry (Same Vec Size I/O)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/gr-owc%3A%20Documentation/Blocks/Hermitian_Symmetry_i_o_same_vec_size.md) | Ensures Hermitian symmetry in complex-valued FFT vectors, keeping input and output vector sizes equal.    |
