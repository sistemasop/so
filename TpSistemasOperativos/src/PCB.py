class PCB:

    def __init__(self):
        self.contadorDePrograma #Indica cual es la siguiente instruccion
        self.apuntadorDePila
        self.posicionDeInicio
        self.posicionDeFin 
        self.estado = PCBNew() #Se inicializa con el estado New
        self.idProcess = kernel.numeroDeProcesos #El ID process debe ser un numero
        										 # unico. En este caso, se asigna el
        										 # numero de programas ejecutados por 
        										 # el kernel
        
        