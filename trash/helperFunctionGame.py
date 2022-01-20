import os
import subprocess
from datetime import datetime
import sqlite3
import qrcode
import multiprocessing
import sys
import time
from main import pathTempNew
import debugFunction

# Variabel
swFirmware = "helperFunctionGame SW: 1.0"
#pathTemp = R"${TEMP}/MontagsMaler"
#pathTempNew = os.path.expandvars(pathTemp)
now = datetime.now()
dataBase = "DataBase.db"
qrCodeFile = "webServerQR.png"
varClass = "no Class"
localHost = "127.0.0.1"
debugFileName = "helperFunctionGame.py"
people = list()


def checkDataBase():
    #Database
    if os.path.isfile(pathTempNew + "/" + dataBase):
        os.remove(pathTempNew + "/" + dataBase)
    else:
        pass
    sql = """CREATE TABLE IF NOT EXISTS person (id integer Primary Key,name text, password text, ip text, port text, team text, begriff1 text, begriff2 text, begriff3 text)"""

    if os.path.isfile(pathTempNew + "/" + dataBase):
        print("Datebnbank exisiter jetzt")
    else:
        pass
    connection = sqlite3.connect(pathTempNew + "/" + dataBase)
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()
    return sql


sql = "Hallo"
#sql = checkDataBase()


def ssidFinder():
    varFunction = "ssidFinder"
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: START Function [ssidFinder] ")

    try:
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "+++ Try: splitt ssid")
        ssid = subprocess.check_output("netsh wlan show interfaces")
        ssid = ssid.splitlines()
        ssid = str(ssid)
        ssid = ssid.split("SSID")[1]
        ssid = ssid.split(": ")[1]
        ssid = ssid.split("'")[0]
        #print("--------------------")
        #print(ssid)
        #print("--------------------")
        #print(type(ssid))
    except Exception as error:
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "--- Except: cant't find ssid!!!")
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "!!! Error: " +str(error))
        ssid = "not found ssid!!! watch log files"
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, ("/// Log: return SSID " + ssid))
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: END Function [ssidFinder]")
    return ssid

def myIPFinder():
    varFunction = "myIPFinder"
    print("ahhlo ip")
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: START Function [myIPFinder]")

    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "+++ Try: finding WLAN IP")
    try:
        ip = subprocess.check_output("ipconfig")
        ip = ip.splitlines()
        ip = str(ip)
        ip = ip.split("Drahtlos-LAN-Adapter WLAN:")[1]
        ip = ip.split("IPv4-Adresse")[1]
        ip = ip.split(": ")[1]
        ip = ip.split("'")[0]

        # print("--------------------")
        # print(ip)
        # print("--------------------")
    except Exception as error:
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "--- Except: Can't find IP Adress for WLAN!!!")
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, ("!!! Error: " + str(error)))
        debugFunction.debug(localHost, debugFileName, varClass, varFunction, "+++ Try: finding LAN IP")
        try:
            ip = subprocess.check_output("ipconfig")
            ip = ip.splitlines()
            ip = str(ip)
            ip = ip.split("Ethernet-Adapter Ethernet:")[1]
            ip = ip.split("IPv4-Adresse")[1]
            ip = ip.split(": ")[1]
            ip = ip.split("'")[0]

            # print("--------------------")
            # print(ip)
            # print("--------------------")

        except Exception as error:
            debugFunction.debug(localHost, debugFileName, varClass, varFunction, "--- Except: Can't find IP Adress for LAN!!!")
            debugFunction.debug(localHost, debugFileName, varClass, varFunction, ("!!! Error: " + str(error)))
            print("not found ip")
            ip = "not found!!!"
    debugFunction.debug(localHost,debugFileName, varClass, varFunction, ("/// Log: return ip: " + ip))
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: End Function [myIPFinder] ")
    return ip

def killProgramm(fromField):
    varFunction = "killProgramm"
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: START Function [killProgramm] ")
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, ("/// Log:Start killing Programm from: " + fromField))
    sys.exit()

def lobbyUserCreater(varName, varPassword, varIP, varPort):
    # from Template
    varFunction = "lobbyUserCreater"
    conn = sqlite3.connect(pathTempNew + "/" + dataBase)
    curs = conn.cursor()
    curs.execute(sql)

    # print(type(varName))
    # print(varName)
    # print("---------")
    # print(type(varIP))
    # print(varIP)

    conn.execute("INSERT INTO person(name, ip, password, port) VALUES(?,?,?,?)", (varName, varIP,varPassword, varPort))
    curs.close()
    conn.commit()
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: In SQL creat new User: " + varName)

def lobbyUserShow():
    conn = sqlite3.connect(pathTempNew + "/" + dataBase)
    curs = conn.cursor()
    curs.execute(sql)
    userList = []

    curs.execute("SELECT name from 'person'")
    row = curs.fetchone()
    while row is not None:
        name = row[0]
        userList.append(name)
        row = curs.fetchone()

    curs.close()
    conn.commit()
    debugFunction.debug(localHost, debugFileName, "no Class", "lobbyUserShow", ("Update Userlist"))
    return userList

def lobbyTeamCreaterCompleat():
    conn = sqlite3.connect(pathTempNew + "/" + dataBase)
    curs = conn.cursor()
    curs.execute(sql)
    userList = {}

    curs.execute("SELECT id, name from 'person'")
    row = curs.fetchone()
    while row is not None:
        userid = row[0]
        userName = row[1]
        foo = {userid: userName}
        userList.update(foo)
        row = curs.fetchone()


    curs.close()
    conn.commit()
    debugFunction.debug(localHost, debugFileName, "no Class", "lobbyTeamCreater", ("Update Userlist withe ID"))
    return userList

