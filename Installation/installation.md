### Introduction
In this document you'll find a complete tutorial for installing gr-owc on your machine. The current version only works with GNURadio 3.8, and you probably have a higher version (3.10 for example), so don't worry, this tutorial covers that situation.

### Installing gr-owc
Currently, with the current version of the module, gr-owc is only compatible with GNU Radio version 3.8, so I'll explain in the rest of this tutorial how to uninstall the current version (if it's more or less recent) and reinstall version 3.8, and how to properly install gr-owc on your computer. 

For Windows users, don't worry, I'll be running the tutorial on WSL2.

#### 1. Uninstalling the current version of GNU Radio (optional)
As mentioned above, gr-owc currently only works with GNU Radio version 3.8, so if you have another version you'll generally need to uninstall it cleanly to make sure you don't cause any compatibility errors.

Type this in your terminal to uninstall gnuradio
   ```
   sudo apt remove gnuradio
   ```
 You may need to enter your password to perform this action. Then type this
 ```
   sudo add-apt-repository --list
```
To list all the personal archives (PPA) you have on your machine. Delete all PPAs containing the name 'gnuradio' by running this line of code in your terminal
```
	sudo add-apt-repository --remove <ppa name>
```
It should be OK now that you've removed everything properly, but if not I suggest you take a look at this [link](https://wiki.gnuradio.org/index.php?title=UnInstallGR) for more information and details.

#### 2. Installing GNU Radio 3.8 on Linux
This tutorial is based on Ubuntu 22.04, and will run on a machine running natively on Linux or on WSL2 with this Linux distribution. 

In your terminal, type the following bash commands to root your system and clone the GNURadio GitHub repository.
```
	cd $HOME
	git clone https://github.com/gnuradio/gnuradio.git
	cd gnuradio
```
Once this is done, go to the branch of the version you want, in our case it will be version 3.8 and so we go to the `maint-3.8` branch, perform all the updates and create a **build** folder and go inside it, all this with the following commands in your terminal
```
	git checkout maint-3.8
	git submodule update --init --recursive
	mkdir build
	cd build
```
In the next step, if you want to install GNU Radio in a different prefix, add the following option `-DCMAKE_INSTALL_PREFIX=XXX` to install GNU Radio in the `XXX` prefix. If this is not specified, the default prefix is `/usr/local`; this will build the project for installation using the **CMake** tool.
```
	cmake -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 ../
```
Next, you'll use the **make** tool to compile your code using the following command
```
	make -j3
```
`-j3` indicates that you want to use 3 CPU cores, if you want to use all cores write `-j$(nproc)`. 

Now proceed with the tests. It's highly likely that not all tests will be valid, but this isn't a problem, as some of the dependencies don't come into play when GNURadio is installed. To run the tests, type the following command: 
```
	make test
```
To install the module, type the following command and enter your password. 
```
	sudo make install
```
Installation may take several minutes. After installation, type the following command 
```
	sudo ldconfig
```
To retrieve the Python libraries, you need to set the PYTHONPATH and LD_LIBRARY_PATH system variables. If you don't remember the prefix you used when installing GNURadio, type the following command to get it
```
	gnuradio-config-info --prefix
```
In the following commands, replace `{your-prefix}` with the prefix you have. 
- Find Python libraries
```
	find {your-prefix} -name gnuradio | grep "packages"
```
You'll see, among other things, the Python version you have (python3 or python2).
- Configure PYTHONPATH
```
	export PYTHONPATH={your-prefix}/lib/{Py-version}/dist-packages:{your-prefix}/lib/{Py-version}/site-packages:$PYTHONPATH
```
- Configure LD_LIBRARY_PATH
```
	export LD_LIBRARY_PATH={your-prefix}/lib:$LD_LIBRARY_PATH
```
- Save the commands in a Bash start-up file so that they run every time
Open one of these files `~/.bash_aliases` or `~/.bashrc` or `~/.profile` in your text editor, e.g. nano or vim as follows (using nano): 
```
	nano ~/.profile
```
And at the end, add the two previous commands like this: 
```
	export PYTHONPATH={your-prefix}/lib/{Py-version}/dist-packages:{your-prefix}/lib/{Py-version}/site-packages:$PYTHONPATH
	export LD_LIBRARY_PATH={your-prefix}/lib:$LD_LIBRARY_PATH
```
Of course, replace with your prefix and the version of Python you have. 

When this is done, save and exit the file, exit your terminal by typing `exit` and restart it, typing in the following command: 
```
	source NAME_OF_FILE_EDITED
```
(e.g. `source ~/.profile` )

Type again in your terminal 
```
	sudo ldconfig
```
Finally, restart your computer.

You should now have GNU Radio properly installed on your machine. You can check this by typing the following command to start GNURadio Companion `gnuradio-companion`.

#### 2. gr-owc installation
Once here, you can follow the installation steps suggested on the module's official GitHub following this [link](https://github.com/UCaNLabUMB/gr-owc/tree/main)

However, I recommend the second method, without using Pybombs. Type the following commands in the folder you want
```
	git clone https://github.com/UCaNLabUMB/gr-owc.git
```
You will have a folder called `gr-owc` in your current folder, move into it and create a `build` folder and move into it too by typing the following commands: 
```
	cd gr-owc
	mkdir build
	cd build
```
Using `cmake`, don't forget to specify the prefix chosen if it's not the default as indicated above, otherwise you can directly run the following command
```
	cmake ../
```
Once this has been done, launch the `make` tool by typing it into your terminal:
```
	make
```
Perform the tests 
```
	make test
```
If all goes well, proceed with the installation. 
```
	sudo make install
```
Once you have done this, configure your linker/debugger again for the various DLLs by typing
```
	sudo ldconfig
```
And that's it! Open GNURadio-Companion and you'll usually find a module called `gr-owc` or `owc`. And voilà!