import unittest
from Disco import *
from Programa import *
from Instruccion import *

class Test(unittest.TestCase):

    def setUp(self):
        #Creo una instruccion
        self.instruccion = Instruccion("Instruccion 1")
        #Creo un programa
        self.programa = Programa("Programa")
        #Agrego la instruccion creada al programa
        self.programa.addIns(self.instruccion)
        #Creo un disco
        self.disco = Disco()
       

    def testAgregarPrograma(self):
        self.mapEsperado = {}
        self.mapEsperado [self.programa.nombre] = self.programa.instrucciones
        self.disco.agregarPrograma(self.programa)
        
        self.assertEqual(self.mapEsperado, self.disco.contenido, "El programa no se encuentra dentro del disco")        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    print(self.disco.contenido)