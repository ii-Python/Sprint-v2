# write.py

# Modules
import os
import json
from rich import print

# Initialization
_SP_PARAMS = json.loads(os.getenv("SP_PARAMS"))

# Check pipe
if "pipe" in _SP_PARAMS and _SP_PARAMS["pipe"]:
    print(_SP_PARAMS["pipe"])

# Print arguments
[print(x) for x in _SP_PARAMS["args"]]
SP_RESULT = 0
