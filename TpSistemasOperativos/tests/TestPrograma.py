import unittest
from Programa import *
from Instruccion import *

class Test(unittest.TestCase):


    def setUp(self):
        self.instruccion1 = Instruccion("Instruccion1")
        self.instruccion2 = Instruccion("Instruccion2")
        self.instruccion3 = Instruccion("Instruccion3")
        self.programa = Programa("Programa")


    def testAgregarInstrucciones(self):
        self.programa.addIns(self.instruccion1)
        self.programa.addIns(self.instruccion2)
        self.programa.addIns(self.instruccion3)
        
        self.assertEqual(self.programa.instrucciones, [self.instruccion1, self.instruccion2, self.instruccion3], "Las instrucciones no se agregaron correctamente")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()