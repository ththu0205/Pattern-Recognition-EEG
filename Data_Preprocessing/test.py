import kagglehub
from scipy.io import loadmat
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Download latest version
path = kagglehub.dataset_download("inancigdem/eeg-data-for-mental-attention-state-detection")

print("Path to dataset files:", path)

# Collect all file names
file_names = []
for dirname, _, filenames in os.walk(path):
    for filename in filenames:
        file_names.append(os.path.join(dirname, filename))

# Load and analyze data from all files
all_data = []
for i in range(3):
    try:
        record = loadmat(file_names[i])
        if 'o' not in record:
            print(f"File {i+1} does not contain key 'o'. Skipping.")
            continue
        
        mdata = record['o']  # main object
        sample1 = {n: mdata[n][0,0] for n in mdata.dtype.names}

        data = sample1['data']
        trials = sample1['trials']

        print(f'File {i+1} - data shape:', data.shape)

        # Plot full data (limiting to the first 1000 samples for visualization purposes)
        plt.figure(figsize=(10, 3))
        plt.plot(data[:1000])  # Limiting to first 1000 samples
        plt.title(f'Full Data from File {i+1}')
        plt.xlabel('Samples')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

        # Extract EEG data (Channels 4-17)
        data_eeg = data[:, 4:18]
        print(f'File {i+1} - data_eeg shape:', data_eeg.shape)

        # Plot extracted EEG data (limiting to the first 1000 samples)
        plt.figure(figsize=(10, 3))
        plt.plot(data_eeg[:1000])
        plt.title(f'EEG Data (Channels 4-17) from File {i+1}')
        plt.xlabel('Samples')
        plt.ylabel('EEG Amplitude')
        plt.grid(True)
        plt.show()

        all_data.append(data_eeg)
    except Exception as e:
        print(f"Error processing file {i+1}: {e}")

# Kết hợp dữ liệu từ tất cả các file thành một array duy nhất
if all_data:
    combined_data = np.concatenate(all_data, axis=0)
    print("Kích thước dữ liệu kết hợp:", combined_data.shape)

    # Chuyển đổi sang Pandas DataFrame
    columns = [f'Channel_{i}' for i in range(4, 18)]
    df = pd.DataFrame(combined_data, columns=columns)
else:
    print("Không có dữ liệu nào để kết hợp.")
