class SprintError(object):

    def __init__(self, eclass, info):
        self.class_ = eclass.upper()
        self.info = info

    def __repr__(self):
        return f"[{self.class_}]: {self.info}"
