# OWC Channel Model(Relative)
Category: Channel Models

Block Name: OWC Channel Model(Relative)

## Overview
The `owc_channel_model` block in the `gr-owc` module simulates the optical channel's behavior in optical wireless communication (OWC) systems. This block models the relationship between the electrical signals from 𝑁 transmitters and the corresponding electrical signals received at 𝑀 receivers. It accounts for emission and acceptance angles, as well as distances between each of the 𝑁 𝑀 transmitter-receiver pairs. The Lambertian orders, which describe the directional emission characteristics of the 𝑁 transmitters, are parameterized, allowing for flexible modeling of various optical setups. On the receiver side, parameters such as the photosensor area, optical filter gain, refractive index, and concentrator field-of-view (FOV) are defined for each of the 𝑀 receivers. Additionally, conversion factors for both electrical-to-optical and optical-to-electrical processes are specified for all 𝑁 transmitters and 𝑀 receivers. If these conversion factors are set to 1, the block directly relates the transmitted optical power to the received optical power at the surface of the photosensor, providing a simplified power relationship model.

## Parameters

The `owc_channel_model` block is designed with the following configurable parameters to simulate the optical channel effectively:

| Parameter Name               | Description                                                                                     | Default Value       | Data Type        |
|------------------------------|-------------------------------------------------------------------------------------------------|---------------------|------------------|
| `num_inputs`                 | Number of Transmitter(s)                                                                         | 1                   | `Integer`            |
| `num_outputs`                | Number of Receiver(s)                                                                            | 1                   | `Integer`            |
| `emission_angle_array`        | Array specifying the emission angles $\( \phi_{ij} \)$ from transmitters to receivers (in degrees) | [1.0]               | `Float array/vector`    |
| `acceptance_angle_array`      | Array specifying the acceptance angles $\( \psi_{ij} \)$ of the receivers (in degrees)            | [1.0]               | `Float array/vector`    |
| `distance_array`              | Array specifying the distances $\( d_{ij} \)$ between transmitters and receivers                  | [1.0]               | `Float array/vector`    |
| `lambertian_order_array`      | Array specifying the Lambertian orders $\( m \)$                                                 | [1.0]               | `Float array/vector`    |
| `photosensor_area_array`      | Array specifying the photosensor areas $\( A_T \)$ at the receivers                               | [1.0]               | `Float array/vector`    |
| `optical_filter_transmittance_array` | Array specifying the optical filter transmittances $\( T_s \)$                                | [1.0]               | `Float array/vector`    |
| `refractive_index_array`      | Array specifying the refractive index $\( n \)$ of the concentrator lens                          | [1.0]               | `Float array/vector`    |
| `concentrator_FOV_array`      | Array specifying the field-of-view (FOV) $\( \Psi_C \)$ of the concentrator lens                  | [90]                | `Float array/vector`    |
| `E2O_conversion_factor_array` | Array specifying the electrical-to-optical conversion factors $\( C_T \)$                         | [1.0]               | `Float array/vector`    |
| `O2E_conversion_factor_array` | Array specifying the optical-to-electrical conversion factors $\( C_R \)$                         | [1.0]               | `Float array/vector`    |

## Description
### LOS Path and DC Gain
In optical wireless communication, the LOS path is usually the most significant component of the channel. The DC gain of the LOS path provides a good approximation for the overall channel gain, allowing the simplification of the model by ignoring multipath effects when a clear LOS is present.

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

### Frequency Characteristics
While the optical channel’s multipath components can be ignored for simplicity, the frequency characteristics of the optical conversion play a significant role in the transmitted signal. The optical channel can be modeled as a series of three systems: the transmitter, the optical channel, and the receiver. Each system impacts the signal’s frequency response, and these characteristics must be considered for accurate modeling.

## Summary
The `owc_channel_model` block in the `gr-owc` module provides a detailed simulation of the optical channel by focusing on the dominant LOS path and modeling its impact using DC channel gain and angle-dependent gain functions. This block helps in understanding and predicting the behavior of optical wireless communication systems in various scenarios.

## Examples:
..

# gr-owc
* [Overview](gr-owc_Overview.md)
* Blocks:
  
| Sl No.   | Block         | Description         |
|-----------------|-----------------|-----------------|
| 1 | OWC_Channel_Model(Relative) | Models the optical channel, considering DC channel gain from transmitter to receiver. |
| 2 | [OOK_Modulator](OOK_Modulator.md) | Implements On-Off Keying (OOK) baseband modulation scheme. |
