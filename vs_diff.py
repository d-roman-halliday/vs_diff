################################################################################
# Create an interface to build command line for diff using Visual Studio
#
# Create two file open dialogues to select the files
# Then open a diff too comparing them
#
# ToDo: Modify input to take argument(s) for files, see below link
#       https://stackoverflow.com/questions/8570288/run-python-script-on-selected-file
################################################################################
import subprocess
import tkinter as tk
from tkinter import filedialog

# Configure
VisualStudio_command=r'C:\Program Files (x86)\Microsoft Visual Studio\2017\SQL\Common7\IDE\devenv.exe'

#Craete base widgets
root = tk.Tk()
root.withdraw()

# Get file paths
file_path1 = filedialog.askopenfilename()
file_path2 = filedialog.askopenfilename()

#Output for debugging
#print(file_path1)
#print(file_path2)

#Run command (capturing output for future use)
proc_output = subprocess.check_output([VisualStudio_command,
                                       '/diff',
                                       file_path1,
                                       file_path2
                                      ],
                                      shell=True)
