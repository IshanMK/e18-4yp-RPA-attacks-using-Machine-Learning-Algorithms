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
    with h5py.File('random_key_normalized.h5', 'w') as hf_normalized:
        # Iterate over all groups in the original HDF5 file
        for group_name, group in hf_data.items():
            # Create a new group in the output HDF5 file
            normalized_group = hf_normalized.create_group(group_name)
            # Iterate over all datasets in the group
            for dataset_name, dataset in group.items():
                if dataset_name == 'traces':
                    # Normalize traces using the fitted scaler
                    traces = np.array(dataset)
                    traces_normalized = scaler.transform(traces)
                    # Create a new dataset named "traces" with the normalized traces
                    normalized_group.create_dataset(name="traces", data=traces_normalized, dtype=traces_normalized.dtype)
                else:
                    # Copy other datasets as is
                    normalized_group.create_dataset(name=dataset_name, data=dataset[:], dtype=dataset.dtype)
