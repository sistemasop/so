
class Programa:
    
    def __init__(self, nombre):
        ''' Inicializa un programa con:
            - un nombre dado
            - una lista de instrucciones vacia
            - un PCB (cuya relacion se crea, cuando se ejecuta
              el programa)
        '''
        self.nombre = nombre
        self.instrucciones = []
        self.pcb # es una sola instancia o hay que guardar todas 
                 # las relaciones cada vez que se ejecuta el 
                 # porgrama????
           
    def printIns(self):
        for i in self.instrucciones:
            i.verInstruccion()
        
    def addIns(self, instruccion):
        self.instrucciones.append(elem)

    def popIns(self):
        self.instrucciones().pop()

    def run(self, so):
        # Aca deberiamos crear un PCB?
        for i in self.instrucciones:
            i.run(so)