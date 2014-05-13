class Disco:

  
    def __init__(self):
        ''' Inicializa un disco vacio, es decir, 
        sin programas.
        Su contenido (los programas que se guardan en el) se 
        representa con un map 
        'nombrePrograma' -> '[instrucciones]'
    '''
        self.contenido = {}
        
    def agregarPrograma(self, programa):
        ''' Agrega un programa al disco'''
        self.contenido [programa.nombre] = programa.instrucciones
        
    def verContenido(self):
        ''' Muestra el contenido del disco'''
        print(self.contenido)

    def cargar(self, nombrePrograma):
        ''' Devuelve las instrucciones de un programa'''
        return self.contenido[nombrePrograma]