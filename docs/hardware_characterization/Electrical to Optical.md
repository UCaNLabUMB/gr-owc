# Electrical to Optical Connection 
## Voltage vs. Flux 
The goal of this section is to identify the ideal operating voltage range of the LED panel by driving it with a DC power supply and measuring the resulting illuminance (lux) using a light meter. This experiment characterizes the linear operating voltage range of the LED panel. Operating within this range ensures that the optical wireless communication (OWC) system behaves as a linear time-invariant (LTI) system during later experiments. 

**Components** 
- Keysight U8002A Single Output DC Power Supply (0–30 V, 5 A)
- ExTech Instruments Datalogging Light Meter with Cosine Corrector
- Small LED panel (e.g., cirlce, rectangular, etc.)
- Male (M) BNC dual binding posts, male-to-male (M-M) BNC cable, male-to-female (M-F) BNC adapter, female (F) jumper wires, and female (F) BNC cable
-  Other accessories (e.g., Thorlabs screws and hardware kit) 

**Setup** 

![Figure 1: Physical setup](/docs/hardware_characterization/Images/section1_setup.png) 

- Find a non-reflective surface (e.g., a black surface). Use the Thorlabs mounting hardware to secure the LED panel so that it faces the cosine corrector connected to the light meter. Position the LED panel and the cosine corrector approximately **0.5 m apart**. 

Tx side: 
- Connect the LED panel as follows: *Male jumper wire* &rarr; *Female jumper wires and female BNC cable* &rarr; *Male-to-female BNC adapter* &rarr; *Male-to-male BNC cable* &rarr; *Male BNC dual binding posts* &rarr; DC power supply.

- Turn on the DC power supply. Press **Output On/Off**, then select **Voltage/Current**. Adjust the voltage using the control knob according to the desired voltage range (e.g., 7.0–10.5 V with 0.05 V increments). 

Rx side: 
- Turn on the light meter, record both the applied voltage and the corresponding illuminance (lux) measured by the light meter. 

**Results**

![Figure 2: Voltage vs Lux](/docs/hardware_characterization/Images/voltage_vs_lux.png)

In this instance, we tested 2 LEDs (i.e., rectangle, circle), we can see that the turn voltage vs lux power associated with each LEDs is different, they both exibit specific turn on voltages, for rectangle LED it at ~7.8V, on the other hand the square LED need higher voltage ~9.5V to turn on, what we want to focus on is the liner characteristic voltage range of the 2 LEDs, which we can see based on the plot we obtain. 

## Voltage vs. Power 
The goal of this section is to characterize the optical power response within the linear voltage range identified for the selected LED panel in the previous section. This experiment illustrates the relationship between the applied voltage and the received optical power for different LED panels. 

From the figure above, determine an appropriate DC offset voltage (e.g., **8.5 V**) and select a suitable peak-to-peak voltage amplitude (e.g., **1 Vpp**) for Channel 1 of the function generator. This ensures that the LED operates entirely within its linear operating region. For example, using an 8.5 V DC offset and a 1 V peak-to-peak signal results in a maximum voltage of **9.5 V**, which remains within the LED's linear operating range. In general, use voltage vs lux figure to determine the maximum and minimum voltages of the LED's linear operating region. These values can then be used to calculate the voltage amplitude and DC offset using the following equations: 

$$ V_{amplitude} = V_{p} = \frac{V_{max} - V_{min}}{2} $$ 

$$ V_{pp} = 2V_{p} $$ 

$$ V_{offset} = V_{max} - V_{amplitude} $$

To compare the transmitted and received signals, observe both the original electrical input signal and the signal detected by the photo-detector. Instead of using the light meter, use the **Thorlabs ADP120A2 photodetector** to convert the received optical signal back into an analog electrical signal. The oscilloscope is then used to display both signals simultaneously in XY mode, where **V1** represents the transmitted input signal and **V2** represents the received signal measured by the photo detector.

