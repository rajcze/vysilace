import datetime
import copy

if __package__ is None:
    import sys
    sys.path.insert(1, "../../")
    sys.path.insert(1, "../")
    import MVC
    __package__ = "MVC.controller"

from ..common.interfaces import icontroller

class Controller(icontroller.IController):
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.setController(self)