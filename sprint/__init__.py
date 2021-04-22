# Base system
from .utils.rich import console
from .utils.logging import SprintLog
from .core.parser.parser import Parser
from .core.handler.errors import SprintError

# Module extenders
from .utils.path import PATH

# Metadata
__author__ = "iiPython"
__copyright__ = "©2021 iiPython"
__license__ = "MIT"

__version__ = "1.0.0"
