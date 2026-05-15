"Drift of 5450A"
import pyvisa
import time

# Set up the VISA resource manager
rm = pyvisa.ResourceManager()

#connect to the instruments
calibrator = rm.open_resource("GPIB::10::INSTR") #Fluke 5700A
daq = rm.open_resource("GPIB::20::INSTR") #Keithley 2700
dmm = rm.open_resource("GPIB::15::INSTR") #Fluke 8508A
resistor = rm.open_resource("GPIB::25::INSTR") #Fluke 5450A

# Optional: Set read/read termination if needed
for inst in [calibrator, daq, multimeter, resistor]:
    inst.read_termination = '\n'
    inst.write_termination = '\n'

print("Connect 5450A in series with the 2700's 742A and the 5700A,"
      "conncet the sense leads of the 2700 to the rear of "
      "the 8508A and connect the front sense connectors to "
      "the front input of the 8508A.")

# select the correct resistor for the 2700
daq.write("SOUR:CLOS (@101)") #select the 742A-1
time.sleep(1)

# Set the 5450A
resistor.write("Clear") # Clear the 5450A
time.sleep(1)
resistor.write("1")  # Set the 5450A to 1 Ohm

# Set the 8508A
dmm.write("*RST")  # Clear the 8508A
time.sleep(1)
dmm.write("VOLT:DC:Auto,Resl8,Fast_Off")  # Set the 8508A to DC Voltage
dmm.write("Inp:DIV_REAR") # Set the 8508A to Ratio mode (F/R)

# Set the 5700A
calibrator.write("Clear")  # Clear the 5700A
time.sleep(1)
calibrator.write("OUT 100 MA, CURR")