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


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# Why would you import everything? Doesn't that seem a little braggerty

class Articles(QWidget):

    def __init__(self, parent=None):
        super(Articles, self).__init__(parent)

        # Table initialization
        self.article_table = QTableWidget()
        self.article = QTableWidgetItem()

        # set selection mode for contiguous cell
        self.article_table.setSelectionMode(
                QAbstractItemView.ContiguousSelection)


        self.article_table.setWindowTitle("arFinder")
        self.article_table.resize(300,300)
        self.article_table.setRowCount(6)
        self.article_table.setColumnCount(6)

        self.article_table.setSpan(0,1,5,4)

        self.article_table.setItem(0,0,QTableWidgetItem("First Article"))
        self.article_table.setItem(1,0,QTableWidgetItem("Second Article"))
        self.article_table.setItem(2,0,QTableWidgetItem("Third Article"))
        self.article_table.setItem(3,0,QTableWidgetItem("Fourth Article"))
        self.article_table.setItem(4,0,QTableWidgetItem("Fifth Article"))
        self.article_table.setItem(5,0,QTableWidgetItem("Sixth Article"))


        self.article_table.cellClicked.connect(self.cellClick)


    def refresh(self):
        return

    def open_screen(self):
        return

#    def get_items(self, search_term):
#        arFinder.cmds(lookup=search_term)

    def cellClick(self, row, col):
        print("I am clicked")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    screen = Articles()
    screen.show()

    sys.exit(app.exec_())
