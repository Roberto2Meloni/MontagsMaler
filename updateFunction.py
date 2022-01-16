# Imports
import debugFunction
import urllib.request
import requests
import os

# Description
# All links for version, download and logfiles is needet to declar at main.py file

# Variabel
# debug variabels
filename = "updateFunction.py"
ip = "127.0.0.1"
myclass = "no Class"

# Function To Do
# 1. check version for "up to date"                 ok
# 2. if up to to date, do nothing                   ok
# 2. if not up to date, download new firmware       ok
# 3. install new firmware


# Update function
def check4update(url, swFirmware):
    debugFunction.debug(ip,filename,myclass,"check4update", "Check 4 update")
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
        print("Last Version: ", decoded_line)

    # compare firmware from cloud with own firmware
    if decoded_line == swFirmware:
        debugFunction.debug(ip,filename,myclass,"check4update", "FW is up to date")
        return True
    else:
        debugFunction.debug(ip,filename,myclass,"check4update", "FW is not up to date!")
        return False


def download_update(url, updateFile):
    download_finish = False
    try:
        debugFunction.debug(ip, filename, myclass, "download_update", "Start Download new file")
        r = requests.get(url, allow_redirects=True)
        open(updateFile, 'wb').write(r.content)
        debugFunction.debug(ip, filename, myclass, "download_update", "Finish download file in %temp% folder")
        download_finish = True
    except Exception as error:
        debugFunction.debug(ip, filename, myclass, "download_update", str(error))
        print("Error")
    return download_finish


def install_update(updateFile):
    try:
        debugFunction.debug(ip, filename, myclass, "install_update", "Start to install update file")
        os.system('msiexec /i %s /qn' % updateFile)
        debugFunction.debug(ip, filename, myclass, "install_update", "Finish to install update file")
    except Exception as error:
        debugFunction.debug(ip, filename, myclass, "install_update", "!!! Error by install update file!")
        debugFunction.debug(ip, filename, myclass, "install_update", str(error))
        