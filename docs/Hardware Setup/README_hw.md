Giovani DeOliveira

Step-by-Step Process for Configuring Raspberry Pi for Analog Discovery Board Use

**Installing Digilent Software**

- Download
  - **Adept Runtime (2.27.9 ARM64 .deb)** → <https://digilent.com/reference/software/adept/start>
  - **Adept Utilities (2.7.1 ARM64 .deb)** → <https://lp.digilent.com/complete-adept-utilities-download>
  - **WaveForms (3.24.4 ARM64 .deb)** → <https://digilent.com/reference/software/waveforms/waveforms-3/previous-versions?srsltid=AfmBOooLU7bZRdIQApq7KIjDNZDf6-tPbD6dRBq1T1Vs-mU8NSj8TxfE>
- Change to that folder and install:
  - cd ~/folder → sudo dpkg -i \*.deb
    - if dependencies are missing: sudo apt -f install -y
- Verify the ADB is detected by the Pi:
  - djtgcfg enum
- Sanity check: launch WaveForms, confirm the AD2 connects and works as expected
  - Run ADB Tx
    - Tx: Waveforms →AD Board (Pin W1) → Rx: Oscilloscope
  - Run ADB Rx
    - Tx: Function Generator → AD Board (Pins: 1+ and 1-) → Rx: Waveforms
- Run: ldconfig -p | grep libdwf
  - Expected: a line containing libdwf.so with a path (for example, /usr/lib/.../libdwf.so).
  - Note: The ADB GNU Radio blocks and the Python dwf wrapper talk to the board through this library.

**Installing gr-ad2 module in GNURadio**

- Install prerequisites:
  - sudo apt install git cmake libboost-all-dev gnuradio=3.10.\* doxygen python-pip
  - Version number depends on version of GNURadio being used on the Pi.
- Run this code:
  - cd
  - git clone <https://github.com/7m4mon/gr-ad2>
  - cd gr-ad2/GNURadio_v38
    - Note: <https://github.com/7m4mon/gr-ad2/tree/master>
- **Build and install v3.8 modules at once**
  - mkdir build
  - cd build
  - cmake ../
    - sudo apt install cmake (if package not found)
  - make
  - sudo make install
  - When all needed modules are installed:
    - sudo ldconfig
- Install PyPI - dwf Python package
  - python3 -m pip install --break-system-packages dwf
    - python3 -c "import dwf; print('dwf OK')"
  - Python wrapper for communicating with the AD Board.
- **Verify the blocks in GNU Radio Companion (GRC)**
  - Launch GRC.
  - In the block tree, confirm an **AnalogDiscovery2** group is present.
  - If blocks are missing:
    - close GRC → sudo ldconfig → relaunch GRC.
    - Debug if needed or repeat the process.

\*IF YOU RUN INTO ISSUES WITH dwf not running error in the flowgraph\*

- Create a new terminal and Run:
  - sudo dpkg --configure -a
  - If it reports a package failing, purge it:
    - sudo apt purge -y package
    - sudo apt -f install
  - Clean and Update:
    - sudo apt clean → sudo apt update
  - Install pip:
    - sudo apt install -y python3-pip
  - Update pip:
    - python3 -m pip install --upgrade pip
