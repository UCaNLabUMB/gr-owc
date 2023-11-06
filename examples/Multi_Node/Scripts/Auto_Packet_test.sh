#!/bin/bash

# Define the path select values you want to loop through
path_select_values=(0 1)

# Define an array of unique file names for each test scenario
file_names=("config1" "config2" "config3") # Add more names as needed

# Loop through each path select value
for path_select in "${path_select_values[@]}"; do
  # Loop through each file name for the current path select value
  for file_name in "${file_names[@]}"; do

    # Set the path select
    echo "Setting path select to $path_select..."
    ./your_script.py set_path_select $path_select
    
    # Wait a bit to make sure the command has been processed
    sleep 2

    # Rename the file
    echo "Renaming file to $file_name..."
    ./your_script.py set_fn $file_name

    # Wait for 10 seconds before the next iteration
    sleep 10
  done
done

echo "All configurations have been set."
