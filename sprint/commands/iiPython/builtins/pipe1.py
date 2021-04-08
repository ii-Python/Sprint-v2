# Modules
import os
import json

# Grab pipe
PARAMS = json.loads(os.getenv("SP_PARAMS"))
if "pipe" in PARAMS:
    print(PARAMS)
    print(f"\n\nPipe (pipe1.py):\n{PARAMS['pipe']}")

else:
    print("Nothing piped.")

# Result
SP_RESULT = 0
