from xmlrpc.client import ServerProxy
import time
import logging



#Initialize server proxy
STA_TX1control = ServerProxy('http://localhost:8080')

# Time Delay in Seconds
time_delay = 3





def set_amplitude(channel, amplitude):
    print(f"[Current TX Amplitude Settings for channel {channel}: {amplitude}]")
    getattr(STA_TX1control, f'set_amp_{channel}')(amplitude)

def set_frequency(channel, frequency):
    print(f"[Current TX Frequency Settings for channel {channel}: {frequency}]")
    getattr(STA_TX1control, f'set_freq_{channel}')(frequency)

def set_selection_block(block, select_config):
        print(f"[Sending Select Configuration for block {block}: {select_config}]")
        result = getattr(STA_TX1control, f'set_select{block}')(select_config)
        

def main(amplitude_settings, frequency_settings, select_configs):
    for i in range(1, len(amplitude_settings) * 2 + 1, 2): 
        select_idx = (i + 1) // 2
        select_config = select_configs[select_idx - 1]
        
        # Set the selection mode first
        set_selection_block(select_idx, select_config)

        # Then set amplitude and frequency
        for (amp1, freq1), (amp2, freq2) in zip(zip(amplitude_settings.get(i, []), frequency_settings.get(i, [])), zip(amplitude_settings.get(i + 1, []), frequency_settings.get(i + 1, []))):
            if select_config == 1:  # If in double tone
                set_amplitude(i, amp1)
                set_frequency(i, freq1)
                time.sleep(time_delay)  # You forgot to call time.sleep(time_delay) in the original code
                set_amplitude(i + 1, amp2)
                set_frequency(i + 1, freq2)
            else:  # If in single tone
                set_amplitude(i, amp1)
                set_frequency(i, freq1)

if __name__ == "__main__":
    

    amplitude_settings = {  
        1: [0.55],
        2: [0.25],
        # Add more signals/channels as needed/using two for simplified testing.
    }

    frequency_settings = {  
        1: [1000000],
        2: [1000000],
        # Add more signals/channels as needed/using two for simplified testing.
    }
    
    select_configs = [0,0,0,0]  
    
    main(amplitude_settings, frequency_settings, select_configs)