**Components** 
- Tektronix MDO3014 Mixed Domain Oscilloscope
- Keysight 33500B Series Waveform Generator 
- Thorlabs ADP120A2 Photo-detector, optical lens & blue filter
- Small LED panel (e.g., cirlce, rectangular, etc.)
- Male (M) BNC dual binding posts, **2 male-to-male (M-M) BNC cable**, male-to-female (M-F) BNC adapter, female (F) jumper wires, and female (F) BNC cable
- Other accessories (e.g., Thorlabs screws and hardware kit) 

**Setup** 

The setup is similar to what we had for Voltage vs Lux (i.e., same distance for LED and photo-detector with the same reflective surface). But instead of using a DC power supply and light meter, we used a function generator for signal generation and a Thorlabs photo-detector with an oscilloscope to observe the transmitted optical signal from the LED. 

The voltage amplitude, and offset for our signal, already had been discussed above, but to reiterate we want to shift our DC offset in the operating region of our LED of interest, and include the V_{amplitude} (i.e., V_{pp}), to ensure that the LED is linear characterize based on the V_{maximum} and V_{minimum} that we choose. The equations above sum up the idea, and the figure below provides another example demonstration of an instance for the rectangular LED panel. 

![Figure 2: Physical setup](/docs/hardware_characterization/Images/section2_setup.png) 
 (Note: the BNC cable and physical space setup is the same as in the Voltage vs. Lux section; thus, we will not mention the wire setup)

Tx side: 
- Use the BNC cable to connect the Function Generator (FG) input Ch1 &rarr; LED male jumping wires. 
- Use the BNC cabe connect FG input ch2 &rarr; oscilloscope input ch1 (input signal). 
- Turn on FG, press 1 (for channel 1) &rarr; Output Load &rarr; Set To High Z &rarr; More &rarr; Dual Channel &rarr; Tracking &rarr; Identical &rarr; Done. 
- Press on Parameter &rarr; change frequency (e.g., 10kHz), amplitude (e.g., 1 V_{pp}), offset (e.g., 8.5 V)
- Press on Waveforms &rarr; sine, ramp, etc. (i.e., in the results, we used ramp because it provides a sharper cutoff, which is more ideal to demonstrate the linearity of the LED). 
- Press 1 & 2 &rarr; Output On. 

Rx side: 
- Turn on the photo-detector, with lens and filter included, use a BNC cable to connect photo-detector output &rarr; oscilloscope input ch2 (output signal received). 
- Turn on the oscilloscope, press 1 &rarr; Coupling DC & Termination 1M&#937, press 2 &rarr; Coupling AC & Termination 1M$#937. 
- To ensure the 2 signals are center in oscilloscope, adjust the Scale &rarr; press 1 & 2 and adjust their Position Push to Center &rarr; Menu (in trigger setting) &rarr; Source select 1 or 2 &rarr; Force Trig &rarr; adjust the Level knob (i.e., if Source 1, the horizontal level at the middle of ch1 signal, if Source 2, the horizontal level at the -V_{p}). 
- Press Acquire &rarr; XY Display &rarr; Triggered XY (i.e., X = ch1 voltage, Y = ch2 voltage); this should display a linear line if we are in the right voltage range. 
- Press Menu (in Save/Recall setting) &rarr; Assign Save to All &rarr; Image, Waveform, and Setup &rarr; Menu Off.
- Press Save (in Save/Recall setting). 

**Results** 

![Figure 3: XY Display](/docs/hardware_characterization/Images/XY_Display.png)

For this result, we primarily focus on the rectangular LED panel collection, examining the relationship on an XY display (where X = channel 1 voltage and Y = channel 2 voltage). In our case, channel 1 on the oscilloscope represents the input signal (a ramp signal), while channel 2 displays the same signal received by the photo-detector, which captures optical power from the LED using the same input signal as in channel 1.

The results reveal two scenarios for the channel 2 signal: clipping and non-clipping. When we adjust the input signal voltage amplitude to approximately 8V, we observe clipping because the LED's turn-on voltage is not ideal at that level. Conversely, a voltage of about 8.8V is more suitable, as the LED accepts anything above 8V as its turn-on voltage (Results in Voltage vs Lux section).

Additionally, the XY plot demonstrates both linear and non-linear responses for the corresponding input signal voltage amplitudes as we vary them (see the figure above). This correlates with the data we have collected and observed concerning the linear characteristics of the LED in the voltage versus lux section.
