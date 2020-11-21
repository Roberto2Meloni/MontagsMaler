# import public
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Line
from kivy.uix.widget import Widget
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
import startHelper
import debugFunticon


# Variabel
swFirmware = "1.0.1"
localHost = "127.0.0.1"
wlanSSID = "not found"


# Teams

# Database

class Painter(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]

class PainterPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class WelcomePage(Screen):
    pass
    # sitzung erstellen (ein bischen sicherheit)
    # generiere random sizungsnummer
    # generiere random hash vor QR Code
    #

class LobbyPage(Screen):
    pass

class TutorialPage(Screen):
    pass


# Screenmanager
screenManager = Builder.load_file("montagsmaler.kv")

class MontagsMaler(App):
    wlanSSID = startHelper.ssidFinder()
    foo = ("Zeile 51. Verbinde dich mit dem WLAN: " + wlanSSID)
    wlanText = StringProperty()
    print(foo)

    #def set_text(self):
    #    #get reverence to Label
    #    wlanText =
    #    print(wlanText)
    #    # get a referent
    #    wlanLabel = self.root.ids.wlanLabel
    #    wlanLabel.text = wlanText


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
    # clear the rule for this Game
    # clear all old Date in temp folder
    # what do the user?
    # import clock
    # send the command for the User
    # show in gui how is now on goin to paint
    # faild the user?
    # creat Teams
    # creat Date for Question to paint
    # foting for enemi team