import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_MonitorPow import Ui_MainWindow

class MainWin:
    def __init__(self):
        self.mainWin = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainWin)

        self.ui.stackedWidget.setCurrentWidget(self.ui.dataP)

        self.ui.dataBtn.clicked.connect(self.showDataP)
        self.ui.mapBtn.clicked.connect(self.showMapP)
        self.ui.pushButton_3.clicked.connect(self.showOptionP)

    def show(self):
        self.mainWin.show()

    def showDataP(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.dataP)

    def showMapP(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.mapP)

    def showOptionP(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.optionP)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWin()
    mainWin.show()
    sys.exit(app.exec_())

