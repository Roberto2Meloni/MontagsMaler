# import public
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# import privat
import startHelper
import debugFunticon


# Variabel
swFirmware = "1.0.1"
localHost = "127.0.0.1"
wlanSSID = "not found"


# Teams

# Database


class WindowManager(ScreenManager):
    pass

class WelcomePage(Screen):
    def creatLobby(self):
        pass
        # sitzung erstellen (ein bischen sicherheit)
        # generiere random sizungsnummer
        # generiere random hash vor QR Code
        #

class LobbyPage(Screen):
    pass


# Screenmanager
screenManager = Builder.load_file("montagsmaler.kv")

class MontagsMaler(App):
    def build(self):
        return screenManager

# Start Tool
if __name__ == "__main__":
    try:
        startHelper.creatFolder()
        debugFunticon.creatLog("startHelper", swFirmware)
        MontagsMaler().run()
    except Exception as e:
        debugFunticon.debug(localHost, "Start Tool", str(e))
        print(str(e))
    # start webserver
    # verifai Netzwork
    # create QR Code
    # start Welcom Gui
    # clear the rule for this Game
    # clear all old Date in temp folder
    # creat Log files
    # creat temp folder
    # what do the user?
    # import clock
    # send the command for the User
    # show in gui how is now on goin to paint
    # faild the user?
    # creat Teams
    # creat Date for Question to paint
    # print the SSID form Netzwork
    # foting for enemi team