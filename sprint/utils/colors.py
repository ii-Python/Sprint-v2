# Modules
import os
import colorama
import subprocess

# Initialize colorama
colorama.init()

# Clear screen
cmd = "clear"
if os.name == "nt":
    cmd = "cls"

subprocess.run([cmd], shell = True)

# Color list
colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "cyan": "\033[36m",
    "blue": "\033[94m",
    "yellow": "\033[93m",
    "reset": "\033[0m"
}

# Colored function
def colored(text, color):
    return colors[color] + text + colors["reset"]

def color(color):
    return colors[color]
