import unittest
from Instruccion import *

class Test(unittest.TestCase):


    def setUp(self):
        self.instruccion = Instruccion("Soy una instruccion")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()