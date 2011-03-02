if __package__ is None:
    import sys
    sys.path.insert(1, "../../")
    sys.path.insert(1, "../")
    import MVC
    __package__ = "MVC.view"

import PyQt4.QtGui

from ..common.interfaces import iview

import _qt.MainWindow


class QtView(iview.IView):
    def __init__(self, *args, **kwargs):
        super(QtView, self).__init__(*args, **kwargs)
        self.ctl = None

    def setController(self, controller):
        self.ctl = controller

    def run(self):
        app = PyQt4.QtGui.QApplication(sys.argv)
        form = _qt.MainWindow.MainWindow(controller = self.ctl)
        form.show()
        app.exec_()

if __name__ == "__main__":
    v = QtView()
    v.run()

