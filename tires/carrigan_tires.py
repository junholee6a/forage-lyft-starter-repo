from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tires_wear):
        self._tires_wear = tires_wear
    
    def needs_service(self):
        return max(self._tires_wear) >= 0.9