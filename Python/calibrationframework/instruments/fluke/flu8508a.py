from ..base.dmm import DMM

class Fluke8508A(DMM):

    def __init__(self, address):
        super().__init__(address)

    def set_ratio_mode(self, front_rear=True):
        """Set the 8508A to Ratio mode (Front/Rear)"""
        if front_rear:
            self.write("Inp:DIV_REAR")
        else:
            self.write("Inp:DIV_FRONT")

    def measure_dc_voltage(self):
        self.write("VOLT:DC:Auto,Resl8,Fast_Off")
        reading = self.query("READ?")
        return float(reading)

    def measure_ratio(self):
        """Measure ratio in ratio mode"""
        reading = self.query("READ?")
        return float(reading)
