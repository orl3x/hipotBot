import pyautogui as pag
import time
import os
def img(name):
    return 'guiImg\\'+name

# MES SCREENSHOTS
mesIconPic = img("mesShortcut.png")
mesUpdateOkButton = img("mesUpdateOkButton.png")
mesLoginBtnPic = img("mesLoginBtn.png")
emptyLoginWindow = img("emptyLoginWindow.PNG")
userNameEntry = img("userNameEntry.PNG")
passwordEntry = img("passwordEntry.PNG")
mesSideMenuBtnPic = img("mesSideMenuBtn.png")
startWorkingSideMenuPic = img("startWorkingSideMenu.PNG")
blueOKbtnPic = img("blueOKbtn.PNG")
processScanSearchPic = img("processScanSearch.PNG")
processScanSearchTextBoxPic = img("processScanSearchTextBox.PNG")
mesSearchBtnPic = img("mesSearchBtn.PNG")


#HIPOT SCREENSHOTS
hipotShortcut = img("HipotShortcut.PNG")
hipotSettingsBtn = img("hipotSettings.PNG")
hipotOpenBtn = img("hipotOpenBtn.PNG")
hipotTestFileFolderPic = img("hipotTestFilesFolder.PNG")
hipotOkBtnPic = img("hipotOkBtn.PNG")
hipotSerialPortErrorPic = img("hipotSerialPortError.PNG")
hipotAutoSwitchBtn = img("hipotAutomaticSwitchingBtn.PNG")

def showDesktop():
    pag.hotkey('win','d')

def mesNeedsLogin(boolean):
    if boolean:
        findAndClick(userNameEntry, 3, 0.95, False)
        pag.write("001864")
        findAndClick(passwordEntry, 3, 0.95, False)
        pag.write("001864")
    print('False')

def findAndClickSimple(img, timeLimit, conf, doubleClick):
    cords = None
    timeLimit = (timeLimit/0.4)
    i = timeLimit
    while cords is None:
     if i > 0:
        i=i-1
        cords = pag.locateCenterOnScreen(img, confidence=conf)
        time.sleep(0.2)
     else:
         print('Out')
         break

    if doubleClick:
         pag.doubleClick(cords)
    else:
         pag.click(cords)

def findAndClick(img, timeLimit, conf, doubleClick):
    cords = None
    timeLimit = (timeLimit/0.4)
    i = timeLimit
    while cords is None:
     if i > 0:
        i=i-1
        cords = pag.locateCenterOnScreen(img, confidence=conf)
        time.sleep(0.2)
     else:
         print('Out')
         pag.alert("Ocurrio un error, solicite apoyo al técnico de pruebas")
         exit()

    if doubleClick:
         pag.doubleClick(cords)
    else:
         pag.click(cords)

def findAndBool(img, timeLimit, conf):
    cords = None
    timeLimit = (timeLimit/0.4)
    i = timeLimit
    while cords is None:
     if i > 0:
        i=i-1
        cords = pag.locateCenterOnScreen(img, confidence=conf)
        print("i value is "+str(i))
        time.sleep(0.2)
     else:
         return False

     return True




def killTasks():
    os.system("taskkill /im MES(MEXICO).exe -f")
    os.system('taskkill /im "HIPOT For Mexico-3.0.exe" -f')
