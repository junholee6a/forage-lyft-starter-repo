import unittest

from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires_wear = [0.8, 0.8, 0.8, 0.8] # sum: 3.2

        tires = OctoprimeTires(tires_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires_wear = [0.8, 0.5, 0.1, 0.6]  # sum: 2.0

        tires = OctoprimeTires(tires_wear)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()