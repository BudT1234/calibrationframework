from ..base.dmm import DMM

class DMM7510(DMM):

    def __init__(self, address):

        super().__init__(address)

    def identify(self):

        return self.query("*IDN?")

    def reset(self):

        self.write("*RST")

    def measure_dc_voltage(self):

        self.write("SENS:FUNC 'VOLT:DC'")

        reading = self.query("READ?")

        return float(reading)

    def measure_resistance(self):

        self.write("SENS:FUNC 'RES'")

        reading = self.query("READ?")

        return float(reading)