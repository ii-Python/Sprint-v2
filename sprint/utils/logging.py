# Modules
# from .colors import colored
from ..core.handler.errors import SprintError

# Main log function
def handleLog(eclass, value):
    print(f"[{eclass}]: {value}")

    return SprintError(eclass, value)

# Connector
SprintLog = handleLog
