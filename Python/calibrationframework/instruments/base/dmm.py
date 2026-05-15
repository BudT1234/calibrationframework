# instruments/base/dmm.py

from .instrument import Instrument

class DMM(Instrument):

    def measure_dc_voltage(self):
        raise NotImplementedError

    def measure_resistance(self):
        raise NotImplementedError