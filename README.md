# gr-owc
GNURadio out-of-tree (OOT) module for optical wireless communications. 

* **Contact:** Dr. Michael Rahaim (<Michael.Rahaim@umb.edu>) from The Ubiquitous Communications and Networking Lab ([UCaN Lab](https://www.umb.edu/ucanlab)), University of Massachusetts, Boston.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20025685.svg)](https://doi.org/10.5281/zenodo.20025685)

`gr-owc` is a GNU Radio Out-Of-Tree (OOT) module designed for Optical Wireless Communication (OWC). It provides a comprehensive suite of signal processing blocks designed to enable efficient experimentation, research, and development of optical wireless systems within the GNU Radio. The ‘gr-owc’ module covers OWC channel simulation, modulation and demodulation techniques, and other essential components. We describe how these blocks can also be implemented in physical systems using Software Defined Radio (SDR) hardware. 



# Directory Structure
* **docs:** Contains markdown file documentation for individual gr-owc blocks and gr-owc tutorial chapters along with default doxygen documentation from GNURadio's module creation.
* **examples:** Example GNURadio flowgraphs for demonstrating gr-owc usage.
* **grc:** .yml files for the gr-owc blocks (to define block representation within GNURadio Companion).
* **lib, include:** C++ and C++ w/ Volk implemeted gr-owc blocks
* **python:** Python implemented gr-owc blocks and QA test code.
* **Install_gr-owc.sh:** Script file to install gr-owc in GNURadio Companion.

# Installation

**Note:** gr-owc is compatible with GNU Radio v3.10. For GNU Radio v3.8, refer to [gr-owc_v3.8](https://github.com/UCaNLabUMB/gr-owc/releases/tag/v1.1.0). 

If you're already familiar with GNURadio, you can jump directly to the [Installation Instructions](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Chapters/gr_owc_Install.md).


# gr-owc Blocks

The `gr-owc` module includes the following implemented blocks:

| Sl No. | Block Name | Description |
|--------|------------|-------------|
| 1 | [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/OWC_Channel_Model(Relative).md) | Models the optical channel using relative positioning between transmitter and receiver. |
| 2 | [OWC_Channel_Block(Absolute)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/OWC_Channel_Block(Absolute).md) | Models the optical channel using absolute coordinates. |
| 3 | [OOK_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/OOK_Modulator.md) | Implements On-Off Keying (OOK) modulation. |
| 4 | [OOK_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/OOK_Demodulator.md) | Recovers binary data from OOK signals. |
| 5 | [PAM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/PAM_Modulator.md) | Implements Pulse Amplitude Modulation (PAM). |
| 6 | [PAM_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/PAM_Demodulator.md) | Recovers symbols from PAM signals using amplitude detection. |
| 7 | [VPPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/VPPM_Modulator.md) | Implements Variable Pulse Position Modulation (VPPM). |
| 8 | [VPPM_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/VPPM_Demodulator.md) | Recovers binary symbols by detecting pulse position in VPPM signals. |
| 9 | [PPM_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/PPM_Modulator.md) | Implements Pulse Position Modulation (PPM). |
| 10 | [PPM_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/PPM_Demodulator.md) | Recovers symbols by detecting pulse position in PPM signals. |
| 11 | [LED_Nonlinearity](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/LED_Nonlinearity.md) | Models LED non-linear behavior in optical systems. |
| 12 | [Hermitian Symmetry (Same Vec Size I/O)](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Blocks/Hermitian_Symmetry_i_o_same_vec_size.md) | Ensures Hermitian symmetry in FFT vectors. |

---

# Chapters

| Chapter | Topic | Summary |
| --- | --- | --- |
| 1    | [Background](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Chapters/gr_owc_Overview.md)  | Overview of Software Defined Radio and an introduction to `gr-owc`, including its motivation and role in OWC.         |
| 2    | [Setup and Installation](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Chapters/gr_owc_Install.md)     | Installation instructions for GNURadio and gr-owc.         |
| 3    | Channel Modeling      | Different channel modeling approaches for OWC, including their characteristics, types, and applications in various OWC scenarios. |
| 4    | SDR; OWC Hardware     | Detailed analysis of hardware components and their characteristics used for OWC, such as Transmitter, Receiver, USRP, and their suitability for OWC. |
| 5    | Modulator & Demodulator | Modulation and demodulation techniques supported by `gr-owc`, along with their applications and implementation considerations. |

---

# Principal Investigator

- **Name**: Dr. Michael B Rahaim  
- **Title/Position**: Associate Professor  
- **University**: University of Massachusetts Boston  
- **Email**: michael.rahaim@umb.edu  

---

# Developers

- **Name**: Kunal P Sangurmath  
- **Contributions**: Updates for GNURadio V3.10. Performance characterization and block improvements. 

- **Name**: Arsalan Ahmed  
- **Contributions**: Initial development for GNURadio V3.8. 