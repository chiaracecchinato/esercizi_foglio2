class Calcolatrice:
    def __init__(self, a, b):
        self.a=a
        self.b=b 

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
                while a>0:
                    quoz=a//2 #//arrotonda la divisione al numero intero più vicino
                    resto=a%2
                    prod*=resto
                    somma+=resto
                    a=quoz
                conv=prod-somma
                return conv
            else:
                print("impossibile fare la conversione in una base diversa da 2")
        else:
            print("I valori non sono dello stesso tipo")


import unittest

class Test(unittest.TestCase):

    calcolo = Calcolatrice(a=4, b=2)

    def test_somma(self):
        self.assertEqual(calcolo.addizione, 6)

    def test_sottrazione(self):
        self.assertEqual(calcolo.sottrazione, 2)

    def test_moltiplicazione(self):
        self.assertEqual(calcolo.moltiplicazione, 8)

    def test_divisione(self):
        self.assertEqual(calcolo.divisione, 2)

    def test_potenza(self):
        self.assertEqual(calcolo.potenza, 16)

    def test_modulo(self):
        self.assertEqual(calcolo.modulo, 0)

    def test_radice(self):
        self.assertEqual(calcolo.radice, 2)

    def test_conversione(self):
        self.assertEqual(calcolo.conversione, 0)
    