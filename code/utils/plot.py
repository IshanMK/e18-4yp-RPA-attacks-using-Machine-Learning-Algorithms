import sys
sys.path.append('/home/e18173/AISY_Framework')

import h5py
import matplotlib.pyplot as plt
filename = "/home/e18173/AISY_Framework/resources/datasets/random_key_190.h5"

# Open the H5 file in read mode
with h5py.File(filename, 'r') as file:
    # Define the keys of interest
    keys_of_interest = ['Attack_traces', 'Profiling_traces']
    
    # Initialize a figure for combined histograms
    # plt.figure(figsize=(12, 8))
    plt.figure()

    # Define colors for the histograms
    colors = ['blue', 'red']
    
    # Iterate over each key and corresponding color
    for key, color in zip(keys_of_interest, colors):
        # Get the traces data
        traces = file[key]['traces'][:]
        
        # Plot histogram of traces
        # plt.hist(traces.flatten(), bins=25, density=True, alpha=0.7, label=key, color=color)
        
        #  # Plot wave signal of traces (taking the mean trace for simplicity)
        mean_trace = traces.mean(axis=0)
        plt.plot(mean_trace, label=key, color=color)
    
    # Add labels and title
    # plt.xlabel('Trace Values' , fontsize=16)
    # plt.ylabel('Frequency' , fontsize=16)
    
    plt.xlabel('Sample point' , fontsize=14)
    plt.ylabel('Mean value of TDC outputs' , fontsize=16)
    # plt.title('Wave Signal of Attack and Profiling Traces' , fontsize=18)
    # plt.title('Histogram of Attack and Profiling Traces' , fontsize=18)
    plt.legend(fontsize=14)
    
    # Increase font size of tick labels
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    # Save the figure
    plt.savefig('combined_wave_random_key.jpg' , dpi=1200)
    # plt.savefig('combined_histograms_random_key.jpg' , dpi=1200)
    
    # Show the figure
    plt.show()
