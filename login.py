from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.uic import loadUi
import sys

def check_login():
    username = w.lineEdit.text()
    password = w.lineEdit_2.text()
    if username == 'admin' and password =='admin':
        message = 'welcome'
    else:
        message = 'get away'
    message_box = QMessageBox()
    message_box.setIcon(QMessageBox.Warning)
    message_box.setText(message)
    message_box.show()
    message_box.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = loadUi('login.ui')
    w.show()
    w.pushButton.clicked.connect(check_login)
    app.exec()