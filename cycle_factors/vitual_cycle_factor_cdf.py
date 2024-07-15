import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

def plot_cdf(data, label):
    # Sort the data
    sorted_data = np.sort(data)
    # Calculate the CDF values
    cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    
    # Plot the CDF
    plt.plot(sorted_data, cdf, marker='.', linestyle='none', label=label)



csv_directory = ''  # Replace with your directory path
csv_files = glob.glob(csv_directory + '*.csv')
column_index = 0 
for csv_file in csv_files:
    # Read the CSV file without headers
    df = pd.read_csv(csv_file, header=None)
    data = df.iloc[:, column_index].dropna().values  # Drop any NaN values
    
    # Extract the file name without extension for labeling
    file_label = csv_file.split('/')[-1].split('.')[0]
    
    # Plot the CDF for the current CSV file
    plot_cdf(data, file_label)

# Customize the plot
plt.xlabel(f'Column {column_index + 1}')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function (CDF)')
plt.grid(True)
plt.legend()
plt.show()
