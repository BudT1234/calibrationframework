
from instruments.base.dmm import DMM

class HP34420A(DMM):

    def measure_dc_voltage(self):
        self.write("CONF:VOLT:DC")
        return float(self.query("READ?"))

    def measure_resistance(self):
        self.write("CONF:RES")
        return float(self.query("READ?"))