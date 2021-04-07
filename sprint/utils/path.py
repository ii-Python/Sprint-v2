# path.py
# handles what sprint is able to see

# Modules
import os

# Constants
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

# Path
PATH = [
    os.path.abspath(f"{ROOT}/commands")
]
# PATH = []  # If you wish to test exceptions, uncomment this.
