# Modules
from .errors import SprintError

# Logger class
class Logger(object):
    def info(self, text: str):
        print(SprintError("info", text))

    def warn(self, text: str):
        print(SprintError("warn", text))

    def error(self, text: str):
        print(SprintError("error", text))
