# import public
from kivy.lang import Builder
from random import choice
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import Screen
from kivy.graphics import Line
from kivy.uix.widget import Widget
import sys
from kivy.uix.gridlayout import GridLayout
from flask import Flask, request, url_for, render_template
from OpenSSL import SSL
import os
import threading
from kivymd.uix.list import OneLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
# from kivy.uix.listview import ListItemButton
import kivy
from kivy.properties import StringProperty
import webbrowser
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

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


# Variabeln
screen_helper = """
ScreenManager:
    WelcomePage:
    TutorialPage:
    LobbyPage:
    TeamPage:
    PainterPage:

<WelcomePage>:
    name: "WelcomePageKV"
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "background.jpeg"

    BoxLayout:
        Label:
            name:"platzhalter"
            size_hint_x: 0.01
            size_hint_y: 0.15
        MDRaisedButton:
            text: "START"
            font_size:40
            size_hint_x: 0.9
            size_hint_y: 0.15
            on_release: 
                root.pressStart()
                root.manager.current = "TutorialPageKV"
                root.manager.transition.direction = "left"
        Label:
            name:"platzhalter"
            size_hint_x: 0.01
            size_hint_y: 0.15


<TutorialPage>:
    name:"TutorialPageKV"
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "background.jpeg"
    GridLayout:
        cols:1
        MDToolbar:
            title: "Anleitung"
    BoxLayout:
        cols: 2
        spacing:10
        padding: 40
        Label:
            text: root.hinweiss
            text_color: "red"
            pos: self.pos
            font_size:30
        Label:
            name: "QR-Code"
            Image:
                center: self.parent.center
                size_hint: 400,400
                source: root.imgSource
    BoxLayout:
        Label:
            name:"platzhalter"
            size_hint_x: 0.01
            size_hint_y: 0.15
        MDRaisedButton:
            text: "Beenden"
            font_size:40 
            size_hint_x: .5
            size_hint_y: 0.15
            on_release: root.pressBeenden()
        Label:
            name:"platzhalter"
            size_hint_x: 0.01
            size_hint_y: 0.15
        MDRaisedButton:
            text: "Zurück"
            font_size:40 
            size_hint_x: .5
            size_hint_y: 0.15
            on_release:
                root.manager.current = "WelcomePageKV"
                root.manager.transition.direction = "right"
                root.pressBack()
        Label:
            name:"platzhalter"
            size_hint_x: 0.01
            size_hint_y: 0.15
        MDRaisedButton:
            text: "Verstanden"
            font_size:40 
            size_hint_x: .5
            size_hint_y: 0.15
            on_release: 
                root.manager.current = "LobbyPageKV"
                root.manager.transition.direction = "left"
                root.pressVerstanden()
        Label:
            name:"platzhalter"
            size_hint_x: 0.01
            size_hint_y: 0.15
            pos_hint_y: 0.01

<LobbyPage>:
    name: "LobbyPageKV"
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "background.jpeg"
    GridLayout:
        cols: 1
        MDToolbar:
            title: "Lobby"
        FloatLayout:
            Label:
                text: "Verbundene Mitspieler"
                font_size: 40
                size_hint: 0.3, 0.25
                pos_hint: {"x":0,"y":0.7}
            Label:
                name: "QR-Code"
                size_hint: 0.4, 0.25
                pos_hint: {"x":0.65,"y":0.7}
                Image:
                    center: self.parent.center
                    size_hint: 400,400
                    source: root.imgSource
        ScrollView:
            pos_hint: {"x":0, "y":0.6}
            MDList:
                cols: 4
                text_color: 245/255, 1, 250/255, 1
                id: userListViewKV
                
        BoxLayout:
            Label:
                name:"platzhalter"
                size_hint_x: 0.01
                size_hint_y: 0.5
            MDRaisedButton:
                text: "Beenden"
                font_size:40 
                size_hint_x: .5
                size_hint_y: 0.5
                on_release: root.pressBeenden()
            Label:
                name:"platzhalter"
                size_hint_x: 0.01
                size_hint_y: 0.5
            MDRaisedButton:
                text: "aktuallisieren"
                font_size:40 
                size_hint_x: .5
                size_hint_y: 0.5
                on_release:
                    root.pressUpdate()
            Label:
                name:"platzhalter"
                size_hint_x: 0.01
                size_hint_y: 0.5
            MDRaisedButton:
                text: "weiter!"
                font_size:40 
                size_hint_x: .5
                size_hint_y: 0.5
                on_release: 
                    root.manager.current = "TeamPageKV"
                    root.manager.transition.direction = "left"
            Label:
                name:"platzhalter"
                size_hint_x: 0.01
                size_hint_y: 0.5
    
<TeamPage>:
    name: "TeamPageKV"        
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "background.jpeg"
    GridLayout:
        cols: 1
        MDToolbar:
            title: "Team Aufteilung"
    GridLayout:
        cols:2
        Label:
            text: "Team Blau"                
        Label:
            text: "Team Rot"
        ScrollView:
            MDList:
                id: userBlueTeam
        ScrollView:
            MDList:
                id: userRedTeam
    BoxLayout:
        cols: 6
        Label:
            name:"platzhalter"
            size_hint_x: 0.01
            size_hint_y: 0.17
        MDRaisedButton:
            text: "Zurück"
            font_size:40 
            size_hint_x: .5
            size_hint_y: 0.17
            on_release:
                root.manager.current = "LobbyPageKV"
                root.manager.transition.direction = "right"
        Label:
            name:"platzhalter"
            size_hint_x: 0.01
            size_hint_y: 0.17
        MDRaisedButton:
            text: "Team erstellen"
            font_size:40 
            size_hint_x: .5
            size_hint_y: 0.17
            on_release:
                on_release: root.berechneTeam()
        Label:
            name:"platzhalter"
            size_hint_x: 0.01
            size_hint_y: 0.17
        MDRaisedButton:
            text: "weiter"
            font_size:40 
            size_hint_x: .5
            size_hint_y: 0.17
            on_release: 
                root.manager.current = "TeamPageKV"
                root.manager.transition.direction = "left"
        Label:
            name:"platzhalter"
            size_hint_x: 0.01
            size_hint_y: 0.17
                
                
    

<PainterPage>:
    name: "PainterPageKV"

"""

