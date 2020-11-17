# here the debugs are created
import time
import os
from datetime import datetime

now = datetime.now()

# variabel for debuging
pathTemp = R"${TEMP}/MontagsMaler"
pathTempNew = os.path.expandvars(pathTemp)
fileName = "log.log"

# start the debugging
# creat the Log file in a folder
def creatLog(fromField, swFirmware):
    #is file creadet?
    if os.path.isfile(pathTempNew + "/" + fileName):
        debug("127.0.0.1", "creatLog", ("continue log file"))
    else:
        debug("127.0.0.1", "creatLog", ("New log file Created"))
    debug("127.0.0.1", "creatLog", ("start debugging mode from " + fromField))
    debug("127.0.0.1", "creatLog", ("create debugging logfile from " + fromField))
    debug("127.0.0.1", "creatLog", "Firmware Version is: " + str(swFirmware))


# so de Debug will be write in the Log file to found easier the trubel
# ip = ip, witch you try to communicat
# codePart = function name (def xy) to see from witch part the message come
# error = hier you can give the Error message or you make try: --- exception Exception e: an give the error log back like str(e)
def debug(ip, codePart, error):
    file = open(str(pathTempNew) + "/" +str(fileName), "a")
    newNow = str(now)

    #foo =  newNow,"] "#, " [",ip,"] "," [",codePart,"] ", " [" , error,"]\n"


    file.write("[")
    file.write(str(now))
    file.write("]   ")
    file.write("[")
    file.write(ip)
    file.write("]   [")
    file.write(codePart)
    file.write("]   [")
    file.write(error)
    file.write("]")
    file.write("\n")

   #file.write(str(foo))

# default debugging Message to stopp that function in logfile
# it will not set the variabel debugMode to Fals!
def stoppDebug(fromField):
    debug("127.0.0.1", "stoppDebug", "stopp debugging mode from " + fromField)

