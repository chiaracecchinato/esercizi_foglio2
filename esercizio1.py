import random

class Automa:
    def __init__(self):
        self.biancheria=None
        self.calzini=None
        self.maglia=None
        self.pantaloni=None
        self.calzatura=None

    def intimo(self):
        self.biancheria=True
        return 1
    
    def calze(self):
        self.calzini=True
        return 1
    
    def magl(self):
        self.maglia=True
        return 1
    
    def panta(self):
        self.pantaloni=True
        return 1
    
    def scarpe(self):
        self.calzatura=True
        return 1

def esegui(automa, capo):
    if capo==biancheria:
        ok=automa.intimo()
    elif capo==calzini:
        ok=automa.calze()
    elif capo==maglia:
        ok=automa.magl()
    elif capo==pantalone:
        ok=automa.panta()
    else:
        ok=0

    return ok    

automa=Automa()
capi_vestiario=[biancheria, calzini, maglia, pantalone, calzatura]
vestito=True

while(vestito){
    capo=random.choice(lista)
    if(pantaloni==True and biancheria==None):
        print("non può indossare i pantaloni prima della biancheria")
    elif(calzatura==True and calzini==None):
        print("non può indossare le scarpe prima dei pantaloni")
    else:
        print("può indossare gli abiti")
    
    esegui(automa, capo)

    if(esegui==1):
        print("automa vestito adeguatamente")
    else:
        raise print("Errore! E' stato resitutito 0 in maniera casuale")  
}
  