import EstadoPCB

class PCBWaiting(EstadoPCB):
    
    def __init__(self) :
        pass
    
    def isReady (self) :
        return False
    
    def isWaiting (self) :
        return True
    
    def isRunning (self) :
        return False