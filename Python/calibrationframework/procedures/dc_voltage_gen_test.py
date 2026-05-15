import time

def dc_voltage_test(dmm, source):

    test_points = [0.1, 1, 10, 100]

    results = []

    source.output_on()

    for point in test_points:

        print(f"\nApplying {point} V")

        source.set_voltage(point)

        time.sleep(2)

        reading = dmm.measure_dc_voltage()

        error = reading - point

        result = {
            "applied": point,
            "measured": reading,
            "error": error
        }

        results.append(result)

        print(result)

    source.output_off()

    return results