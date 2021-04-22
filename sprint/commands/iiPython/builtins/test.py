# test.py
# Command to test sprint features

# Modules
import os
import json

# Initialization
PARAMS = json.loads(os.getenv("SP_PARAMS"))
print(PARAMS)
