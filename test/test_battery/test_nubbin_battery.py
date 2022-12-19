import unittest
from datetime import datetime

from batteries.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced_after_5_years(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def battery_should_not_be_serviced_after_2_years(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0

        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()