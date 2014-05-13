class Instruccion:

    def __init__(self,descripcion):
        ''' Inicializa una instruccion de un programa con
        una descripcion'''
        self.descripcion = descripcion
        # Agregamos un booleano que indique si es o no I/O o creamos una jerarquia de clases?

    def verInstruccion(self):
    	# Este metodo no se si es necesario pero lo estabamos usando en Programa
    	# y no estaba implementado
        print (self.descripcion)
        
    def run(self, so):
        print(self.descripcion)
    