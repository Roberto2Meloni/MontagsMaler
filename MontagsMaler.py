# import public
from random import choice
import sys
from flask import Flask, request, url_for, render_template
from OpenSSL import SSL
import os
import threading


from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAbstractItemView
from PyQt5.uic import loadUi


# import privat
import debugFunction
import helperFunctionGame

# Variabel
swFirmware = "1.0.1"
localHost = "127.0.0.1"
serverIP = "0.0.0.0"
wlanSSID = "not found"
debugFileName = "MontagsMaler.py"
context = SSL.Context(SSL.TLSv1_2_METHOD)
app = Flask(__name__)
new_environ = os.environ.copy()
folderName = "MontagsMaler"
pathTemp = R"${TEMP}/" + folderName
pathTempNew = os.path.expandvars(pathTemp)
qrCodeFile = "webServerQR.png"
varClass = "no Class"



helperFunctionGame.appBootFunction(swFirmware)
# muss hier das debuging erstellen, ansonsten passiert das:
# [2020-12-21 21:23:52.017477]   [127.0.0.1]   [helperFunctionGame.py]   [no Class]   [ssidFinder]   [/// Log: START Function [ssidFinder] ]
# [2020-12-21 21:23:52.017477]   [127.0.0.1]   [helperFunctionGame.py]   [no Class]   [ssidFinder]   [+++ Try: splitt ssid]
# [2020-12-21 21:23:52.017477]   [127.0.0.1]   [helperFunctionGame.py]   [no Class]   [ssidFinder]   [/// Log: return SSID 3Unbekannt]
# [2020-12-21 21:23:52.017477]   [127.0.0.1]   [helperFunctionGame.py]   [no Class]   [ssidFinder]   [/// Log: END Function [ssidFinder]]
# [2020-12-21 21:23:52.017477]   [----------]   [----------]   [----------]   [----------]   [----------]
# [2020-12-21 21:23:52.017477]   [IP - Adress]   [File Name]   [Class Name]   [Function Name]   [Message Typ]
# [2020-12-21 21:23:52.017477]   [127.0.0.1]   [debugFunction.py]   [no Class]   [creatLog]   [/// Log: Continue log file]

# Pages Class


class WelcomePage(QMainWindow):
    # from Template
    varClass = "WelcomePage(QMainWindow)"
    def defaultFunction(self):
        # CLASS INIT
        # from Template
        varFunction = "defaultFunction"
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log:")

        # ERROR
        # from Template if tool is going down
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "!!! Error: ")

        # TRY
        # from Template if tool is going try
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "+++ Try: ")

        # EXCEPT
        # from Template if tool is going except
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "--- Except: ")

        # PRESS BUTTON
        # from Template if tool is going press Button
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "~~~ Press Button: ")

        # WHILE
        # from Template if tool is going while
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "1/2 WHILE: ")

        # FOR
        # from Template if tool is going for
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "1-2 FOR: ")

    def __init__(self):
        # CLASS INIT
        # from Template
        varFunction = "__init__"
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: Start Init Gui")
        super(WelcomePage, self).__init__()
        uic.loadUi("PyQT/01WelcomePage.ui", self)
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: Loading Gui success")

        # all Button
        self.btn_Start.clicked.connect(self.gotoTutPage)

        # Background Image

        #self.label.setStyleSheet("border: 4px solid")
        self.label.setPixmap(QtGui.QPixmap("PyQT/Image/background.jpeg"))

        #self.MainWindow.setPixmap("background.jpeg")
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: End Init Gui")

        #self.mLayout.setStyleSheet(„ background-image: url(backgound.png);“)
        #stylesheet = """
        #    MainWindow {
        #        background-image: url("PyQT/background.jpeg");
        #        background-repeat: no-repeat;
        #        background-position: center;
        #    }
        #
#





    def gotoTutPage(self):
        varFunction = "gotoTutPage"
        myPages.setCurrentIndex(myPages.currentIndex()+1)
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "~~~ Press Button: [Start]")


class TutorialPage(QWidget):
    varClass = "TutorialPage(QWidget)"

    def __init__(self):
        varFunction = "__init__"
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: Start Init Gui")

        super(TutorialPage, self).__init__()
        loadUi("PyQT/02TutorialPage.ui", self)
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: Loading Gui success")

        # all Button to push
        self.btn_Zurueck.clicked.connect(self.gotoWelPage)
        self.btn_Beenden.clicked.connect(self.close)
        self.btn_Weiter.clicked.connect(self.gotoLobPage)

        # QR Code Image
        self.qrCode.setPixmap(QtGui.QPixmap(pathTempNew + "/" + qrCodeFile))

        # output the ssid
        onlySSID = helperFunctionGame.ssidFinder()
        string = "1. Verbinde dich mit dem WLAN [" + onlySSID + "]\n\n2. QR-Code Scannen\n\n3. Erstelle dein Benutzer\n\n4. Schliese den Browser nich!"
        self.label_tut.setText(string)


        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: End Init Gui")

    def gotoWelPage(self):
        varFunction = "gotoWelPage"
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "~~~ Press Button: [Zurück]")
        myPages.setCurrentIndex(myPages.currentIndex() - 1)

    def close(self):
        varFunction = "close"
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "~~~ Press Button: [Beenden]")
        helperFunctionGame.killProgramm("TutorialPage")

    def gotoLobPage(self):
        varFunction = "gotoLobPage"
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction,"~~~ Press Button: [Weiter]")
        myPages.setCurrentIndex(myPages.currentIndex() +1)

