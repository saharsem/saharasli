from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()
    b = QPushButton("click on me", w)
    app.exec()