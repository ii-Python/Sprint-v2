# Modules
import os
import sys
import json
import importlib.util
from os.path import dirname
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

        # Change location to a more readable format
        location = location.replace("\\", "/")

        # Create environment
        sys.argv = [repr(self.cmd)] + self.params.get("args")  # Enable existing CLIs to function

        os.environ["SP_WORKDIR"] = os.getcwd()  # Current working directory
        os.environ["SP_ASSETDIR"] = dirname(location)  # Top level directory of command

        os.environ["SP_PARAMS"] = json.dumps(self.params.values)

        sys.path.append(os.getenv("SP_ASSETDIR"))

        # Try to import the command
        try:
            spec = importlib.util.spec_from_file_location(
                command["command"]["full_name"],
                location
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

        except Exception as Error:
            return LOGGER.error(Error)

        # Grab value
        if not hasattr(module, "SP_RESULT"):
            result = None

        else:
            result = module.SP_RESULT

        return result
