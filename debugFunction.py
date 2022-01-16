# Impot libarys
import os
from datetime import datetime
from main import pathTempNew, folderpathTemp, fromField, swFirmware

# variabel for debuging
debugFileName = "debugFunction.py"
fileName = "log.log"
localHost = "127.0.0.1"
varClass = "no Class"
now = datetime.now()


def creatFolder(folderpathTemp):
    # print("Start creat folder function")
    varFunction = "creatFolder"
    # variabel
    toolStart = True
    folderCheck = True


    while toolStart == True:
        # check that the Folder for debuging and update exist!
        # print("[start] toolStart")
        while folderCheck == True:
            # print("[start] folder Check")
            # print(i)
            if os.path.exists(pathTempNew):
                # print("[folder] exist")
                # print(i)
                folderCheck = False
            else:
                # print("[folder] not exist")
                # print("[folder] creat in Temp")
                os.system(r"md " + folderpathTemp)
            # print("[finish] folder Check")
        toolStart = False


# start the debugging
# creat the Log file in a folder
def creatLog(fromField, swFirmware):
    # from Template
    varFunction = "creatLog"
    #is file creadet?
    if os.path.isfile(pathTempNew + "/" + fileName):
        debug("----------", "----------", "----------", "----------", "----------")
        debug("IP - Adress", "File Name", "Class Name", "Function Name", "Message Typ")
        debug(localHost, debugFileName, varClass, varFunction, "/// Log: Continue log file")
    else:
        debug("----------", "----------", "----------", "----------", "----------")
        debug("IP - Adress", "File Name", "Class Name", "Function Name", "Message Typ")
        debug(localHost, debugFileName, varClass, varFunction, "/// Log: New log file Created")
    debug(localHost, debugFileName, varClass, varFunction, "/// Log: Start debugging mode from " + fromField)
    debug(localHost, debugFileName, varClass, varFunction, "/// Log: Create debugging logfile from " + fromField)
    debug(localHost, debugFileName, varClass, varFunction, "/// Log: Firmware Version is: " + str(swFirmware))


# so de Debug will be write in the Log file to found easier the trouble
# ip = ip, witch you try to communicat
# codePart = function name (def xy) to see from witch part the message come
# error = hier you can give the Error message or you make try: --- exception Exception e: an give the error log back like str(e)
def debug(ip, debugFileName, codeClass, function, error):
    file = open(str(pathTempNew) + "/" +str(fileName), "a")
    newNow = str(now)

    #foo =  newNow,"] "#, " [",ip,"] "," [",codePart,"] ", " [" , error,"]\n"


    file.write("[")
    file.write(str(now))
    file.write("]   ")
    file.write("[")
    file.write(ip)
    file.write("]   [")
    file.write(debugFileName)
    file.write("]   [")
    file.write(codeClass)
    file.write("]   [")
    file.write(function)
    file.write("]   [")
    file.write(error)
    file.write("]")
    file.write("\n")


def individuallyDebug(yourText):
    file = open(str(pathTempNew) + "/" +str(fileName), "a")
    newNow = str(now)


# default debugging Message to stopp that function in logfile
# it will not set the variabel debugMode to Fals!
def stoppDebug(fromField):
    # from Template
    varFunction = "stoppDebug"
    debug(localHost, debugFileName, varClass, varFunction, "/// Log: stopp debugging mode from " + fromField)


# Templates
class Default0():

    # from Template
    varClass = "Default0()"

    # from Template
    #debugFunction.debug(localHost, debugFileName, varClass, "class", "### Log: Class [Default]")

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


try:
    creatFolder(folderpathTemp)
    creatLog(fromField, swFirmware)
    print("Folder and logfile creat successfuli")
except Exception as error:
    print("fail to creat Folder")