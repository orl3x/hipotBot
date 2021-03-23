########################################################
#DEFINE PATH
def img(name):
    return 'modelsImg\\'+name

########MODEL FAMILIES SS#########################


class Driver():
    def __init__(self, model='', ssHipot=''):
        self.model = model
        self.ssHipot = ssHipot


    def get_data(self):
        print("Model: "+str(self.model)+" SS_Hipot: "+str(self.ssHipot))


    def getName(self):
        return self.model

#DEFINE MODEL OBJECTS
#################       EUD FAMILY #######################################################
EUD075S180DT = Driver("EUD075S180DT", img("EUD075S180DT.PNG"))

EUD075S280DT = Driver("EUD075S280DT", img("EUD075S280DT.PNG"))

EUD150S350DTA = Driver("EUD150S350DTA", img("EUD150S350DTA.PNG"))

EUD150S560DTA = Driver("EUD150S560DTA", img("EUD150S560DTA.PNG"))

EUD240S100DT = Driver("EUD240S100DT", img("EUD240S100DT.PNG"))

EUD600S12ADT = Driver("EUD600S12ADT", img("EUD600S12ADT.PNG"))


##############################ESD FAMILY ###################################################
ESD150S350DT = Driver("ESD150S350DT", img("ESD150S350DT.PNG"))

ESD150S560DT = Driver("ESD150S560DT", img("ESD150S560DT.PNG"))

ESD240S460DT = Driver("ESD240S460DT", img("ESD240S460DT.PNG"))

ESD240S660DT = Driver("ESD240S660DT", img("ESD240S660DT.PNG"))

ESD320S150DT = Driver("ESD320S150DT", img("ESD320S150DT.PNG"))

ESD320S620DT = Driver("ESD320S620DT", img("ESD320S620DT.PNG"))

ESD600S12ADT = Driver("ESD600S12ADT", img("ESD600S12ADT.PNG"))


############################## EUG FAMILY ###################################################
EUG150S105DT = Driver("EUG150S105DT", img("EUG150S105DT.PNG"))

EUG150S350DT = Driver("EUG150S350DT", img("EUG150S350DT.PNG"))
