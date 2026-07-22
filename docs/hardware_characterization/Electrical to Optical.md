# Electrical to Optical  
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

# Optical to Electrical 
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

The voltage amplitude, and offset for our signal, already had been discussed above, but to reiterate we want to shift our DC offset in the operating region of our LED of interest, and include the $V_{amplitude}$ (i.e., $V_{pp}$), to ensure that the LED is linear characterize based on the $V_{maximum}$ and $V_{minimum}$ that we choose. The equations above sum up the idea, and the figure below provides another example demonstration of an instance for the rectangular LED panel. 

![Figure 2: Physical setup](/docs/hardware_characterization/Images/section2_setup.png) 
 (Note: the BNC cable and physical space setup is the same as in the Voltage vs. Lux section; thus, we will not mention the wire setup)

Tx side: 
- Use the BNC cable to connect the Function Generator (FG) input Ch1 &rarr; LED male jumping wires. 
- Use the BNC cabe connect FG input ch2 &rarr; oscilloscope input ch1 (input signal). 
- Turn on FG, press 1 (for channel 1) &rarr; Output Load &rarr; Set To High Z &rarr; More &rarr; Dual Channel &rarr; Tracking &rarr; Identical &rarr; Done. 
- Press on Parameter &rarr; change frequency (e.g., 10kHz), amplitude (e.g., 1 $V_{pp}$), offset (e.g., 8.5 V)
- Press on Waveforms &rarr; sine, ramp, etc. (i.e., in the results, we used ramp because it provides a sharper cutoff, which is more ideal to demonstrate the linearity of the LED). 
- Press 1 & 2 &rarr; Output On. 

Rx side: 
- Turn on the photo-detector, with lens and filter included, use a BNC cable to connect photo-detector output &rarr; oscilloscope input ch2 (output signal received). 
- Turn on the oscilloscope, press 1 &rarr; Coupling DC & Termination 1M&#937, press 2 &rarr; Coupling AC & Termination 1M$#937. 
- To ensure the 2 signals are center in oscilloscope, adjust the Scale &rarr; press 1 & 2 and adjust their Position Push to Center &rarr; Menu (in trigger setting) &rarr; Source select 1 or 2 &rarr; Force Trig &rarr; adjust the Level knob (i.e., if Source 1, the horizontal level at the middle of ch1 signal, if Source 2, the horizontal level at the $-V_{p}$). 
- Press Acquire &rarr; XY Display &rarr; Triggered XY (i.e., X = ch1 voltage, Y = ch2 voltage); this should display a linear line if we are in the right voltage range. 
- Press Menu (in Save/Recall setting) &rarr; Assign Save to All &rarr; Image, Waveform, and Setup &rarr; Menu Off.
- Press Save (in Save/Recall setting). 

**Results** 

![Figure 3: XY Display](/docs/hardware_characterization/Images/XY_Display.png)

For this result, we primarily focus on the rectangular LED panel collection, examining the relationship on an XY display (where X = ch1 voltage and Y = ch2 voltage). In our case, ch1 on the oscilloscope represents the input signal (a ramp signal), while ch2 displays the same signal received by the photo-detector, which captures optical power from the LED using the same input signal as in ch1.

The results reveal two scenarios for the ch2 signal: clipping and non-clipping. When we adjust the input signal voltage amplitude to approximately 8V, we observe clipping because the LED's turn-on voltage is not ideal at that level. Conversely, a voltage of about 8.8V is more suitable, as the LED accepts anything above 8V as its turn-on voltage (Results in Voltage vs Lux section).

Additionally, the XY plot demonstrates both linear and non-linear responses for the corresponding input signal voltage amplitudes as we vary them (see the figure above). This correlates with the data we have collected and observed concerning the linear characteristics of the LED in the voltage versus lux section.

## Linearty Check [OPTIONAL]
The goal for this section is to ensure that there is no harmonicity within the linear voltage range that we have, since harmonics in the frequency domain mean our signals are clipped in the time domain (i.e., since clipped signals look like square waves, and square waves in frequency introduce harmonic spikes), this is bad because it could lead to signal **distortion** and **interference**. For this section, we want to send a sine wave rather than a ramp wave because a sine wave is a deterministic signal ideal for a real-life scenario. The experiment in this section will use the same setup with small changes to the BNC cable from the previous section, and use the math function of the Fast-Fourier-Transform (FFT) in the oscilloscope to convert our time-varying sine wave into the frequency domain.

