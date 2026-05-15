import pyvisa

class Instrument:

    def __init__(self, address=None):
        self.address = address
        self.rm = pyvisa.ResourceManager()
        self.resource = None
        if address:
            self.resource = self.rm.open_resource(address)

    def write(self, command):
        if self.resource is None:
            raise RuntimeError("Instrument resource is not open")
        self.resource.write(command)

    def query(self, command):
        if self.resource is None:
            raise RuntimeError("Instrument resource is not open")
        return self.resource.query(command)

    def identify(self):
        return self.query("*IDN?")
