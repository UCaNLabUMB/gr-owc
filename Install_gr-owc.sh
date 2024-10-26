#!/bin/bash

if [ -d gr-owc ]; then
    echo "Directory gr-owc already exists."
    
    read -p "Existing directory gr-owc must be removed for proceeding installation. Do you want to remove this directory and continue? (y/n): " response

    case "$response" in
        [Yy]* )
            echo "Removing directory gr-owc"
            sudo rm -rf gr-owc
            if [ $? -ne 0 ]; then
                echo "Failed to remove directory gr-owc"
                exit 1
            fi
            ;;
        [Nn]* )
            echo "Aborting installation. Directory gr-owc will not be removed."
            exit 1
            ;;
        * )
            echo "Invalid response. Aborting installation."
            exit 1
            ;;
    esac
fi

git clone https://github.com/UCaNLabUMB/gr-owc.git
if [ $? -ne 0 ]; then
    echo "Failed to clone repository from https://github.com/UCaNLabUMB/gr-owc.git"
    exit 1
fi

cd gr-owc
if [ $? -ne 0 ]; then
    echo "Failed to find gr-owc directory"
    exit 1
fi

mkdir build
if [ $? -ne 0 ]; then
    echo "Failed to create build directory in gr-owc"
    exit 1
fi

cd build
if [ $? -ne 0 ]; then
    echo "Failed to move to build directory in gr-owc"
    exit 1
fi

cmake ..
if [ $? -ne 0 ]; then
    echo "Failed to run CMake"
    exit 1
fi

make
if [ $? -ne 0 ]; then
    echo "Failed to compile(make failed)"
    exit 1
fi

make test
if [ $? -ne 0 ]; then
    echo "Test cases of gr-owc blocks failed"
    exit 1
fi

sudo make install
if [ $? -ne 0 ]; then
    echo "Failed to install"
    exit 1
fi

sudo ldconfig
if [ $? -ne 0 ]; then
    echo "Failed to update the linking for the gr-owc library"
    exit 1
fi

echo "The gr-owc module installation is successfully completed and should now be available in GNU Radio Companion."