class LobbyPage(QWidget):
    varClass = "LobbyPage(QWidget)"

    def __init__(self):
        varFunction = "__init__"
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: Start Init Gui")
        super(LobbyPage, self).__init__()
        loadUi("PyQT/03LobbyPage.ui", self)
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: Loading Gui success")

        # all Button to push
        self.btn_Zurueck.clicked.connect(self.gotoTutPage)
        self.btn_Update.clicked.connect(self.update)
        self.btn_Weiter.clicked.connect(self.gotoTeamPage)

        # QR Code Image
        self.qrCode.setPixmap(QtGui.QPixmap(pathTempNew + "/" + qrCodeFile))

        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: End Init Gui")

    def gotoTutPage(self):
        varFunction = "gotoTutPage"
        myPages.setCurrentIndex(myPages.currentIndex() - 1)
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "~~~ Press Button: [Zurueck]")

    def update(self):
        varFunction = "update"
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "~~~ Press Button: [Aktualisieren]")
        try:
            userListSQL = helperFunctionGame.lobbyUserShow()
            zSpieler = len(userListSQL)
            #self.playerView.setObjectName(_fromUtf8("listView"))

            model = QtGui.QStandardItemModel()
            self.playerView.setModel(model)
            self.playerView.setEditTriggers(QAbstractItemView.NoEditTriggers)

            for i in userListSQL:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)

            self.verbSpieler.setText("Verbundene Spieler: " + str(zSpieler))

            #self.verbSpieler.setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents)
        except Exception as error:
            print(str(error))



        #self.playerView

    def gotoTeamPage(self):
        varFunction = "gotoTeamPage"
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "~~~ Press Button: [Aktualisieren]")
        myPages.setCurrentIndex(myPages.currentIndex() +1)


class TeamSplitPage(QWidget):
    varClass = "TeamSplitPage"

    def __init__(self):
        varFunction = "__init__"
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: Start Init Gui")

        super(TeamSplitPage, self).__init__()
        loadUi("PyQT/04TeamSplitPage.ui", self)
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: Loading Gui success")

        # all button
        self.btn_Zurueck.clicked.connect(self.gotoLobbyPage)
        self.btn_TeamErstellen.clicked.connect(self.berechneTeam)
        self.btn_Weiter.clicked.connect(self.gotoPlayPage)

    def berechneTeam(self):
        varFunction = "berechneTeam"
        debugFunction.debug(localHost, debugFileName, self.varClass, varFunction, "/// Log: Start Function")

        userListCompleat = helperFunctionGame.lobbyTeamCreaterCompleat()
        userListID = helperFunctionGame.lobbyTeamCreaterID()

        teamBlau = []
        teamRot = []

        teamBlauNew = []
        teamRotNew = []

        lenPeople = len(userListID)
        print("es gibt " + str(lenPeople) + " Mitspieler")

        if lenPeople % 2 == 0:
            print("Die anzahl spieler ist gerade")

            while len(userListID):
                playerBlau = choice(userListID)
                teamBlau.append(playerBlau)
                # user in sql Team eintragen
                helperFunctionGame.addUsert2Team(str(playerBlau), "Blau")
                userListID.remove(playerBlau)

                playerRot = choice(userListID)
                teamRot.append(playerRot)
                helperFunctionGame.addUsert2Team(str(playerRot), "Rot")
                userListID.remove(playerRot)

        else:
            print("Die anzahl Lobby ist ungerade!!!")

            while len(userListID) != 1:
                playerBlau = choice(userListID)
                teamBlau.append(playerBlau)
                userListID.remove(playerBlau)

                playerB = choice(userListID)
                teamRot.append(playerB)
                userListID.remove(playerB)

            # add last user in Team Blue
            playerBlau = choice(userListID)
            teamBlau.append(playerBlau)
            userListID.remove(playerBlau)

        # ID auf Benuztername auflösen von Team A
        while len(teamBlau):
            playerID = choice(teamBlau)
            foo = int(playerID)
            playerName = userListCompleat[foo]
            teamBlauNew.append(playerName)
            teamBlau.remove(playerID)

        # ID auf Benuztername auflösen von Team B
        while len(teamRot):
            playerID = choice(teamRot)
            foo = int(playerID)
            playerName = userListCompleat[foo]
            teamRotNew.append(playerName)
            teamRot.remove(playerID)

        modelBlue = QtGui.QStandardItemModel()
        modelRed = QtGui.QStandardItemModel()

        print("model ok")
        self.list_blue.setModel(modelBlue)
        self.list_red.setModel(modelRed)

        for i in teamRotNew:
            item = QtGui.QStandardItem(i)
            modelRed.appendRow(item)
        print("finish red Team")

        for i in teamBlauNew:
            item = QtGui.QStandardItem(i)
            modelBlue.appendRow(item)
        print("finish Blue Team")


        zTeamBlue = str(len(teamBlauNew))
        zTeamRed = str(len(teamRotNew))


        self.label_blue.setText("Team Blau: " + zTeamBlue)
        self.label_red.setText("Team Rot: " + zTeamRed)

        # don't overwrite tabel
        self.list_blue.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_red.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def gotoLobbyPage(self):
        myPages.setCurrentIndex(myPages.currentIndex() - 1)

    def gotoPlayPage(self):
        pass


