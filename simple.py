import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui     import QIcon


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 250)
    w.move(100,100)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
