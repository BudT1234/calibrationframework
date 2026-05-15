from calibrationframework.instruments.keithley.kei2700 import Keithley2700
from calibrationframework.instruments.fluke.flu8508a import Fluke8508A
from calibrationframework.instruments.fluke.flu5700a import Fluke5700A
from calibrationframework.instruments.fluke.flu5450a import Fluke5450A

from calibrationframework.procedures.fluke5450a_drift_test import fluke5450a_drift_test

# VISA Addresses
DAQ_ADDRESS = "GPIB0::20::INSTR"
DMM_ADDRESS = "GPIB0::15::INSTR"
CALIBRATOR_ADDRESS = "GPIB0::10::INSTR"
RESISTOR_ADDRESS = "GPIB0::25::INSTR"

# Create instruments
daq = Keithley2700(DAQ_ADDRESS)
dmm = Fluke8508A(DMM_ADDRESS)
calibrator = Fluke5700A(CALIBRATOR_ADDRESS)
resistor = Fluke5450A(RESISTOR_ADDRESS)

# Identify instruments
print("Identifying instruments...")
print(f"DAQ: {daq.identify()}")
print(f"DMM: {dmm.identify()}")
print(f"Calibrator: {calibrator.identify()}")
print(f"Resistor: {resistor.identify()}")

# Run drift test procedure
print("\n" + "="*50)
results = fluke5450a_drift_test(daq, dmm, calibrator, resistor)

print("\n" + "="*50)
print("\nDrift Test Results:")
for result in results:
    print(result)