# API Web Flask
@app.route("/")
def index():
    return render_template("index.html", webServer=serverIP)


@app.route("/loginUser")
def hallo():
    return render_template("loginUser.html", webServer=serverIP)


@app.route("/creatUserInWeb", methods=["POST", "GET"])
def creatUserInWeb():
    name = ""
    #

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        remotIP = request.environ['REMOTE_ADDR']
        print("der Name von Web lautet: " + name)
        print("Das pw lautet: " + password)
        helperFunctionGame.lobbyUserCreater(name, remotIP, password)
    else:
        name = request.args.get("name")
    return render_template("creatUserInWeb.html", newUserName=name, webServer=serverIP)


def startWebServer():
    # from Template
    varFunction = "startWebServer"
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: RUN Webserver on Port 1818!")
    app.run(host=serverIP, ssl_context='adhoc', port=1818, debug=False)


# Start Tool
if __name__ == "__main__":
    # from Template
    varFunction = "__main__"
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: START function")

    guiApp = QtWidgets.QApplication(sys.argv)
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: Creat App")
    myPages = QtWidgets.QStackedWidget()
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: Creat Stacked Widget")

    # all Pages
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: Creat Page shurtCut")
    welcomePage = WelcomePage()
    tutorialPage = TutorialPage()
    lobbyPage = LobbyPage()
    teamSplitPage = TeamSplitPage()

    # add Pages to StackeWidget
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: add Widgets to Stacked Widget")
    myPages.addWidget(welcomePage)
    myPages.addWidget(tutorialPage)
    myPages.addWidget(lobbyPage)
    myPages.addWidget(teamSplitPage)



    # TRY
    # from Template if tool is going try
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "+++ Try: ONE")
    try:
        serverIP = helperFunctionGame.myIPFinder()
        if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
            webServerProcess = threading.Thread(target=startWebServer, daemon=True).start()
        helperFunctionGame.testCreatNewUser()
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: finish creat test users!")
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: show Welcome Page!")
        myPages.show()
    except Exception as e:
        # from Template if tool is going except
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "--- Except: ONE")
        # from Template if tool is going down
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "!!! Error: " + str(e))
        print(str(e))
    sys.exit(guiApp.exec_())
    # start webserver and gui
    # verifai Netzwork
    # start sqlite Database
    # clear the rule for this Game
    # clear all old Date in temp folder
    # what do the user?
    # import clock
    # send the command for the User
    # show in gui how is now on goin to paint
    # faild the user?
    # creat Date for Question to paint
    # foting for enemi team


# Templates
class Default0():

    # from Template
    varClass = "Default0()"


    def defaultFunction(self):
        # CLASS INIT
        # from Template
        varFunction = "defaultFunction"
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log:")

        # ERROR
        # from Template if tool is going down
        #debugFunction.debug(localHost, debugFileName, varClass, varFunction, "!!! Error: ")

        # TRY
        # from Template if tool is going try
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "+++ Try: ")

        # EXCEPT
        # from Template if tool is going except
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "--- Except: ")

        # PRESS BUTTON
        # from Template if tool is going press Button
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "~~~ Press Button: ")

        # WHILE
        # from Template if tool is going while
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "1/2 WHILE: ")

        # FOR
        # from Template if tool is going for
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "1-2 FOR: ")

        # API Web Flask
        # from Template if tool is going except
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "--- Except: ")

        # FOR
        # from Template if tool is going for
        # debugFunction.debug(localHost, debugFileName, varClass, varFunction, "1-2 FOR: ")

    pass
        #@app.route("/")
        #def index():
        #    return render_template("index.html", webServer=serverIP)