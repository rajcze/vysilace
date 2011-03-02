from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Cell(QTableWidgetItem):
    pass
#    def __init__(self):
#        super(self.__class__, self).__init__()

class Spreadsheet(QTableWidget):
    def __init__(self, parent = None):
        super(self.__class__, self).__init__(parent)
        self.prototype_cell = Cell()
        self.setItemPrototype(self.prototype_cell)
        self.rowcount = 24
        self.colcount = 10
        self.init_grid()

        #self.connect(self, SIGNAL("itemChanged(QTableWidgetItem *)"), self.somethingChanged)
    
    def somethingChanged(self, item):
        print item
    
    def init_grid(self):
        self.setRowCount(0)
        self.setColumnCount(0)
        self.setRowCount(self.rowcount)   
        self.setColumnCount(self.colcount)
        self.setCurrentCell(0,0)
        self.setSpan(0,0,2,2)
