import time

def fluke5450a_drift_test(daq, dmm, calibrator, resistor):
    """
    Test the drift of Fluke 5450A resistance calibrator.
    
    Args:
        daq: Keithley2700 data acquisition unit
        dmm: Fluke8508A multimeter
        calibrator: Fluke5700A voltage calibrator
        resistor: Fluke5450A resistance calibrator
    
    Returns:
        List of measurement results
    """
    print("Connect 5450A in series with the 2700's 742A and the 5700A, "
          "connect the sense leads of the 2700 to the rear of "
          "the 8508A and connect the front sense connectors to "
          "the front input of the 8508A.")
    
    results = []
    
    # Select the correct resistor for the 2700 (742A-1)
    print("\nSelecting 742A-1 channel...")
    daq.select_channel(101)
    time.sleep(1)
    
    # Clear and set the 5450A to 1 Ohm
    print("Setting 5450A to 1 Ohm...")
    resistor.clear()
    time.sleep(1)
    resistor.set_resistance(1)
    
    # Reset and configure the 8508A
    print("Configuring 8508A...")
    dmm.reset()
    time.sleep(1)
    dmm.measure_dc_voltage()
    dmm.set_ratio_mode(front_rear=True)
    
    # Configure the 5700A calibrator
    print("Configuring 5700A calibrator...")
    calibrator.reset()
    time.sleep(1)
    calibrator.set_voltage(100)
    calibrator.output_on()
    
    print("\nDrift test started...")
    time.sleep(2)
    
    # Perform ratio measurements over time
    test_duration = 300  # 5 minutes in seconds
    measurement_interval = 30  # Measure every 30 seconds
    
    elapsed_time = 0
    while elapsed_time < test_duration:
        reading = dmm.measure_ratio()
        result = {
            "elapsed_time": elapsed_time,
            "reading": reading
        }
        results.append(result)
        print(f"Time: {elapsed_time}s - Ratio: {reading}")
        
        time.sleep(measurement_interval)
        elapsed_time += measurement_interval
    
    # Clean up
    calibrator.output_off()
    
    return results
