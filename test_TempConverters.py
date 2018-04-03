# test_TempConverters.py
# Tests Temp Converter functions

import unittest
import TempConverters

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription
    def test_fahrenheitToCelsius_for212F(self):
        # Capture the results of the function
        result = TempConverters.fahrenheitToCelsius(212)
        # Check for expected output
        self.assertEqual(100.0, result)

    def test_fahrenheitToCelsius_for32F(self):
        # Capture the results of the function
        result = TempConverters.fahrenheitToCelsius(212)
        # Check for expected output
        self.assertEqual(0.0, result)

    def test_fahrenheitToCelsius_for5F(self):
        # Capture the results of the function
        result = TempConverters.fahrenheitToCelsius(5)
        # Check for expected output
        self.assertEqual(-15.0, result)
    
    def test_fahrenheitToCelsius_for50F(self):
        # Capture the results of the function
        result = TempConverters.fahrenheitToCelsius(50)
        # Check for expected output
        self.assertEqual(40.0, result)

    def test_celsiusToFahrenheit_for0C(self):
        # Capture the results of the function
        result = TempConverters.celsiusToFahrenheit(0)
        # Check for expected output
        self.assertEqual(32.0, result)

    def test_celsiusToFahrenheit_for100C(self):
        # Capture the results of the function
        result = TempConverters.celsiusToFahrenheit(100)
        # Check for expected output
        self.assertEqual(212.0, result)

    def test_celsiusToFahrenheit_for55C(self):
        # Capture the results of the function
        result = TempConverters.celsiusToFahrenheit(55)
        # Check for expected output
        self.assertEqual(131.0, result)
        

    def test_celsiusToFahrenheit_forMinus50C(self):
        # Capture the results of the function
        result = TempConverters.celsiusToFahrenheit(-50)
        # Check for expected output
        self.assertEqual(-58.0, result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
