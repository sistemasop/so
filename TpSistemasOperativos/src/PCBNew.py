import EstadoPCB:

class PCBNew(EstadoPCB):
    
    def __init__(self) :
        pass
    
    def isReady (self) :
        return False
    
    def isWaiting (self) :
        return False
    
    def isRunning (self) :
        return False