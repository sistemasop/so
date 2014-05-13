
class Programa:
    
    def __init__(self, nombre):
        ''' Inicializa un programa con un nombre dado.

        '''
        self.nombre = nombre
        self.instrucciones = []
        self.pcb
           
    def printIns(self):
        #print(self.instrucciones)
        for i in self.instrucciones:
            i.verInstruccion()
        
    def addIns(self, elem):
        self.instrucciones.append(elem)

    def popIns(self):
        self.instrucciones().pop()

    def run(self, so):
        # Aca deberiamos crear un PCB?
        for i in self.instrucciones:
            i.run(so)