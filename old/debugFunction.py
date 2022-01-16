# here the debugs are created
import time
import os
from datetime import datetime

now = datetime.now()

# variabel for debuging
pathTemp = R"${TEMP}/MontagsMaler"
pathTempNew = os.path.expandvars(pathTemp)
debugFileName = "debugFunction.py"
fileName = "log.log"
localHost = "127.0.0.1"
varClass = "no Class"

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


# so de Debug will be write in the Log file to found easier the trubel
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

   #file.write(str(foo))

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
