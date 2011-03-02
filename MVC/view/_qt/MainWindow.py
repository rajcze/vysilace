import datetime

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_MainWindow import  Ui_MainWindow

class MainWindow(QMainWindow,  Ui_MainWindow):

    def __init__(self, parent = None, controller = None):
        super(self.__class__, self).__init__(parent)
        self.controller = controller
        self.setupUi(self)
        
        self.connect(self.timeButton, SIGNAL("clicked()"), self.tableView.init_grid)
        
        self.init_tableView()
    
    def init_tableView(self):
        pass
    
    