helperFunctionGame.appBootFunction(swFirmware)
# muss hier das debuging erstellen, ansonsten passiert das:
# [2020-12-21 21:23:52.017477]   [127.0.0.1]   [helperFunctionGame.py]   [no Class]   [ssidFinder]   [/// Log: START Function [ssidFinder] ]
# [2020-12-21 21:23:52.017477]   [127.0.0.1]   [helperFunctionGame.py]   [no Class]   [ssidFinder]   [+++ Try: splitt ssid]
# [2020-12-21 21:23:52.017477]   [127.0.0.1]   [helperFunctionGame.py]   [no Class]   [ssidFinder]   [/// Log: return SSID 3Unbekannt]
# [2020-12-21 21:23:52.017477]   [127.0.0.1]   [helperFunctionGame.py]   [no Class]   [ssidFinder]   [/// Log: END Function [ssidFinder]]
# [2020-12-21 21:23:52.017477]   [----------]   [----------]   [----------]   [----------]   [----------]
# [2020-12-21 21:23:52.017477]   [IP - Adress]   [File Name]   [Class Name]   [Function Name]   [Message Typ]
# [2020-12-21 21:23:52.017477]   [127.0.0.1]   [debugFunction.py]   [no Class]   [creatLog]   [/// Log: Continue log file]

# Classes
class Painter(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]


class PainterPage(Screen):
    pass

class WelcomePage(Screen):

    def pressStart(self):
        debugFunction.debug(localHost, debugFileName, "WelcomePage(Screen)", "pressStart", "~~~ Press Button: [Start]")

class LobbyPage(Screen):
    imgSource = (pathTempNew + "/" + qrCodeFile)

    def pressUpdate(self):
        debugFunction.debug(localHost, debugFileName, "LobbyPage(Screen)", "pressUpdate", "~~~ Press Button: Update")
        userListSQL = helperFunctionGame.lobbyUserShow()
        self.ids.userListViewKV.clear_widgets()

        debugFunction.debug(localHost, debugFileName, "LobbyPage(Screen)", "pressUpdate", "1-2 FOR: userListSQL")
        for i in userListSQL:
            self.ids.userListViewKV.add_widget(OneLineListItem(text=i))


    def pressBeenden(self):
        debugFunction.debug(localHost, debugFileName, "LobbyPage(Screen)", "pressBeenden", "~~~ Press Button: Beenden")
        helperFunctionGame.killProgramm("MontagsMaler.py/LobbyPage/pressBeenden")

