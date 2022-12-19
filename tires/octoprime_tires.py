from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tires_wear):
        self._tires_wear = tires_wear
    
    def needs_service(self):
        return sum(self._tires_wear) >= 3