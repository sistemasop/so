from Programa import *

class Disco:

    def __init__(self):
        ''' Inicializa un disco vacio, es decir, sin programas.
        Su contenido (programas que se guardan en el) se 
        representa con un map 
            'nombrePrograma' -> '[instrucciones]'
    '''
        self.contenido = {}
        
    def agregarPrograma(self, programa):
        ''' Agrega un programa al disco'''
        self.contenido [programa.__nombre] = programa.__instrucciones
        # El nombre del programa es la clave y la coleccion de instrucciones
        # es el valor del map.
        
    def verContenido(self):
        ''' Muestra el contenido del disco, es decir, los programas que
        se encuentran en el disco y su coleccion de instrucciones'''
        print(self.contenido)

    def run(self, nombrePrograma):
        ''' Devuelve las instrucciones de un programa para pasarlas como
        parametro y se carguen en memoria'''
        # Hay que analizar la estructura que estamos utilizando
        # porque en este momento hay que mandarle el mensaje run a la
        # instancia de programa que estamos ejecutando para que cree
        # su PCB, por ejemplo 
        #   programa.run()
        return self.contenido[nombrePrograma]