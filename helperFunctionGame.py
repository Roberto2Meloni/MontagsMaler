import os
import sys
import subprocess
from datetime import datetime
import debugFunction
import time

# Variabel
swFirmware = "helperFunctionGame SW: 1.0"
pathTemp = R"${TEMP}/MontagsMaler"
pathTempNew = os.path.expandvars(pathTemp)
now = datetime.now()

allUser = "allUserFile.txt"
teamBlue = "teamBlue.txt"
teammRed = "teamRed.txt"
allQ4Blue = "allQ4Blue.txt"
allQ4Red = "allQ4Red.txt"

# System Start helper
def creatFolder():
    # variabel
    folderName = "MontagsMaler"
    pathTemp = R"${TEMP}/" + folderName
    pathTempNew = os.path.expandvars(pathTemp)
    #updateFile = R"${TEMP}/SIPPhoneManager/Update_File.jpg"
    #updateFileNew = os.path.expandvars(updateFile)

    toolStart = True
    folderCheck = True
    updateCheck = False

    # List, what is to chek
    # print("Dose the folder SIPPhoenManager exist in User Temp Folder?\n"
    #     "Does it hav a update File?\n"
    #    "...\n")

    while toolStart == True:
        # check that the Folder for debuging and update exist!
        # print("[start] toolStart")
        while folderCheck == True:
            # print("[start] folder Check")
            if os.path.exists(pathTempNew):
                # print("[folder] exist")
                folderCheck = False
            else:
                # print("[folder] not exist")
                # print("[folder] creat in Temp")
                os.system(r"md %temp%\MontagsMaler")
            # print("[finish] folder Check")
        while updateCheck == True:
            # print("[start] file Chek")
            if os.path.isfile(updateFileNew):
                #    print("[file] exist")
                #   print("[file] delet form folder")
                os.system(r"del %temp%\MontagsMaler\Update_File.jpg")
                updateCheck = False
            else:
                # print("[file] not exist")
                updateCheck = False
            # print("[finish] file check")
        # print("[finish] tool start")
        toolStart = False

def ssidFinder():
    try:
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
    except:
        ssid = "not found new"
    return ssid

def myIPFinder():
    try:
        ip = subprocess.check_output("ipconfig")
        ip = ip.splitlines()
        ip = str(ip)
        ip = ip.split("Drahtlos-LAN-Adapter WLAN:")[1]
        ip = ip.split("IPv4-Adresse")[1]
        ip = ip.split(": ")[1]
        ip = ip.split("'")[0]

        #print("--------------------")
        #print(ip)
        #print("--------------------")
    except:
        print("not found ip")
        ip = "not found!!!"
    return ip

def delOldFiles():
    # deleat in temp folder all files except the log file
    # QR code
    # all User with id
    if os.path.isfile(pathTempNew + "/" + allUser):
        os.remove(pathTempNew + "/" + allUser)
    else:
        print("The file does not exist")

    # team blue file
    if os.path.isfile(pathTempNew + "/" + teamBlue ):
        os.remove(pathTempNew + "/" + teamBlue )
    else:
        print("The file does not exist")

    # team red file
    if os.path.isfile(pathTempNew + "/" + teammRed ):
        os.remove(pathTempNew + "/" + teammRed )
    else:
        print("The file does not exist")

    # all question for blue
    if os.path.isfile(pathTempNew + "/" + allQ4Blue ):
        os.remove(pathTempNew + "/" + allQ4Blue )
    else:
        print("The file does not exist")

    # all question for red
    if os.path.isfile(pathTempNew + "/" + allQ4Red ):
        os.remove(pathTempNew + "/" + allQ4Red )
    else:
        print("The file does not exist")

def lobbyFileCreater():
    # creat all files in temp folder!
    # creat QR-Code

    # all User with id and IP
    file1 = open(str(pathTempNew) + "/" +str(allUser ), "a")
    file1.write("Creat File 4 all user\n")

    # team blue file
    file2 = open(str(pathTempNew) + "/" + str(teamBlue ), "a")
    file2.write("Creat File 4 teamBlue \n")

    # team red file
    file3 = open(str(pathTempNew) + "/" + str(teammRed ), "a")
    file3.write("Creat File 4 teammRed \n")

    # all question for blue
    file4 = open(str(pathTempNew) + "/" + str(allQ4Blue ), "a")
    file4.write("Creat File 4 allQ4Blue \n")

    # all question for red
    file5 = open(str(pathTempNew) + "/" + str(allQ4Red ), "a")
    file5.write("Creat File 4 allQ4Red \n")

def lobbyUserCreater(Name,id,ip):
    file1 = open(str(pathTempNew) + "/" + str(allUser), "a")
    file1.write(Name)
    file1.write("/")
    file1.write(id)
    file1.write("/")
    file1.write(ip)
    file1.write("!!")
    file1.write("\n")

def lobbyTeamCreater():
    people = []
    finish = True

    # take all user from allUser File (zeile für zeile) an put it in a team random!
    # for x in userlist
    file1 = open(str(pathTempNew) + "/" + str(allUser), "a")
    file1.write("Stopp adding new user, creat Teamlist")
    file1 = open(str(pathTempNew) + "/" + str(allUser), "r")

    # strip file that just the Teammeads avilebar are
    foo = file1.read()
    mainFile = str(foo)
    mainFile = mainFile.strip("Creat File 4 all user\n")
    mainFile = mainFile.strip("Stopp adding new user, creat Teamlist")
    mainFile = mainFile.splitlines()
    print("MainFile:")
    print(mainFile)
    print(type(mainFile))
    mainFile = str(mainFile)
    print("Wie ist es jetzt")
    print(type(mainFile))

    allPeople = mainFile
    print(allPeople)
    allPeople = allPeople.strip("1")[0]
    print(allPeople)

    #while finish==True:
    #    allPeople = mainFile
    #    print(allPeople)
    #    pass
    #    allPeople = allPeople.strip(", '")[1]
    #    print()
    #    #for x in allPeople:
        #    people = allPeople.strip("!")[0]
        #    print(people)
        #    time.sleep(2)


def appBootFunction(swFirmware):
    creatFolder()
    debugFunction.creatLog("helpderFuntcionGame", swFirmware)
    delOldFiles()
    lobbyFileCreater()



#ssidFinder()
#delOldFiles()
#lobbyFileCreater()
#lobbyUserCreater("Roberto","1","192.168.1.1")
#lobbyUserCreater("Fabio","2","192.168.1.2")
#lobbyUserCreater("Nik","3","192.168.1.3")
#lobbyUserCreater("Maria","4","192.168.1.4")

#lobbyTeamCreater()