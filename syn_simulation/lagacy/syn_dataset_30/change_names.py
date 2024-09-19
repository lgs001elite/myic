import os
import glob

directory = "./"
pattern = "scalability_30*"  # Wildcard pattern
num_chars_to_remove = 14  # Length of "prefix_"

for filepath in glob.glob(os.path.join(directory, pattern)):
    filename = os.path.basename(filepath)
    new_filename = filename[num_chars_to_remove:]
    new_filename = "no_poweroff_30_general" + new_filename
    os.rename(filepath, os.path.join(directory, new_filename))
