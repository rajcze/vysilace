if __package__ is None:
    import sys
    sys.path.insert(1, "../../")
    sys.path.insert(1, "../")
    import MVC
    __package__ = "MVC.controller"

__all__ = ['controller']

from controller import *