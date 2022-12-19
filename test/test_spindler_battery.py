import unittest
from datetime import datetime

from batteries.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced_after_3_years(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def battery_should_not_be_serviced_after_1_years(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()