**Components**
- [Same as Voltage vs Power] 
- Mini-Circuits 15542 SLP-5+ Low Pass Filter (LPF) & Mini-Circuits DC Block 50&Omega BLK-89-S+
- Other accessories (e.g., Thorlabs screws and hardware kit) 

**Setup** 

The setup is the same as in the Voltage vs Power section, with the addition of an LPF and a DC Block for the ch2 input port of the oscilloscope. In this section, we do not dive into detail about the LPF and DC Block; the Frequency Response section will explain it in detail. To check whether the voltage range is consistent and does not introduce any harmonics in the frequency domain, we are sending a sine wave and using Fast-Fourier-Transform (FFT) mode in the math function to observe the input sine wave's frequency domain under the same setup.

![Figure 4: Physical setup](/docs/hardware_characterization/Images/section3_setup.png)

Tx side: 
- [Same as Voltage vs Power] 
- Press on Waveforms &rarr; sine 
- Press 1 & 2 &rarr; Output On. 

Rx side: 
- Turn on the photo-detector, with lens and filter included, use a BNC cable to connect photo-detector output &rarr; LPF & DC Block &rarr; oscilloscope input ch2. 
- To ensure the 2 signals are center in oscilloscope, adjust the Scale &rarr; press 1 & 2 and adjust small knob (in Position Push to Center) &rarr; Menu (in trigger setting) &rarr; Source select 1 or 2 &rarr; Force Trig &rarr; adjust the Level knob (i.e., if Source 1, the horizontal level at the middle of ch1 signal, if Source 2, the horizontal level at the $-V_{p}$). 
- Turn on the oscilloscope, press 1 &rarr; Coupling DC & Termination 1M&Omega, press 2 &rarr; Coupling AC & Termination 1M&Omega. 
- Press Math &rarr; FFT &rarr; FFT Source &rarr; Adjust Multipurpose a knob &rarr; Change it to ch2. 

**Results** 

![Figure 5: FFT Display](/docs/hardware_characterization/Images/FFT_Display.png)

The figure results feature two scenarios for different voltage amplitudes, $1V_{pp}$ and  $3V_{pp}$, with a fixed DC offset of 8.5V and a frequency of 10kHz for the rectangular LED. Using the FFT mode in the oscilloscope, we can see that at $1V_{pp}$, in ch2 the photo-detector can receive a signal without clipping; this can also be viewed in the frequency domain with FFT, where there are barely any visible signs of harmonic peaks around our tone frequency 10kHz that we send for the sine wave. On the other hand, as we increase the amplitude to $3V_{pp}$, the signal clipping (for more details of clipping visit Voltage vs Power section), and as the signal clip the bottom half of it look like a square waves, square wave in frequency domain have harmonic spikes around the tone frequency, thus we can see the output clearly display that harmonicity around our frequency of interest (i.e., 10kHz). This behavior comes back to the idea that our voltage range is out of range for linear characterization (Voltage vs Power); thus, we want to choose a correct voltage range when working through this, ensuring the system is Linear Time Invariant (LTI). 
 
## Frequency Response 
The goal for this section is to characterize the frequency response of our hardware component. In other words, we want to characterize what the sine-sweep signal's frequency response looks like when we use the low-pass filter (LPF) and DC Block to capture the output from the photo-detector. This gives us insight into the frequency characteristics. The setup for this section will be the same as in the previous section; one notable difference is that we will use the Radio Frequency (RF) channel on the oscilloscope to measure the frequency response. 

But to intuitively understand the later observation from this section, we can trace back to signal and system concepts. Let's say our FG input sine-sweep as x(t), and the output signal received from photo-detector to be y(t), and in the process x(t) went through 3 different filters: $h_1(t)$, $h_2(t)$, $h_3(t)$, to obtain y(t) where: 

$h_1(t)$: associated with the photo-detector optical lens and blue filter. 

