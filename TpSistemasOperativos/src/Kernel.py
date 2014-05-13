
class Kernel:

    def __init__(self, so, disco):
        self.so = so                # conoce a standar output
        self.disco = disco
        self.procesos = [] #tenemos que cambiar la estructura
        #self.memoria = memoria
        self.numeroDeProcesos = 0

    def load(self, prog):
        print(self.disco.cargar(prog))

    def run(self, nombrePrograma):
        self.numeroDeProcesos = self.numeroDeProcesos + 1
        # tiene que ir a buscar el programa a disco
        ins = self.disco.cargar(nombrePrograma)
        
        print(ins)