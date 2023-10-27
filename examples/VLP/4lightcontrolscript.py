from xmlrpc.client import ServerProxy
import time

# Time Delay in Seconds
time_delay = 1

# Initialize amplitude and frequency settings as a dictionary
# where keys are signal numbers and values are the corresponding settings
amplitude_settings = {
    1: [1, 2, 3],
    2: [4, 5, 6],
    3: [7, 8, 9],
    # Add more signal settings if needed
}

frequency_settings = {
    1: [100, 200, 300],
    2: [400, 500, 600],
    3: [700, 800, 900],
    # Add more signal settings if needed
}
#Selector Block
# 0 = Single, 1 = Double.
select_configs = [0, 1, 0, 1]  # 1-2 use select1, 3-4 use select2, etc.
#Initialize server proxy
STA_TX1control = ServerProxy('http://10.1.1.2:8080')


# Loop through each selection block configuration
for j, select_config in enumerate(select_configs):
    block = j + 1
    print(f"[Current Select Configuration for block {block}: {select_config}]")
    getattr(STA_TX1control, f'set_select{block}')(select_config)

# Loop to set amplitude and frequency
for i in range(1, 9):  # Assuming 8 signals
    # If there are amplitude settings for this signal, apply them
    if i in amplitude_settings:
        for amp in amplitude_settings[i]:
            print(f"[Current TX Amplitude Settings for channel {i}: {amp}]")
            getattr(STA_TX1control, f'set_amp_{i}')(amp)
            time.sleep(time_delay)
    
    # If there are frequency settings for this signal, apply them
    if i in frequency_settings:
        for freq in frequency_settings[i]:
            print(f"[Current TX Frequency Settings for channel {i}: {freq}]")
            getattr(STA_TX1control, f'set_freq_{i}')(freq)
            time.sleep(time_delay)
