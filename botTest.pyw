import pyperclip
import tkinter as tk
import tkinter.ttk as ttk
from guiScreenshots import *
from modelNames import *


guiPasswords = {'201101','2020', '5313'}
bgColor= "#e7e7de"
entryBg = "#f8f1f1"
textColor = entryBg
textColor2 = '#00587a'
entryTextColor = "#008891"
buttonColor1 = "#00587a"
buttonColor2 = "#008891"
testWithoutWO = False


def scanProduct():


    def testWithoutMes():
        global testWithoutWO
        testWithoutWO = True
        print(testWithoutWO)
        root.destroy()

    #CREATING WIDGET WINDOW
    print("Ejecutando scan product")
    global root
    root = tk.Tk()
    root.title("Hipot BOT v1.0")
    root.config(bg=bgColor)
    root.iconbitmap("bot.ico")

    # CREATING TEXT VARIABLE FOR SERIAL NUMBER ENTRY
    global product
    product = tk.StringVar()

   ##########################   DEFINING LABELS, BUTTONS AND TEXTBOX    ##################################################

    #LABEL "ESCANEE EL NUMERO DE SERIE"
    label = tk.Label(root, text="Escaneé el número de serie:")
    label.config(font=('Franklin Gothic Medium', '40'), fg=textColor2, bg=bgColor)

    #CREATING AND SETTING UP TEXT BOX
    textBox = tk.Entry(root, textvariable=product, width=20)
    textBox.config(font=('Arial', 40), bd=4, bg=entryBg, fg="#008891")


    #ENTER EVENT ACTION
    def enterEvent(event):
        global workOrder
        workOrder = tk.StringVar()
        workOrder.set(product.get())
        root.destroy()

    #KILL MODEL SELECTION WINDOW
    def endProgram():
        exit()



    #DEFINE "ENTER" KEY PRESS ACTION FOR THE ENTRY TEXTBOX
    root.bind('<Return>', enterEvent)

    ########################    PACK ALL THE COMPONENTS INTO THE WIDGETS    ##############
    label.grid(column=0, row=1, columnspan=2, padx=(20))
    textBox.grid(column=0, row=2, ipadx=20, columnspan=2, padx=(20), pady=(0,20))



    #FOCUS TEXTBOX
    textBox.focus()

    #SELECT "X" BUTTON ACTION
    root.protocol("WM_DELETE_WINDOW", endProgram)
    root.mainloop()



def mes():
    ##OPEN MES
    showDesktop()
    findAndClick(mesIconPic, 5, 0.8, True)
    findAndClick(mesLoginBtnPic, 10, 0.9, False)
    findAndClick(mesSideMenuBtnPic,10, 0.9,False)
    findAndClick(startWorkingSideMenuPic,10, 0.9,False)
    time.sleep(0.2)
    pag.press('tab')
    ## PASTE AND ENTER WO
    pag.write(workOrder.get())
    pag.press('enter')
    findAndClick(blueOKbtnPic,4, 0.9,False)
    time.sleep(0.2)
    pag.press('enter')

    #DEFINE GLOBAL VARIABLE TO STORE MODEL
    global model
    ##LOOK FOR PROCESS SCAN SEARCH
    findAndClick(processScanSearchPic, 5, 0.9, False)
    findAndClick(processScanSearchTextBoxPic, 5, 0.9, False)
    time.sleep(0.2)

    ##ENTER WO IN PROCESS SCAN SEARCH
    pag.write(workOrder.get())
    findAndClick(mesSearchBtnPic, 5, 0.9, False)
    time.sleep(0.5)
    pag.press('tab', presses=5)
    time.sleep(0.2)
    pag.keyDown('ctrlleft')
    pag.press('c')
    pag.keyUp('ctrlleft')

    ##SET MODEL INTO VARIABLE
    model = pyperclip.paste()
    model = eval(model.replace('-',''))
    showDesktop()
    return model



def showDesktop():
    # SHOW DESKTOP
    time.sleep(0.2)
    pag.hotkey("win","d")

def openHipot():
    global modelHipotFile
    findAndClick(hipotShortcut,3,0.95,True)
    findAndClick(hipotSettingsBtn,5, 0.95, False)
    findAndClick(hipotOpenBtn, 5, 0.95, False)
    time.sleep(1)
    pag.press('tab',8)


    hipotTestFilesCoords = pag.locateCenterOnScreen(hipotTestFileFolderPic, confidence=0.95)
    while hipotTestFilesCoords is None:
        hipotTestFilesCoords = pag.locateCenterOnScreen(hipotTestFileFolderPic, confidence=0.95)
        print('Looking for file')
        pag.scroll(-100)
    print("File found")
    pag.doubleClick(hipotTestFilesCoords)

    print(modelHipotFile)
    hipotFileCoords = pag.locateCenterOnScreen(modelHipotFile, confidence=0.94)
    while hipotFileCoords is None:
        hipotFileCoords = pag.locateCenterOnScreen(modelHipotFile, confidence=0.94)
        print("Looking for file")
        pag.scroll(-100)
    print("File found")
    pag.doubleClick(hipotFileCoords)


    findAndClick(hipotOkBtnPic, 3, 0.95, False)
    time.sleep(1)
    if pag.locateCenterOnScreen(hipotSerialPortErrorPic, confidence=0.95) is None:
        print("Serial error not found")
    else:
        pag.alert("Ocurrió un error, solicite el apoyo del técnico de pruebas")
        exit()
    findAndClick(hipotAutoSwitchBtn, 3, 0.95, False)
    time.sleep(0.3)
    pag.alert("¡Configuración exitosa!\n Puede comenzar a probar las unidades.")







# INITIALIZING REQUIRED FUNCTIONS
killTasks()
scanProduct()
model = mes()
# print("Screenshot location is "+model.ssHipot)
modelHipotFile = model.ssHipot
# print("Model ATS file is "+modelHipotFile)
openHipot()


















