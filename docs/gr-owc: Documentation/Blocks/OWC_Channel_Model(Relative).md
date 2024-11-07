# OWC Channel Model(Relative)
Category: Channel Models

Block Name: OWC Channel Model(Relative)

## Overview
The `OWC_Channel_Model(Relative)` block in the `gr-owc` module simulates the optical channel's behavior in optical wireless communication (OWC) systems. This block models the relationship between the electrical signals from 𝑁 transmitters and the corresponding electrical signals received at 𝑀 receivers. It accounts for emission and acceptance angles, as well as distances between each of the 𝑁 𝑀 transmitter-receiver pairs. The Lambertian orders, which describe the directional emission characteristics of the 𝑁 transmitters, are parameterized. On the receiver side, parameters such as the photosensor area, optical filter gain, refractive index, and concentrator field-of-view (FOV) are defined for each of the 𝑀 receivers. Additionally, conversion factors for both electrical-to-optical and optical-to-electrical processes are specified for all 𝑁 transmitters and 𝑀 receivers.

## Parameters

The `OWC_Channel_Model(Relative)` block is designed with the following configurable parameters to simulate the optical channel effectively:

| Parameter Name                   | Description                                                                                          | Default Value       | Data Type           | Example Input                            |
|----------------------------------|------------------------------------------------------------------------------------------------------|---------------------|---------------------|------------------------------------------|
| `num_inputs`                     | Number of Transmitter(s)                                                                             | 1                   | `Integer`           | `2`                                      |
| `num_outputs`                    | Number of Receiver(s)                                                                                | 1                   | `Integer`           | `3`                                      |
| `acceptance_angle_array`         | Array specifying the acceptance angles $\( \psi_{ij} \)$ of the receivers (in degrees)                 | `[1.0]`             | `Float array/vector` | For $\ \psi_{11} = 20.0, \psi_{12} = 25.0 \$: `[20.0, 25.0]` |
| `emission_angle_array`        | Array specifying the emission angles $\( \phi_{ij} \)$ from transmitters(i) to receivers(j) (in degrees) | [1.0]               | `Float array/vector`    | For $\ \phi_{11} = 20.0, \phi_{12} = 25.0 \$: `[20.0, 25.0]` |
| `distance_array`                 | Array specifying the distances $\ d_{ij}$ between transmitters(i) and receivers(j)                       | `[1.0]`             | `Float array/vector` | For $\ d_{11} = 2.0,  d_{12} = 2.5 \$: `[2.0, 2.5]` |
| `lambertian_order_array`         | Array specifying the Lambertian orders $\( m \)$                                                       | `[1.0]`             | `Float array/vector` |  For Tx₁ = 1.0 & Tx₂ = 2.0 : <br> `[1.0, 2.0]` |
| `photosensor_area_array`         | Array specifying the photosensor areas $\( A_T \)$ at the receivers                                    | `[1.0]`             | `Float array/vector` | For Rx₁ = 0.5, Rx₂ = 1.0: <br> `[0.5, 1.0]` |
| `optical_filter_transmittance_array` | Array specifying the optical filter transmittances $\( T_s \)$                                   | `[1.0]`             | `Float array/vector` | For Rx₁ = 1.0, Rx₂ = 1.5: <br> `[1.0, 1.5]` |
| `refractive_index_array`         | Array specifying the refractive index $\( n \)$ of the concentrator lens                               | `[1.0]`             | `Float array/vector` | For Rx₁ = 1.0, Rx₂ = 1.5: <br> `[1.0, 1.5]` |
| `concentrator_FOV_array`         | Array specifying the field-of-view (FOV) $\( \Psi_C \)$ of the concentrator lens                       | `[90]`              | `Float array/vector` | For $\ \Psi_{C1} = 60, \Psi_{C2} = 45 \$: `[60, 45]` |
| `E2O_conversion_factor_array`    | Array specifying the electrical-to-optical conversion factors $\( C_T \)$                              | `[1.0]`             | `Float array/vector` | For Tx₁ = 1.0 & Tx₂ = 2.0 : <br> `[1.0, 2.0]` |
| `O2E_conversion_factor_array`    | Array specifying the optical-to-electrical conversion factors $\( C_R \)$                              | `[1.0]`             | `Float array/vector` | For Rx₁ = 1.0, Rx₂ = 1.5: <br> `[1.0, 1.5]` |


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
