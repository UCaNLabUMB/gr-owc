# gr-owc
GNURadio out-ot-tree (OOT) module for optical wireless communications. 

* **Contact:** Dr. Michael Rahaim (<Michael.Rahaim@umb.edu>) from The Ubiquitous Communications and Networking Lab ([UCaN Lab](https://www.umb.edu/ucanlab)), University of Massachusetts, Boston.

<a href="https://zenodo.org/badge/latestdoi/323626297"><img src="https://zenodo.org/badge/323626297.svg" alt="DOI"></a>



# Installation
**NOTE:** gr-owc is currently only compatible with GNURadio 3.8 version.

This installation guide assumes that GNURadio has been installed using PyBOMBS. With a PyBOMBS installation, gr-owc can be installed using either of the following methods:
* **Install via PyBOMBS:** Since gr-owc is available in [CGRAN](https://www.cgran.org/), PyBOMBS can be used to directly add the gr-owc library to an existing GNURadio prefix.
* **Basic Installation:** Download this repository and use _make_ to install the gr-owc library in an existing GNURadio prefix.



## Install via PyBOMBS (SUGGESTED)
As part of the Comprehensive GNURadio Archive Network (CGRAN), gr-owc can be installed directly into the desired GNURadio prefix using PyBOMBS. For this, follow the steps below:

1. In a terminal, configure PyBOMBS for default configuration with `pybombs auto-config`
1. Point PyBOMBS to the recipes for installing OOT modules. You can use `pybombs recipes add-defaults` (adds gr-recipes and gr-etcetra) 
1. Move to the desired GNURadio prefix folder with `cd <prefix directory>` 
1. Install gr-owc using PyBOMBS with `pybombs install gr-owc`
1. Open `gnuradio-comapanion` and you should find a module for gr-owc
   * (Make sure you have sourced the prefix for the GNURadio Installation where gr-owc was added)



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



# Documentation
The documentation provided in the chapters below offers a step-by-step overview of gr-owc and how it can be used to deploy a multi-cell/multi-user OWC testbed.

| Chapter | Topic | Image | Summary 
| --- | --- | --- | --- |
| 1 | [Introduction](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/Chapters/Overview.md)           | ADD IMAGE | Introduction to gr-owc channel blocks and modulators/demodulators
| 2 | [Hardware Setup](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/Chapters/Hardware.md)         | ADD IMAGE | Overview of setup procedure for over-the-air OWC transmission with USRPs
| 3 | [Data Collection](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/Chapters/Data_Collection.md) | ADD IMAGE | Overview of examples for packet error rate analysis and automated data collection
| 4 | [Multi-User OWC](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/Chapters/MultiUser_OWC.md)    | ADD IMAGE | Setup process for multi-user configuration with DCO-OFDMA
| 5 | [Multi-Cell OWC](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/Chapters/MultiCell_OWC.md)    | ADD IMAGE | Hardware description and configuration for multiple transmitter setup in multi-cell/multi-user OWC networks


