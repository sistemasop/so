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
        self.contenido [programa.nombre] = programa.instrucciones
        # El nombre del programa es la clave y la coleccion de instrucciones
        # es el valor del map.
        
    def verContenido(self):
        ''' Muestra el contenido del disco, es decir, los programas que
        se encuentran en el disco y su coleccion de instrucciones'''
        print(self.contenido)

    def cargar(self, nombrePrograma): # Luis, este metodo para que lo pusimos?????
        ''' Devuelve las instrucciones de un programa'''
        return self.contenido[nombrePrograma]