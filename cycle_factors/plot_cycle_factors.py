
# import subprocess
# import sys
# import time
# import random
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Function to install and import packages
# def install_and_import(package):
#     try:
#         __import__(package)
#     except ImportError:
#         print(f"{package} not found. Installing...")
#         subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#         print(f"{package} installed successfully.")
#     finally:
#         globals()[package] = __import__(package)

# # Ensure required packages are installed
# install_and_import('matplotlib')

# # Set global plot parameters
# plt.rcParams.update({
#     'font.size': 15,
#     'font.family': 'Arial',
#     'figure.figsize': (18, 6),  # Increased width to accommodate three plots
#     'axes.labelsize': 16,
#     'axes.titlesize': 18,
#     'legend.fontsize': 12,
#     'xtick.labelsize': 12,
#     'ytick.labelsize': 12
# })

# # Define scenarios
# scenarios = ["300 slots", "[1,500] slots", "[300,500] slots"]

# # Define colors for each scenario
# colors = ['red', 'green', 'orange']

# # Threshold value (adjust if needed)
# threshold = 502

# def merge_series_average(series1, series2):
#     """
#     Merge two pandas Series by averaging their corresponding values.
#     If Series have different lengths, they are trimmed to the shortest length.

#     Parameters:
#     - series1: pandas.Series
#     - series2: pandas.Series

#     Returns:
#     - merged_series: pandas.Series
#     """
#     # Find the minimum length
#     min_length = min(len(series1), len(series2))
    
#     # Trim both Series to the minimum length
#     trimmed_series1 = series1.iloc[:min_length].reset_index(drop=True)
#     trimmed_series2 = series2.iloc[:min_length].reset_index(drop=True)
    
#     # Compute the average
#     merged_series = (trimmed_series1 + trimmed_series2) / 2
    
#     return merged_series

# if __name__ == "__main__":
#     # Create a figure with three subplots arranged in a row
#     plt.rcParams['font.family'] = 'Arial'
#     plt.rcParams.update({'font.size': 20})
#     fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(6, 5), sharey=True)
    
#     # Adjust font settings for individual plots if needed
#     import matplotlib as mpl
#     mpl.rcParams["legend.loc"] = 'best'
    
#     for index, (scenario, ax) in enumerate(zip(scenarios, axes)):
#         ave_neu = pd.Series(dtype='float')  # Initialize as empty Series
#         x_ticks = np.array([])  # Initialize empty x_ticks

#         if scenario == "[300,500] slots":
#             try:
#                 # Read both front and back CSV files
#                 csvRecorder_front = pd.read_csv("front-[300,500].csv")
#                 csvRecorder_back = pd.read_csv("back-[300,500].csv")
                
#                 # Ensure the '1' column exists in both CSVs
#                 if '1' not in csvRecorder_front.columns or '1' not in csvRecorder_back.columns:
#                     raise KeyError("Column '1' not found in one of the CSV files.")
                
#                 # Extract the '1' column from both
#                 ave_neu_front = csvRecorder_front["1"]
#                 ave_neu_back = csvRecorder_back["1"]
                
#                 # Merge the Series by averaging
#                 ave_neu = pd.concat([ave_neu_front, ave_neu_back], ignore_index=True)
                
#                 # Define cycle sizes from 300 to 500
#                 cycle_start = 1
#                 cycle_end = 500
#                 expected_length = cycle_end - cycle_start + 1  # 500
                
#                 actual_length = len(ave_neu)
#                 print(f"[300,500] slots: Expected {expected_length} data points, got {actual_length}.")
#                 ax.set_xlabel("Cycle size")
#                 if actual_length != expected_length:
#                     print(f"Warning: Expected {expected_length} data points, but got {actual_length}. Adjusting x_ticks accordingly.")
#                     x_ticks = np.arange(cycle_start, cycle_start + actual_length)
#                 else:
#                     x_ticks = np.arange(cycle_start, cycle_end + 1)
            
#             except FileNotFoundError as e:
#                 print(f"Error reading merged files: {e}")
#                 ave_neu = pd.Series([0]*threshold)
#                 x_ticks = np.arange(1, threshold + 1)
#             except KeyError as e:
#                 print(f"Error: {e}")
#                 ave_neu = pd.Series([0]*threshold)
#                 x_ticks = np.arange(1, threshold + 1)
#             ax.plot(x_ticks, ave_neu, label=scenario, color=colors[index])
        
#         elif scenario == "[1,500] slots":
#             try:
#                 csvRecorder = pd.read_csv("[1,500].csv")
                
#                 if '1' not in csvRecorder.columns:
#                     raise KeyError("Column '1' not found in [1,500].csv.")
                
#                 ave_neu = csvRecorder['1']
                
