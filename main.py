######################################################################################
# Description
# 1. please adjust all path and links below
# 2. note current firmware
# 3. if update method is not included, set uptodate to "True"
#
# From the debugFunction the folders and logfiles are created automatically.
# Important: Folder name must be correct, so that the logs are written correctly.
######################################################################################

# public Library
import os

# local library
import updateFunction
import debugFunction

# Some file variable
fromField = "main.py"
swFirmware = "1.0.0"

# debugs Variabel
# ip, debugFileName, codeClass, function, error
ip = "127.0.0.1"
debugFileName = "main.py"
codeClass = "no Class main"
function = "main_debug_class"

# Path Variable 4 debugFunction
pathTemp = R"${TEMP}/MontagsMaler"  # To Do
pathTempNew = os.path.expandvars(pathTemp)
folderpathTemp = r"%temp%\MontagsMaler" # To Do

# update filename
updateFile = R"${TEMP}/Update_Framework/update.msi" # To Do
updateFile = os.path.expandvars(updateFile)

# Stat variabels
uptodate = True

# Update Links
# this link is for the new version
ud_donwload_link = "https://melonih0me.ddns.net/index.php/s/6GPPB2s3KYnDy5e"
ud_donwload_link = "https://melonih0me.ddns.net/index.php/s/6GPPB2s3KYnDy5e/download/First Update File.msi"

# ud_pw_link =
# maby later in use

# this link is for checking the version of the Programm
up_version_link = "https://melonih0me.ddns.net/index.php/s/xnDPfkiBnHSRcts"
up_version_link = "https://melonih0me.ddns.net/index.php/s/xnDPfkiBnHSRcts/download/Version_File.md"

# this folder is to upload log files, check permissions!
up_log_link = "https://melonih0me.ddns.net/index.php/s/77kFbRD3ifSE56o"

# Start Script
if __name__ == "__main__":
    # Start
    print("Courent Version: ", swFirmware)
    uptodate = updateFunction.check4update(up_version_link, swFirmware)
    if uptodate == False:
        foo = input("Update available!\nDo you want to update? [y/yes]")
        if foo.lower() in ["y", "yes"]:
            debugFunction.debug(ip, debugFileName, codeClass, function, ("!!! Update available !!! +++ Download startet, input: " + foo))
            download_finish = updateFunction.download_update(ud_donwload_link, updateFile)
            if download_finish == True:
                updateFunction.install_update(updateFile)
        else:
            debugFunction.debug(ip, debugFileName, codeClass, function, ("!!! Update available !!! --- No download startet, input: " + str(foo)))
