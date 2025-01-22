import numpy as np
import h5py
from sklearn.preprocessing import StandardScaler

# Set a fixed random seed for reproducibility
np.random.seed(42)

# Read the HDF5 file containing the dataset
with h5py.File('random_key.h5', 'r') as hf_data:
    
    # Get the profiling traces
    profiling_traces = np.array(hf_data['Profiling_traces']['traces'])
    # Fit the scaler to the profiling traces
    scaler = StandardScaler().fit(profiling_traces)
    
    # Create a new HDF5 file to store the transformed traces and other groups
    with h5py.File('random_key_fft_normalized.h5', 'w') as hf_fft:
        # Iterate over all groups in the original HDF5 file
        for group_name, group in hf_data.items():
            # Check if the group contains traces
            if 'traces' in group:
                # Apply Fourier transform to the traces in this group
                traces = np.array(group['traces'])
                # Normalize the traces
                traces_normalized = scaler.transform(traces)
                traces_fft = np.fft.fft(traces_normalized, axis=1)
                # Compute the magnitude of the FFT-transformed traces
                traces_fft_magnitude = np.abs(traces_fft)
                # Create a new group in the output HDF5 file
                fft_group = hf_fft.create_group(group_name)
                # Create a new dataset named "traces" with the magnitude of FFT-transformed traces
                fft_group.create_dataset(name="traces", data=traces_fft_magnitude, dtype=traces_fft_magnitude.dtype)
                # Copy all other datasets and their content from the original group
                for dataset_name, dataset in group.items():
                    if dataset_name != 'traces':
                        fft_group.create_dataset(name=dataset_name, data=dataset[:], dtype=dataset.dtype)
            else:
                # Copy the group and its content as is
                hf_data.copy(group_name, hf_fft)
