from ..base.dmm import DMM

class Keithley2700(DMM):

    def __init__(self, address):
        super().__init__(address)

    def select_channel(self, channel):
        """Select a channel on the switch card"""
        self.write(f"SOUR:CLOS (@{channel})")

    def measure_dc_voltage(self):
        self.write("SENS:FUNC 'VOLT:DC'")
        reading = self.query("READ?")
        return float(reading)

    def measure_resistance(self):
        self.write("SENS:FUNC 'RES'")
        reading = self.query("READ?")
        return float(reading)
