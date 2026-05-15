from ..base.source import Source

class Fluke5450A(Source):

    def __init__(self, address):
        super().__init__(address)

    def set_resistance(self, value):
        """Set the 5450A to a specific resistance value"""
        self.write(str(value))

    def set_voltage(self, value):
        """Not applicable for 5450A (resistance calibrator)"""
        raise NotImplementedError("Fluke 5450A is a resistance calibrator, not a voltage source")

    def output_on(self):
        """Not applicable for 5450A"""
        pass

    def output_off(self):
        """Not applicable for 5450A"""
        pass

    def clear(self):
        """Clear the 5450A"""
        self.write("Clear")
