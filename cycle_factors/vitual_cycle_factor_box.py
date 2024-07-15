import pandas as pd
import matplotlib.pyplot as plt
import glob

# Directory containing the CSV files
csv_directory = ''  # Replace with your directory path
csv_files = glob.glob(csv_directory + '*.csv')

# Column index to extract data from (0-based index)
column_index = 0  # Replace with your column index

# List to store data from each CSV file
data_list = []

# Iterate through each CSV file
for csv_file in csv_files:
    # Read the CSV file without headers
    df = pd.read_csv(csv_file, header=None)
    data = df.iloc[:, column_index].dropna().values  # Drop any NaN values
    
    # Append the data to the list
    data_list.append(data)

# Create a box plot
plt.figure(figsize=(10, 6))
plt.boxplot(data_list, patch_artist=True)

# Customize the plot
plt.xlabel('CSV Files')
plt.ylabel(f'Column {column_index + 1}')
plt.title('Box Plot for Multiple CSV Files')
plt.grid(True)

# Set x-tick labels to the CSV file names (without directory path and extension)
file_labels = [csv_file.split('/')[-1].split('.')[0] for csv_file in csv_files]
plt.xticks(range(1, len(file_labels) + 1), file_labels, rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
