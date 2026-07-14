# Electrical to Optical Connection 
## Voltage vs. Flux 
The goal of this section is to identify the ideal operating voltage range of the LED panel by driving it with a DC power supply and measuring the resulting illuminance (lux) using a light meter. This experiment characterizes the linear operating voltage range of the LED panel. Operating within this range ensures that the optical wireless communication (OWC) system behaves as a linear time-invariant (LTI) system during later experiments. 

**Components** 
- Keysight U8002A Single Output DC Power Supply (0–30 V, 5 A)
- ExTech Instruments Datalogging Light Meter with Cosine Corrector
- Small LED panel (e.g., square, rectangular, etc.)
- Male (M) BNC dual binding posts, male-to-male (M-M) BNC cable, male-to-female (M-F) BNC adapter, female (F) jumper wires, and female (F) BNC cable
-  Other accessories (e.g., Thorlabs screws and hardware kit) 

**Setup** 

![Figure 1: Physical setup](https://github.com/UCaNLabUMB/grc-owc/docs/hardware_characterization/Images/voltage_vs_flux.png) 

- Find a non-reflective surface (e.g., a black surface). Use the Thorlabs mounting hardware to secure the LED panel so that it faces the cosine corrector connected to the light meter. Position the LED panel and the cosine corrector approximately **0.5 m apart**. 
- Connect the LED panel as follows: *Male jumper wire* &rarr; *Female jumper wires and female BNC cable* &rarr; *Male-to-female BNC adapter*&rarr; *Male-to-male BNC cable* &rarr; *Male BNC dual binding posts* 

- Turn on the DC power supply. Press **Output On/Off**, then select **Voltage/Current**. Adjust the voltage using the control knob according to the desired voltage range (e.g., 7.0–10.5 V with 0.05 V increments). 

- Record both the applied voltage and the corresponding illuminance (lux) measured by the light meter. 
