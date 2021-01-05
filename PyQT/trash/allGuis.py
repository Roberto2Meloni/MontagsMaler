from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.uic import loadUi
import sys


class WelcomePage(object):

    def __init__(self):
        super(WelcomePage, self).__init__()
        print("GUI init ...")
        try:
            uic.loadUi("Welcome.ui", self)
            uic.loadUi(self.get_resource("ui/board.ui"), self)
            print("finisch load welcome")
        except Exception as error:
            print("fail to load the ui!!!")
            print(str(error))
        #button.clicked.connect(self.gedrueckt)


class TutorialPage(object):

    def __init__(self):
        super(TutorialPage, self).__init__()
        loadUi("Tutorial.ui", self)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    print("Creat app")
    myPages = QtWidgets.QStackedWidget()
    print("1")

    welcomePage = WelcomePage()
    print("2")
    tutorialPage = TutorialPage()

    myPages.addWidget()
    print("3")
    myPages.addWidget(welcomePage)
    myPages.addWidget(tutorialPage)

    myPages.show()
    sys.exit(app.exec_())




    #MainWindow = QtWidgets.QMainWindow()
    #ui = WelcomePage()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
