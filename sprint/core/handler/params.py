# Parameter class
class SprintParams(object):

    def __init__(self, values: dict = {}):
        self.values = values

    def __repr__(self):
        return str(self.values)

    def set(self, name: str, value = None):
        self.values[name] = value
        return self.values[name]

    def get(self, name: str):
        return self.values[name] if name in self.values else None
