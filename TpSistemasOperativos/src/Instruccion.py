class Instruccion:

    def __init__(self,descripcion):
        ''' Inicializa una instruccion de un programa con
        una descripcion'''
        self.descripcion = descripcion
        
    def run(self, so):
        print(self.descripcion)
    