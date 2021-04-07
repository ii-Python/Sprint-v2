# loader.py
# handles command loading

# Modules
from ..handler.logging import Logger

# Main loader class
class Loader(object):
    def __init__(self, path: list = []):
        self.path = path
        self.logger = Logger()

        if not self.path:
            self.logger.warn("sprint path is empty, no commands will be loaded.")

    def locate_command(self, name: str):
        return