$h_2(t)$: associated with the DC-Block. 

$h_3(t)$: associated with the LPF filter. 

If we **convolve** them in the time domain, that means when we look at the frequency response, they're **multiplied** by each other in the frequency domain. 

$$ y(t) = x(t) * h_1(t) * h_2(t) * h_3(t) $$ 
$$  Y(f) = X(f) H_1(f) H_2(f) H_3(f) $$ 

![Figure 6: signal process](/docs/hardware_characterization/Images/signal_process.png)

Because we are sending the same $8.5V DC_{offset}$ and $1V_{pp}$ or $0.5V_{p}$ (i.e., Voltage and Power) for the sine sweep, our input signal is: 

$$ x(t) = 8.5 + 0.5sin(2$\pi$ft) $$ 

The optical lens and blue filter will not be mentioned, since they are physical filter components that help capture the optical wavelength more easily for power efficiency.

On the other hand, the DC Block, as the name suggests, blocks the DC signal; we want it purely AC because we don't want the DC to introduce **distortion** and **interference**. We can think of it as a charging capacitor (i.e., the DC Block has a capacitor component) — when fully charged, the voltage across the capacitor reaches steady state and equals the input voltage (8.5V DC offset), so the two cancel out, blocking the DC offset. 

Another way to think of it is as an RL high-pass filter, since the transfer function of an RL high-pass filter is typically: 

$$ |H(f)| = \left|\frac{V_o}{V_i}\right| = \frac{1}{\sqrt{1 + \left(\dfrac{R}{2\pi f L}\right)^2}} $$

Our DC offset component has a frequency of 0 Hz, which results in zero gain in the transfer function.

In addition, since higher frequencies appear only as white noise, we filtered the signal using an LPF with a cutoff frequency of ~5 MHz. Thus, the observed output signal is:

$$ y(t) = 0.5\sin(2\pi f t) $$

The images above sum up the frequency response as well as the signal-in-time characteristics that we mentioned. 


**Components** 
- [Same as Linearity Check] 

**Setup**

The setup is based on the previous Linearity Check section. But now, we disabled ch1 and ch2 and used the RF channel, which helps us determine the frequency response of the output signal. To get the frequency response, we will use the **Max Hold** function in the oscilloscope, which continuously captures and retains the maximum amplitude (power) reached at each frequency over multiple sweeps.

![Figure 7: Physical setup](/docs/hardware_characterization/Images/section4_setup.png)

Tx side: 
- [Same as Voltage vs Power]
- Press on Waveforms &rarr; sine. 
- Press on Sweep &rarr; Start Freq (e.g., 100 Hz) &rarr; Stop Freq (e.g., 10 MHz) &rarr; Sweep Time (e.g., 10s) &rarr; Output On. 
- Press on 1 &rarr; Output On. 

Rx side: 
- Turn on the photo-detector, with lens and filter included; use a BNC cable to connect the photo-detector output &rarr; oscilloscope input RF. 
- Press on RF &rarr; Spectrum Traces &rarr; Normal On &rarr; Average16 Off &rarr; Max Hold On &rarr; Min Hold Off. 
- Press on Freq/Span &rarr; adjust Center Frequency (e.g., 6.5 MHz) &rarr; adjust Span (e.g., 13 MHz) (i.e., the start should be at 0 Hz and the stop should be close to FG Stop Freq). 
- Press Save.

**Results** 

![Figure 8: Frequency Response](/docs/hardware_characterization/Images/Frequency_response.png)

From the figure, the result correlates with our analysis above: the low-pass filter is doing its job, with the response starting to roll off around $f_c \approx 6\text{ MHz}$. The frequency response was swept from 0 Hz to 13 MHz (CF 6.5 MHz, span 13.0 MHz, RBW 100 kHz). Beyond ~7 MHz, the trace drops into the noise floor, confirming the filter attenuates frequencies past the cutoff.

We can also argue that the oscilloscope and environmental factors reduced our voltage when we look at power in dBm. In the plot, marker R reads −20.0 dBm at 2.76 MHz, and a second marker reads −49.6 dBm at 5.51 MHz — well past the point where attenuation begins.
