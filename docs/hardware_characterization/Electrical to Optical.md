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

![](/docs/hardware_characterization/Images/voltage_vs_lux.png) 

- Find a non-reflective surface (e.g., a black surface). Use the Thorlabs mounting hardware to secure the LED panel so that it faces the cosine corrector connected to the light meter. Position the LED panel and the cosine corrector approximately **0.5 m apart**. 
- Connect the LED panel as follows: *Male jumper wire* &rarr; *Female jumper wires and female BNC cable* &rarr; *Male-to-female BNC adapter*&rarr; *Male-to-male BNC cable* &rarr; *Male BNC dual binding posts* 

- Turn on the DC power supply. Press **Output On/Off**, then select **Voltage/Current**. Adjust the voltage using the control knob according to the desired voltage range (e.g., 7.0–10.5 V with 0.05 V increments). 

- Record both the applied voltage and the corresponding illuminance (lux) measured by the light meter. 

**Results**

 ## Voltage vs. Power 
The goal of this section is to characterize the optical power response within the linear voltage range identified for the selected LED panel in the previous section. This experiment illustrates the relationship between the applied voltage and the received optical power for different LED panels. 

From Fig. [...], determine an appropriate DC offset voltage (e.g., **8.5 V**) and select a suitable peak-to-peak voltage amplitude (e.g., **1 Vpp**) for Channel 1 of the function generator. This ensures that the LED operates entirely within its linear operating region. For example, using an 8.5 V DC offset and a 1 V peak-to-peak signal results in a maximum voltage of **9.5 V**, which remains within the LED's linear operating range. In general, use Fig. [...] to determine the maximum and minimum voltages of the LED's linear operating region. These values can then be used to calculate the peak-to-peak voltage and DC offset using the following equations: 

$$ V_{amplitude} = \frac{V_{max} - V_{min}}{2} $$ 

$$ V_{offset} = V_{max} - V_{amplitude} $$

To compare the transmitted and received signals, observe both the original electrical input signal and the signal detected by the photodetector. Instead of using the light meter, use the **Thorlabs ADP2004A photodetector** to convert the received optical signal back into an analog electrical signal. The oscilloscope is then used to display both signals simultaneously in XY mode, where **V1** represents the transmitted input signal and **V2** represents the received signal measured by the photodetector.

**Components** 
. 



