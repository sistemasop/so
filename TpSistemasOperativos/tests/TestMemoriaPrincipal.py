import unittest
from Instruccion import *
from Programa import *
from MemoriaPrincipal import *

class Test(unittest.TestCase):


    def setUp(self):
    	instruccion1 = Instruccion('instruccion1')
    	instruccion2 = Instruccion('instruccion2')
    	instruccion3 = Instruccion('instruccion3')

    	programa = Programa('programa1')
    	programa.addIns(instruccion1)
    	programa.addIns(instruccion2)
    	programa.addIns(instruccion3)

    	memoria = Memoria()



    def testName(self):
        memoria.cargar(programa)
        self.assertEquals(memoria.__proximaAcargar, celdas[3], 'se cargo correctamente')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()