from .instrument import Instrument

class Source(Instrument):

    def set_voltage(self, value):

        raise NotImplementedError

    def output_on(self):

        raise NotImplementedError

    def output_off(self):

        raise NotImplementedError