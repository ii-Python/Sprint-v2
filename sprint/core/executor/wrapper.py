# Modules
from .loader import Loader
from ..handler.logging import Logger
from ..handler.params import SprintParams

# Load path
from ...utils.path import PATH

# Initialization
LOADER = Loader(PATH)
LOGGER = Logger()

# Main command class
class Command(object):

    def __init__(self, command: str, params: SprintParams = {}):
        self.cmd = command
        self.params = params

    def execute(self):

        # Grab command
        status, command = LOADER.locate_command(self.cmd)
        if status is False:
            if not command:
                return LOGGER.error(f"command '{self.cmd}' not found.")

        else:
            print("Command conflict found, below are your options:")
            for match in command:
                print(match)

            return

        command = command[0]
        location = command["command"]["path"]

        print(command, location)

        # Check
        return True
