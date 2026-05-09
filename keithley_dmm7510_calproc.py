from calibrationframework.instruments.keithley.keidmm7510 import DMM7510
from calibrationframework.instruments.fluke.flu5700a import Fluke5700A

from calibrationframework.procedures.dc_voltage_gen_test import dc_voltage_test

# VISA Addresses
DMM_ADDRESS = "TCPIP0::192.168.1.50::INSTR"

SOURCE_ADDRESS = "GPIB0::5::INSTR"

# Create instruments
dmm = DMM7510(DMM_ADDRESS)

source = Fluke5700A(SOURCE_ADDRESS)

# Identify instruments
print(dmm.identify())

print(source.identify())

# Run procedure
results = dc_voltage_test(dmm, source)

print("\nFinal Results:")

for result in results:

    print(result)