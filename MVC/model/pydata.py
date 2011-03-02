if __package__ is None:
    import sys
    sys.path.insert(1, "../../")
    sys.path.insert(1, "../")
    import MVC
    __package__ = "MVC.model"

from ..common.interfaces import imodel


class PyDataModel(imodel.IModel):
    def __init__(self):
        pass

if __name__ == "__main__":
    pass