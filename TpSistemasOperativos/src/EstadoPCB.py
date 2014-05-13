
class EstadoPCB(object):
    ''' Es una clase abstracta que provee los metodos a
    los distintos estados que puede tomar un PCB'''

    def __init__(self) :
        pass
    
    def isReady (self) :
        pass
    
    def isWaiting (self) :
        pass
    
    def isRunning (self) :
        pass