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

def ssidFinder():
    try:
        ssid = subprocess.check_output("netsh wlan show network")
        ssid = ssid.splitlines()
        ssid = str(ssid)
        ssid = ssid.split("SSID 1")[1]
        ssid = ssid.split("Netzwerktyp")[0]
        ssid = ssid.split(":")[1]
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

def fileHandler():
    pass