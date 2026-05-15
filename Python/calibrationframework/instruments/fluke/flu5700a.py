from ..base.source import Source

class Fluke5700A(Source):

    def reset(self):

        self.write("*RST")

    def set_voltage(self, value):

        cmd = f"OUT {value}V"

        self.write(cmd)

    def output_on(self):

        self.write("OPER")

    def output_off(self):

        self.write("STBY")