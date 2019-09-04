from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
import sys

def click_on_you():
    print(w.lineEdit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = loadUi('first_example.ui')
    w.pushButton.clicked.connect(click_on_you)
    w.show()
    app.exec()