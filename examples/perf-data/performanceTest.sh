#!/bin/bash

# Purpose:
#   Sweep a range of sample rates (and samples-per-symbol, Modulation-Order) for a GNU Radio flowgraph
#   and record the average CPU core utilization for a specific “Unit Under Test” (UUT)
#   block/thread while the flowgraph runs.

# How it works (high level):
#   1) Launches `python3 test.py (GNU Radio flowgrapgh)` with a selected sample rate (and sps, mo).
#   2) Waits briefly for the flowgraph to stabilize.
#   3) Samples CPU usage of the UUT thread 15 times using `pidstat -t`.
#   4) Averages those samples and appends a line to a results file.
#   5) Repeats for all parameter combinations and prints the results.

# Usage:
#   chmod +x performanceTest.sh
#   ./performanceTest.sh

# Notes:
#   - Update `block_names` to the exact thread/block identifiers shown by `pidstat -t`.
#     If you’re unsure, run your flowgraph and execute: `pidstat -t -p <PID> 1`
#   - The field extraction (`awk '{print $(NF-2)}'`) assumes the “%CPU” column is
#     the third field from the end in your `pidstat` version. Adjust if needed.
#   - `kill $pid` is called after the measurement; ensure `test.py` exits cleanly.

# Sample rates to test. Add/remove values as needed.
sample_rates=("10000" "25000" "50000" "75000" "100000" "250000" "500000" "750000" "1000000" "2500000" "5000000" "7500000" "10000000" "15000000" "25000000" "35000000" "50000000" "75000000" "100000000" "125000000" "150000000" "175000000" "200000000" "225000000" "250000000" "275000000" "300000000" "325000000" "350000000" "375000000" "400000000" "425000000" "450000000" "475000000" "500000000" "525000000" "550000000" "575000000" "600000000")

# Names of the UUT block/thread as it appears in `pidstat -t` output.
# You can list multiple blocks to sweep them one by one.
block_names=("OOK_Modulator_c")

# Samples per symbol values to sweep
sps=("1" "5" "20")

# Modulation order sweep values
order=("4" "8" "16")

# Output file setup
temp_file="cpu_utilization_results.txt"
> $temp_file

# -----------------------
# Helper: Average CPU utilization for a given PID/UUT
# -----------------------
# get_avg_cpu_utilization <pid>
# Uses `pidstat -t 1 1` to collect snapshot of per-thread CPU core usage,
# greps for the UUT `block_name`, and extracts the %CPU column.
# Repeats 15 times with a 1s sleep between iterations, then averages
get_avg_cpu_utilization() {
    local pid=$1
    local total_cpu=0
    local count=0

    # Collect 15 samples
    for i in {1..15}; do
        cpu=$(pidstat -p $pid -t 1 1 | grep "$block_name" | tail -1 | awk '{print $(NF-2)}')
        if [[ ! -z "$cpu" ]]; then
            total_cpu=$(echo "$total_cpu + $cpu" | bc)
            count=$((count + 1))
        fi
        sleep 1
    done

    if [[ $count -gt 0 ]]; then
        avg_cpu=$(echo "scale=2; $total_cpu / $count" | bc)
    else
        avg_cpu="0.00"
    fi

    echo $avg_cpu
}


for ((i=0; i<${#block_names[@]}; i++)); do
    for samp_sym in "${sps[@]}"; do
        for samp_rate in "${sample_rates[@]}"; do
            block_name=${block_names[$i]}
        
            # Run flowgrapgh passing along sample rate (and SPS, MO) using parameter block
            python3 test.py -r "$samp_rate" -v "$samp_sym" &
            pid=$!
            sleep 10  

            if ps -p $pid > /dev/null; then
                #avg_cpu_percent=$(get_avg_cpu_utilization $pid $block_name)
                avg_cpu_percent=$(get_avg_cpu_utilization $pid)
                echo "$block_name $samp_rate $avg_cpu_percent" >> $temp_file
                kill $pid
            else
                echo "$block_name $samp_rate Process not found" >> $temp_file
            fi
            kill $pid
        done
    done
done


cat $temp_file