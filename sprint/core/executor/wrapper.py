# Modules
from .loader import Loader
from ..handler.params import SprintParams

# Load path
from ...utils.path import PATH

# Initialize loader
LOADER = Loader(PATH)

# Main command class
class Command(object):

    def __init__(self, command: str, params: SprintParams = {}):
        self.cmd = command
        self.params = params

    def execute(self):

        # Check
        return True
