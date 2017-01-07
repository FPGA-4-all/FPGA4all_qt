import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon
class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #Exit action code
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)

        #status Bar
        self.statusBar()

        #tool Bar
        self.toolBar = self.addToolBar('Exit')
        self.toolBar.addAction(exitAction)

        #Menu Bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        #window geometry, title and show
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('statusBar')
        self.show()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
