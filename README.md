# gr-owc
GNURadio out-ot-tree (OOT) module for optical wireless communications. 

* **Contact:** Dr. Michael Rahaim (<Michael.Rahaim@umb.edu>) from The Ubiquitous Communications and Networking Lab ([UCaN Lab](https://www.umb.edu/ucanlab)), University of Massachusetts, Boston.

<a href="https://zenodo.org/badge/latestdoi/323626297"><img src="https://zenodo.org/badge/323626297.svg" alt="DOI"></a>

`gr-owc` is a GNU Radio Out-Of-Tree (OOT) module designed for Optical Wireless Communication (OWC). It provides a comprehensive suite of signal processing blocks designed to enable efficient experimentation, research, and development of optical wireless systems within the GNU Radio. The ‘gr-owc’ module covers OWC channel simulation, modulation and demodulation techniques, and other essential components. We describe how these blocks can also be implemented in physical systems using Software Defined Radio (SDR) hardware. 

**Note:** gr-owc is compatible with GNU Radio v3.10. For GNU Radio v3.8, refer to [gr-owc_v3.8](https://github.com/UCaNLabUMB/gr-owc/releases/tag/v1.1.0). 

# Directory Structure
* **Documentation:** Contains documentation of gr-owc blocks and chapters; offers a step-by-step overview of gr-owc.
* **examples:** Example GNURadio flowgraphs for demonstrating gr-owc usage.
* **grc:** .yml files of gr-owc blocks.
* **lib, include:** C++ and C++ w/ Volk implemeted gr-owc blocks
* **python:** Python implemented gr-owc blocks and QA test code.
* **Install_gr-owc.sh:** Script file to install gr-owc in GNURadio Companion.

# Installation

This installation guide assumes that GNURadio v3.10 has been installed. gr-owc can be installed using either of the following methods:
* **Install via Install_gr-owc.sh:** Automates installation of gr-owc in GNURadio.
* **Basic Installation:** Download this repository and use _make_ to install the gr-owc library in an existing GNURadio prefix.



## Install via Install_gr-owc.sh (SUGGESTED)
For this, follow the steps below:

1. Download **only** the [Install_gr-owc.sh](https://github.com/UCaNLabUMB/gr-owc/blob/main/Install_gr-owc.sh)
2. In the downloaed script directory, open terminal. Give executable permission for script file `chmod +x ./Install_gr-owc.sh`
3. Execute scrpit file `./Install_gr-owc.sh`
   * (There should be no failure displayed)
4. Open `gnuradio-comapanion` and you should find a module for gr-owc
   


## Basic Installation
Alternatively, to download the repository and install, follow the steps below:

1. Download this repository by cloning with git clone (url)
1. In a terminal, cd to the gr-owc directory
1. Create a build directory with `mkdir build` and move into the directory with `cd build`
1. Make sure to source the desired GNURadio prefix
1. Run `cmake ../` from the build directory
   * (the path to the sourced GNURadio installation would be found automatically)
1. Run `make`
1. Test the build with `make test` 
   * (there shouldn't be any failures)
1. Install with `make install`
1. Configure your linker/debugger with `sudo ldconfig`
1. Open gnuradio-companion and you should find a module for gr-owc



# gr-owc Blocks

The `gr-owc` module includes the following implemented blocks:

| Sl No. | Block Name                    | Description                                                                                               |
|--------|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1      | [OWC_Channel_Block(Relative)](https://github.com/UCaNLabUMB/gr-owc/blob/main/Documentation/Blocks/OWC_Channel_Model(Relative).md)    | Models the optical channel, considering DC channel gain from transmitter to receiver.                     |
| 2      | [OWC_Channel_Block(Absolute)]()    | Models the optical channel using absolute coordinates of the transmitter and receiver, considering DC channel gain from transmitter to receiver. |
| 3      | [OOK_Modulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/Documentation/Blocks/OOK_Modulator.md)                  | Implements On-Off Keying (OOK) baseband modulation scheme.                                                |
| 4      | [OOK_Demodulator](https://github.com/UCaNLabUMB/gr-owc/blob/main/Documentation/Blocks/OOK_Demodulator.md)                | Demodulates On-Off Keying (OOK) baseband signals and defines the binary outcome.                          |

---

# Chapters

| Chapter | Topic                | Summary                                                                                                               |
|---------|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1       | Background            | Overview of Software Defined Radio and an introduction to `gr-owc`, including its motivation and role in OWC.         |
| 2       | Channel Modeling      | Different channel modeling approaches for OWC, including their characteristics, types, and applications in various OWC scenarios. |
| 3       | SDR; OWC Hardware     | Detailed analysis of hardware components and their characteristics used for OWC, such as Transmitter, Receiver, USRP, and their suitability for OWC. |
| 4       | Modulator & Demodulator | Modulation and demodulation techniques supported by `gr-owc`, along with their applications and implementation considerations. |

---

# Principal Investigator

- **Name**: Dr. Michael B Rahaim  
- **Title/Position**: Associate Professor  
- **University**: University of Massachusetts Boston  
- **Email**: michael.rahaim@umb.edu  

---

# Developer

- **Name**: Kunal P Sangurmath  
- **University**: University of Massachusetts Boston  
- **Email**: sangurmathkunal@gmail.com / k.sangurmath001@umb.edu  

**Note**: This work is an extension of the original code developed by Arsalan Ahmed(<arsalanqasimahmed@gmail.com>) for GNURadio v3.8.
