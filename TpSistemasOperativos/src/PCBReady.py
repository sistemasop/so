import EstadoPCB:

class PCBReady(EstadoPCB):
    
    def __init__(self) :
        pass
    
    def isReady (self) :
        return True
    
    def isWaiting (self) :
        return False
    
    def isRunning (self) :
        return False