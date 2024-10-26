#!/bin/bash

# Define arrays for different flags
flag1_values=(value1a value1b value1c) # Replace with actual values for flag1
flag2_values=(value2a value2b)         # Replace with actual values for flag2
# Add more arrays for additional flags if needed

# Iterate through combinations of flag values
for val1 in "${flag1_values[@]}"; do
    for val2 in "${flag2_values[@]}"; do
        # Add loops for more flags if needed

        # Generate a unique filename for this combination of flag values
        filename="data_${val1}_${val2}_$(date +%s).dat"

        # Call the first GNU Radio flowgraph with the current combination of flag values
        python path/to/gnuradio_flowgraph.py --flag1 "$val1" --flag2 "$val2" # Add more flags as needed

        # Optional: Wait for the flowgraph to process and transmit data
        sleep 5

        # Call your Python XML-RPC script to set file name on the always-running second flowgraph
        python AFRL_Control_April_Autodata_Collection.py set_fn "$filename"

        # Optional: Add delay or additional commands if needed
        sleep 1
    done
done