def addUsert2Team(varID, varTeam):
    varIDnew = int(varID)


    conn = sqlite3.connect(pathTempNew + "/" + dataBase)
    curs = conn.cursor()
    curs.execute(sql)

    # add Team name in the SQL
    conn.execute("UPDATE person SET team = ? WHERE id = ?", (varTeam, varIDnew))

    conn.commit()
    curs.close()
    debugFunction.debug(localHost, debugFileName, "no Class", "addUsert2Team", ("Add ID: " + varID + " to Team " + varTeam))


def lobbyTeamCreaterID():
    conn = sqlite3.connect(pathTempNew + "/" + dataBase)
    curs = conn.cursor()
    curs.execute(sql)
    userListID = []

    curs.execute("SELECT id from 'person'")
    row = curs.fetchone()
    while row is not None:
        userid = str(row[0])
        userListID.append(userid)
        row = curs.fetchone()


    curs.close()
    conn.commit()
    debugFunction.debug(localHost, debugFileName, "no Class", "lobbyTeamCreater", ("Update Userlist withe ID:"))
    return userListID

def getUserInfos4SplitTeam(varID):
    # get IP and port 4 communication to User to tell him wich team he is
    varIDNew = varID
    varIP = ""
    varPort = ""
    varTeam = ""

    debugFunction.debug(localHost, debugFileName, "no Class", "getUserInfos4SplitTeam",("Get infos (IP/Port/Team) from ID ", varIDNew))

    
    conn = sqlite3.connect(pathTempNew + "/" + dataBase)
    curs = conn.cursor()
    curs.execute(sql)

    # from id get IP/Port/Team and then return
    curs.execute("SELECT id, name from 'person'")
    row = curs.fetchone()
    # now get to the info from sql

    conn.commit()
    curs.close()
    debugFunction.debug(localHost, debugFileName, "no Class", "getUserInfos4SplitTeam", ("IP / Port = ", varIP, "/", varPort))
    return varIP, varPort, varTeam

def creatQR():
    # CLASS INIT
    # from Template
    varFunction = "creatQR"
    serverIP = myIPFinder()
    input_data = "https://"+serverIP+":1818/"

    if os.path.isfile(pathTempNew + "/" + qrCodeFile):
        os.remove(pathTempNew + "/" + qrCodeFile)
    else:
        pass

    # Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)

    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save((pathTempNew + "/" + qrCodeFile))
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: QR-Code creat an save in temp Folder")

def appBootFunction(swFirmware):
    # from Template
    varFunction = "appBootFunction"
    sql = checkDataBase()
    #creatFolder()
    #checkDataBase()
    # debugFunction.creatLog("helpderFuntcionGame", swFirmware)
    creatQR()
    debugFunction.debug(localHost, debugFileName, varClass, varFunction, "/// Log: Finish all boot Function")



#lobbyFileCreater()
def testCreatNewUser():
    lobbyUserCreater("Roberto","IEMIE","192.168.1.1","noPort")
    lobbyUserCreater("Fabio","EAE","192.168.1.2","noPort")
    lobbyUserCreater("te","EAE","192.168.1.2","noPort")
    lobbyUserCreater("te","EAE","192.168.1.2","noPort")
    lobbyUserCreater("te","EAE","192.168.1.2","noPort")
    lobbyUserCreater("te","EAE","192.168.1.2","noPort")
    lobbyUserCreater("te","EAE","192.168.1.2","noPort")
    lobbyUserCreater("te","EAE","192.168.1.2","noPort")
    lobbyUserCreater("te","EAE","192.168.1.2","noPort")
    lobbyUserCreater("Fabceio","EAE","192.168.1.2","noPort")
    lobbyUserCreater("ae","EAE","192.168.1.2","noPort")
    lobbyUserCreater("ae","EAE","192.168.1.2","noPort")
    lobbyUserCreater("ae","EAE","192.168.1.2","noPort")
    lobbyUserCreater("ae","EAE","192.168.1.2","noPort")
    lobbyUserCreater("ae","EAE","192.168.1.2","noPort")
    lobbyUserCreater("ae","EAE","192.168.1.2","noPort")
    lobbyUserCreater("ae","EAE","192.168.1.2","noPort")
    lobbyUserCreater("caec","EAE","192.168.1.2","noPort")
    lobbyUserCreater("eaea","EAE","192.168.1.2","noPort")
    lobbyUserCreater("hh","IMIE88","192.168.1.3","noPort")
    lobbyUserCreater("Maria","lmce558","192.168.1.4","noPort")
    lobbyUserCreater("Maria","lmce558","192.168.1.4","noPort")
    lobbyUserCreater("Maria","lmce558","192.168.1.4","noPort")
    lobbyUserCreater("Maria","lmce558","192.168.1.4","noPort")
    lobbyUserCreater("Maria","lmce558","192.168.1.4","noPort")
    lobbyUserCreater("Maria","lmce558","192.168.1.4","noPort")
    lobbyUserCreater("Maria","lmce558","192.168.1.4","noPort")
    lobbyUserCreater("Maria","lmce558","192.168.1.4","noPort")
    lobbyUserCreater("eae","lmce558","192.168.1.4","noPort")
    lobbyUserCreater("hkhhi","lmce558","192.168.1.4","noPort")



# Templates
class Default0():

    # from Template
    varClass = "Default0()"

    # from Template
    # debugFunction.debug(localHost, debugFileName, varClass, "class", "### Log: Class [Default]")

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
    pass