#                 # Define cycle sizes from 1 to 500
#                 cycle_start = 1
#                 cycle_end = 500
#                 expected_length = cycle_end - cycle_start + 1  # 500
                
#                 actual_length = len(ave_neu)
#                 print(f"[1,500] slots: Expected {expected_length} data points, got {actual_length}.")
                
#                 if actual_length != expected_length:
#                     print(f"Warning: Expected {expected_length} data points, but got {actual_length}. Adjusting x_ticks accordingly.")
#                     x_ticks = np.arange(cycle_start, cycle_start + actual_length)
#                 else:
#                     x_ticks = np.arange(cycle_start, cycle_end + 1)
#                 x_ticks = ""
            
#             except FileNotFoundError:
#                 print("File [1,500].csv not found.")
#                 ave_neu = pd.Series([0]*threshold)
#                 x_ticks = np.arange(1, threshold + 1)
#             except KeyError as e:
#                 print(f"Error: {e}")
#                 ave_neu = pd.Series([0]*threshold)
#                 x_ticks = np.arange(1, threshold + 1)
#             ax.plot(ave_neu, label=scenario, color=colors[index])
#         elif scenario == "300 slots":
#             try:
#                 csvRecorder = pd.read_csv("[300].csv")
                
#                 if '1' not in csvRecorder.columns:
#                     raise KeyError("Column '1' not found in [300].csv.")
                
#                 ave_neu = csvRecorder['1']
                
#                 # Define cycle size as fixed at 300 for all data points
#                 x_ticks = "" # Assuming cycle size is plotted against index or another variable
            
#             except FileNotFoundError:
#                 print("File [300].csv not found.")
#                 ave_neu = pd.Series([0]*threshold)
#                 x_ticks = np.arange(1, threshold + 1)
#             except KeyError as e:
#                 print(f"Error: {e}")
#                 ave_neu = pd.Series([0]*threshold)
#                 x_ticks = np.arange(1, threshold + 1)
        
#         else:
#             print(f"Unknown scenario: {scenario}")
#             ave_neu = pd.Series([0]*threshold)
#             x_ticks = np.arange(1, threshold + 1)
#         ax.plot( ave_neu, label=scenario, color=colors[index])
        
#         # Set titles and labels for each subplot
#         #ax.set_title(scenario)
#         if index == 1:
#             ax.set_ylabel("Average syn [slots]")
#         ax.set_yscale('log')
        
#         # Apply tick formatting only to x-axis
#         ax.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
        
#         # Add legend to each subplot
#         ax.legend()
        
#         # Optional: Add grid for better readability
#         #ax.grid(True, which="both", ls="--", linewidth=0.5)
    
#     # Adjust layout to prevent overlap
#     plt.tight_layout()
    
#     # Save and display the plot
#     plt.savefig("cycle_size_syn_merged.pdf", format='pdf')
#     plt.show()
#     plt.close("all")










import subprocess
import sys
import time
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to install and import packages
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"{package} installed successfully.")
    finally:
        globals()[package] = __import__(package)

# Ensure required packages are installed
install_and_import('matplotlib')

# Set global plot parameters
plt.rcParams.update({
    'font.size': 15,
    'font.family': 'Arial',
    'figure.figsize': (10, 18),  # Increased height to accommodate three vertically stacked plots
    'axes.labelsize': 16,
    'axes.titlesize': 18,
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12
})

# Define scenarios
scenarios = ["300 slots", "[1,500] slots", "[300,500] slots"]

# Define colors for each scenario
colors = ['red', 'green', 'orange']

# Threshold value (adjust if needed)
threshold = 502

def merge_series_average(series1, series2):
    """
    Merge two pandas Series by averaging their corresponding values.
    If Series have different lengths, they are trimmed to the shortest length.

    Parameters:
    - series1: pandas.Series
    - series2: pandas.Series

    Returns:
    - merged_series: pandas.Series
    """
    # Find the minimum length
    min_length = min(len(series1), len(series2))
    
    # Trim both Series to the minimum length
    trimmed_series1 = series1.iloc[:min_length].reset_index(drop=True)
    trimmed_series2 = series2.iloc[:min_length].reset_index(drop=True)
    
    # Compute the average
    merged_series = (trimmed_series1 + trimmed_series2) / 2
    
    return merged_series