class TeamPage(Screen):

    def defaultFunction(self):
        # CLASS INIT
        # from Template
        debugFunction.debug(localHost, debugFileName, "TeamPage(Screen)", "defaultFunction", "/// Log:")

        # ERROR
        # from Template if tool is going down
        # debugFunction.debug(localHost, debugFileName, "TeamPage(Screen)", "defaultFunction", "!!! Error: ")

        # TRY
        # from Template if tool is going try
        # debugFunction.debug(localHost, debugFileName, "TeamPage(Screen)", "defaultFunction", "+++ Try: ")

        # EXCEPT
        # from Template if tool is going except
        # debugFunction.debug(localHost, debugFileName, "TeamPage(Screen)", "defaultFunction", "--- Except: ")

        # PRESS BUTTON
        # from Template if tool is going press Button
        # debugFunction.debug(localHost, debugFileName, "TeamPage(Screen)", "defaultFunction", "~~~ Press Button: ")

        # WHILE
        # from Template if tool is going while
        # debugFunction.debug(localHost, debugFileName, "TeamPage(Screen)", "defaultFunction", "1/2 WHILE: ")

        # FOR
        # from Template if tool is going for
        # debugFunction.debug(localHost, debugFileName, "TeamPage(Screen)", "defaultFunction", "1-2 FOR: ")
    def berechneTeam(self):
        debugFunction.debug(localHost, debugFileName, "TeamPage(Screen)", "berechneTeam", "/// Log: Start Function")

        userListCompleat = helperFunctionGame.lobbyTeamCreaterCompleat()
        userListID = helperFunctionGame.lobbyTeamCreaterID()

        teamBlau = []
        teamRot = []

        teamBlauNew = []
        teamRotNew = []

        lenPeople =len(userListID)
        print("es gibt " +str(lenPeople) + " Mitspieler")

        if lenPeople%2==0:
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

            while len(userListID) !=1:
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


        # creat MD List for Blue Team
        self.ids.userBlueTeam.clear_widgets()
        self.ids.userRedTeam.clear_widgets()

        for i in teamBlauNew:
            self.ids.userBlueTeam.add_widget(OneLineListItem(text=i))

        for i in teamRotNew:
            self.ids.userRedTeam.add_widget(OneLineListItem(text=i))


        # mit ID aus sql eintrag erstellen für die Team zuweisung


class TutorialPage(Screen):
    onlySSID = helperFunctionGame.ssidFinder()

    hinweiss = "1. Verbinde dich mit dem WLAN [" + onlySSID + "]\n\n2. QR-Code Scannen\n\n3. Erstelle dein Benutzer\n\n4. Schliese den Browser nich!"
    imgSource = (pathTempNew + "/" + qrCodeFile)

    def pressBeenden(self):
        debugFunction.debug(localHost, debugFileName, "TutorailPage", "pressBeenden", "Press on [Beenden] Button || dont chage debug")
        helperFunctionGame.killProgramm("MontagsMaler.py/TutorialPage/pressBeenden")

    def pressBack(self):
        debugFunction.debug(localHost, debugFileName, "TutorailPage", "pressBack", "Press on [Zurueck] Button|| dont chage debug")

    def pressVerstanden(self):
        debugFunction.debug(localHost, debugFileName, "TutorailPage", "pressVerstanden", "Press on [Verstanden] Button|| dont chage debug")


# Screenmanager
sm = ScreenManager()
sm.add_widget(WelcomePage(name="WelcomePageKV"))
sm.add_widget(TutorialPage(name="TutorialPageKV"))
sm.add_widget(LobbyPage(name="LobbyPageKV"))
sm.add_widget(PainterPage(name="PainterPageKV"))


class MontagsMaler(MDApp):
    # from Template
    varClass = "MontagsMaler(MDApp)"
    def build(self):
        varFunction = "build"
        screen = Builder.load_string(screen_helper)
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: RETURN ScreenManager")
        return screen


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
    print("changes")
    # from Template
    varFunction = "__main__"
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: START function")
    # TRY
    # from Template if tool is going try
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "+++ Try: ONE")
    try:
        serverIP = helperFunctionGame.myIPFinder()
        if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
            webServerProcess = threading.Thread(target=startWebServer, daemon=True).start()
        helperFunctionGame.testCreatNewUser()
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: finish creat test users!")
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: RUN MontasMaler!")
        MontagsMaler().run()
    except Exception as e:
        # from Template if tool is going except
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "--- Except: ONE")
        # from Template if tool is going down
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "!!! Error: " + str(e))
        print(str(e))
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