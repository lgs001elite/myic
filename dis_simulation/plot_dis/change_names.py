import os
import glob

directory = "./"
pattern = "no_poweroff_51_general*"  # Wildcard pattern
num_chars_to_remove = 22  # Length of "prefix_"

for filepath in glob.glob(os.path.join(directory, pattern)):
    filename = os.path.basename(filepath)
    new_filename = filename[num_chars_to_remove:]
    new_filename = "no_poweroff_51_general_" + new_filename
    os.rename(filepath, os.path.join(directory, new_filename))
