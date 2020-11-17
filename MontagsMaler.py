# import public
import kivy
from kivy.app import App
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
swFirmware = "1.0"
localHost = "127.0.0.1"

# Teams

# Database



# Kivy Class
indow.size = (1000, 700)
Builder.load_string("""
<StartPage>



<WelcomePage>



""")

class StartPage(Screen):
    pass

class WelcomePage(Screen):
    pass


ms = ScreenManager()
ms.add_widget(StartPage(name="StartPage"))
ms.add_widget(WelcomePage(name="WelcomePage"))

class StartApp(App):
    def build(self):
        return ms



# Start Tool
if __name__ == "__main__":
    try:
        instanzBoot1 = startHelper.BootClass()
        instanzBoot1.creatFolder()
        debugFunticon.creatLog("startHelper", swFirmware)
        StartApp().run()
    except Exception as e:
        debugFunticon.debug(localHost, "Start Tool", str(e))
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