# Modules
from .args import Argument
from json import JSONEncoder

# Custom encoder class
class SprintJSONEncoder(JSONEncoder):
    def default(self, obj):

        # Check if object is an argument
        if isinstance(obj, Argument):
            return str(obj)

        # Encode it properly
        super().default(obj)
