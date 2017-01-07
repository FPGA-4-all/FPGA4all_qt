import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui     import QIcon, QFont
from PyQt5.QtCore    import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #Icon and Logo code
        self.setGeometry(300, 300, 300 ,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('logo.png'))

        #button code
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Quit', self)
        btn.setToolTip('This is the <b>Quit</b> button')
        btn.resize(btn.sizeHint())
        btn.move(10,10)

        btn.clicked.connect(QCoreApplication.instance().quit)

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
        "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
