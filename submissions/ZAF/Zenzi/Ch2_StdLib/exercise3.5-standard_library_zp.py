# Exercise 3.5
"""Use the sys module to create a relative path from a Python module, print that path.
Zenzi Pahla
UN-OG Core training
25 January 2025
"""
# Importing the sys and os modules"
import sys
import os   #for accessing the filesystem.

# Getting the path of the current script:
current_script = os.path.abspath(sys.argv[0])  #sys.argv[0] returns the path of the currently running .py script

# Getting the directory of the current script:
current_directory = os.path.dirname(current_script) #dirname() extracts the current directory of the .py script path

# Creating a relative path to a file in a subdirectory:
relative_path = os.path.join(current_directory, 'subdir', 'file.txt') #join() combines the current directory with a subdirectory and file name to create a relative path.

# Printing the relative path:
print(f"Relative path: {relative_path}")