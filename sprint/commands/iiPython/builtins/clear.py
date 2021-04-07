# Modules
import os
import subprocess

# Grab OS
OS = os.name
CMD = "clear"

if OS == "nt":
    CMD = "cls"

# Clear screen
subprocess.run([CMD], shell = True)
