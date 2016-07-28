#!/usr/bin/python

'''
 GUI for arFinder. Starting small and then moving into the description
 mentioned in the main file (arFinder.py).
 Things to do everywhere:
    implement unit testing
    logs
    errors and exceptions
    robustness
    follow PEP 8 guidelines
'''

import sys
from backend.arFinder import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# Why would you import everything? Doesn't that seem a little braggerty

class Table(#QTableWidget,
            QMainWindow):

    def __init__(self, *args, parent=None):
        QMainWindow.__init__(self)
#        QTableWidget.__init__(self, *args)
        self.data = []
        self.initUI()
#        self.set_data()
#        self.resizeColumnsToContents()
#        self.resizeRowsToContents()
        # Table

    def set_data(self, *args):
        if args:
            self.data = cmds(args)
        else:
            self.data = cmds(('-all', 'electrons'))

        for m, n in enumerate(self.data):
            newitem = QTableWidgetItem(n.__str__())
            self.setItem(1,m, newitem)

    def initUI(self):

        self.statusBar().showMessage("ready")
        self.setGeometry(300, 300, 250, 150)

        self.setWindowTitle("Statusbar")


    def refresh(self):
        return

    def open_screen(self):
        return

#    def get_items(self, search_term):
#        arFinder.cmds(lookup=search_term)

    def cellClick(self, row, col):
        print("I am clicked")

def main(args):
    app = QApplication(args)
    table = Table(10, 5)
    table.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)
