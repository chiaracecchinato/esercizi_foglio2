class Calcolatrice:
    def addizione(a, b):
        if (isinstance(a, int) & isinstance(b, int)) | (isinstance(a, float) & (isinstance(b, float))): 
            somma=a+b
            return somma
        else:
            print("I valori non sono dello stesso tipo")
    
    def sottrazione(a,b):
        if (isinstance(a, int) & isinstance(b, int)) | (isinstance(a, float) & (isinstance(b, float))):
            sott=a-b
            return sott
        else:
            print("I valori non sono dello stesso tipo")
    
    def moltiplicazione(a, b):
        if (isinstance(a, int) & isinstance(b, int)) | (isinstance(a, float) & (isinstance(b, float))):
            prodotto=a*b
            return prodotto
        else:
            print("I valori non sono dello stesso tipo")

    def divisione(a, b):
        if (isinstance(a, int) & isinstance(b, int)) | (isinstance(a, float) & (isinstance(b, float))):
            if b==0:
                print("La divisone per 0 non è ammessa!")
            else:
                quoziente=a/b
                return quoziente
        else:
            print("I valori non sono dello stesso tipo")
    
    def potenza(a, b):
        if (isinstance(a, int) & isinstance(b, int)):
            if b==0:
                return 1
            if b==1:
                return a
            else:
                pot=a**b
                return pot
        else:
            print("I valori non interi o dello stesso tipo")
    
    def modulo(a, b):
        if (isinstance(a, int) & isinstance(b, int)) | (isinstance(a, float) & (isinstance(b, float))):
            mod=a%b
            return mod
        else:
            print("I valori non sono dello stesso tipo")
    
    def radice(a, b):
        if (isinstance(a, int) & isinstance(b, int)) | (isinstance(a, float) & (isinstance(b, float))):
            if a>0 and b>0:
                radicando=a**(1/b)
                return mod
            else:
                print("impossibile fare la radice di numeri negativi")
        else:
            print("I valori non sono dello stesso tipo")

    def conversione(a, b):
        if (isinstance(a, int) & isinstance(b, int)) | (isinstance(a, float) & (isinstance(b, float))):
            if b==2:
                while n>0:
                    quoz=a//2
                    resto=a%2
                    prod*=rest0
                    somma+=resto
                    a=quoz
                conv=prod-somma
                return conv
            else:
                print("impossibile fare la conversione in una base diversa da 2")
        else:
            print("I valori non sono dello stesso tipo")

class Test:
    