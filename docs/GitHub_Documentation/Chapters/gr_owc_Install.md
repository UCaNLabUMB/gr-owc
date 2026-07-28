# gr-owc Installation

## Overview
This chapter introduces the installation process for GNURadio and how to include the gr-owc module in GNURadio.

**Tutorial Video:** _Coming Soon_


### Objective
_Coming Soon_


## Installing GNURadio and GNURadio Companion (GRC)
_Coming Soon_

This installation guide assumes that GNURadio v3.10 has been installed. gr-owc can be installed using either of the following methods:
* **Install via Install_gr-owc.sh:** Automates installation of gr-owc in GNURadio.
* **Basic Installation:** Download this repository and use _make_ to install the gr-owc library in an existing GNURadio prefix.



### Install via Install_gr-owc.sh (SUGGESTED)
For this, follow the steps below:

1. Download **only** the [Install_gr-owc.sh](https://github.com/UCaNLabUMB/gr-owc/blob/main/Install_gr-owc.sh)
2. In the downloaded script directory, open terminal. Give executable permission for script file `chmod +x ./Install_gr-owc.sh`
3. Execute scrpit file `./Install_gr-owc.sh`
   * (There should be no failure displayed)
4. Open `gnuradio-comapanion` and you should find a module for gr-owc
   


### Basic Installation
Alternatively, to download the repository and install, follow the steps below:

1. Download this repository by cloning with git clone (url)
2. In a terminal, cd to the gr-owc directory
3. Create a build directory with `mkdir build` and move into the directory with `cd build`
4. Make sure to source the desired GNURadio prefix
5. Run `cmake ../` from the build directory
   * (the path to the sourced GNURadio installation would be found automatically)
6. Run `make`
7. Test the build with `make test` 
   * (there shouldn't be any failures)
8. Install with `make install`
9. Configure your linker/debugger with `sudo ldconfig`
10. Open gnuradio-companion and you should find a module for gr-owc

The gr-owc blocks will be available under the `owc` drop down in the block library:
![gr-owc in GRC](https://github.com/UCaNLabUMB/gr-owc/blob/main/docs/GitHub_Documentation/Images/gr-owc_in_GRC.png)


## Installing the gr-owc Module
_Coming Soon_


# References
* GNURadio: [https://www.gnuradio.org/about/](https://www.gnuradio.org/about/)


# Tutorial Chapters

* **Next Chapter:** 

| Chapter | Topic | Summary |
| --- | --- | --- |
| 1    | Background            | Overview of Software Defined Radio and an introduction to `gr-owc`, including its motivation and role in OWC.         |