if __name__ == "__main__":
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams.update({'font.size': 20})
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(6, 5), sharey=True)
    
    # Adjust font settings for individual plots if needed
    import matplotlib as mpl
    mpl.rcParams["legend.loc"] = 'best'
    
    for index, (scenario, ax) in enumerate(zip(scenarios, axes)):
        ave_neu = pd.Series(dtype='float')  # Initialize as empty Series
        x_ticks = np.array([])  # Initialize empty x_ticks

        if scenario == "[300,500] slots":
            try:
                # Read both front and back CSV files
                csvRecorder_front = pd.read_csv("front-[300,500].csv")
                csvRecorder_back = pd.read_csv("back-[300,500].csv")
                
                # Ensure the '1' column exists in both CSVs
                if '1' not in csvRecorder_front.columns or '1' not in csvRecorder_back.columns:
                    raise KeyError("Column '1' not found in one of the CSV files.")
                
                # Extract the '1' column from both
                ave_neu_front = csvRecorder_front["1"]
                ave_neu_back = csvRecorder_back["1"]
                
                # Merge the Series by averaging
                ave_neu = pd.concat([ave_neu_front, ave_neu_back], ignore_index=True)
                
                # Define cycle sizes from 1 to 500
                cycle_start = 1
                cycle_end = 500
                expected_length = cycle_end - cycle_start + 1  # 500
                
                actual_length = len(ave_neu)
                print(f"[300,500] slots: Expected {expected_length} data points, got {actual_length}.")
                
                if actual_length != expected_length:
                    print(f"Warning: Expected {expected_length} data points, but got {actual_length}. Adjusting x_ticks accordingly.")
                    x_ticks = np.arange(cycle_start, cycle_start + actual_length)
                else:
                    x_ticks = np.arange(cycle_start, cycle_end + 1)
            
            except FileNotFoundError as e:
                print(f"Error reading merged files: {e}")
                ave_neu = pd.Series([0]*threshold)
                x_ticks = np.arange(1, threshold + 1)
            except KeyError as e:
                print(f"Error: {e}")
                ave_neu = pd.Series([0]*threshold)
                x_ticks = np.arange(1, threshold + 1)
        
        elif scenario == "[1,500] slots":
            try:
                csvRecorder = pd.read_csv("[1,500].csv")
                
                if '1' not in csvRecorder.columns:
                    raise KeyError("Column '1' not found in [1,500].csv.")
                
                ave_neu = csvRecorder['1']
                
                # Define cycle sizes from 1 to 500
                cycle_start = 1
                cycle_end = 500
                expected_length = cycle_end - cycle_start + 1  # 500
                
                actual_length = len(ave_neu)
                print(f"[1,500] slots: Expected {expected_length} data points, got {actual_length}.")
                
                if actual_length != expected_length:
                    print(f"Warning: Expected {expected_length} data points, but got {actual_length}. Adjusting x_ticks accordingly.")
                    x_ticks = np.arange(cycle_start, cycle_start + actual_length)
                else:
                    x_ticks = np.arange(cycle_start, cycle_end + 1)
            
            except FileNotFoundError:
                print("File [1,500].csv not found.")
                ave_neu = pd.Series([0]*threshold)
                x_ticks = np.arange(1, threshold + 1)
            except KeyError as e:
                print(f"Error: {e}")
                ave_neu = pd.Series([0]*threshold)
                x_ticks = np.arange(1, threshold + 1)
        
        elif scenario == "300 slots":
            try:
                csvRecorder = pd.read_csv("[300].csv")
                
                if '1' not in csvRecorder.columns:
                    raise KeyError("Column '1' not found in [300].csv.")
                
                ave_neu = csvRecorder['1']
                
                # Define cycle size as fixed at 300 for all data points
                # Since cycle size is fixed, we can use the index as x-axis
                x_ticks = np.arange(1, len(ave_neu) + 1)  # Using index as x-axis
                cycle_size_fixed = 300  # Fixed cycle size
                
            except FileNotFoundError:
                print("File [300].csv not found.")
                ave_neu = pd.Series([0]*threshold)
                x_ticks = np.arange(1, threshold + 1)
            except KeyError as e:
                print(f"Error: {e}")
                ave_neu = pd.Series([0]*threshold)
                x_ticks = np.arange(1, threshold + 1)
        
        else:
            print(f"Unknown scenario: {scenario}")
            ave_neu = pd.Series([0]*threshold)
            x_ticks = np.arange(1, threshold + 1)
        
        # Plot the data on the current subplot
        if index == 2:
            ax.plot(x_ticks, ave_neu, label=scenario, color=colors[index])
            ax.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
            ax.set_xlabel("Cycle size")
        else:
            ax.plot(ave_neu, label=scenario, color=colors[index])
            ax.set_xticklabels("")
            if index == 1:
                 ax.set_ylabel("Average syn [slots]")
        
        ax.set_yscale('log')
    
        ax.legend()
        
        # Optional: Add grid for better readability
        #ax.grid(True, which="both", ls="--", linewidth=0.5)
    
    # Adjust layout to prevent overlap
    

    plt.tight_layout(pad=0.5, w_pad=0.5, h_pad=0)
    
    # Save and display the plot
    plt.savefig("cycle_size_syn_merged.pdf", format='pdf')
    plt.show()
    plt.close("all")

