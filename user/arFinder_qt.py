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
from PyQt5.QtWidgets import *
# Why would you import everything? Doesn't that seem a little braggerty

class Form(QWidget):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.submitButton = QPushButton("&amp;Submit")

        buttonL1 = QVBoxLayout()
        buttonL1.addWidget(nameLabel)
        buttonL1.addWidget(self.nameLine)
        buttonL1.addWidget(self.submitButton)

        self.submitButton.clicked.connect(self.submitContact)

        mainLayout = QGridLayout()
        mainLayout.addLayout(buttonL1,0,1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Hello Qt")

    def submitContact(self):
        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Emty Field",
                            "Please enter a name and address.")
            return
        else:
            QMessageBox.information(self, "Success!",
                                    "Hello %s!" % name)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
