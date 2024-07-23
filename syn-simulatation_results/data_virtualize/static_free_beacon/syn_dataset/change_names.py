import os
import glob

directory = "./"
pattern = "special_*"  # Wildcard pattern
num_chars_to_remove = 8  # Length of "prefix_"

for filepath in glob.glob(os.path.join(directory, pattern)):
    filename = os.path.basename(filepath)
    new_filename = filename[num_chars_to_remove:]
    os.rename(filepath, os.path.join(directory, new_filename))
