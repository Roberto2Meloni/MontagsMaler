import os
import sys
import subprocess

swFirmware = "1.0"

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

def networkStarter():
    cli = subprocess.call("netsh wlan show network")
    cli = str(cli)
    print(type(cli))
    ssid = cli.split()
    # ssid = ssid.split(" ")[0]
    #print(test)
    print("Jetzt kommt die SSID")
    print(ssid)
    # WLAN SSID return
    # start webserver


networkStarter()