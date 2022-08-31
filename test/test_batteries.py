import unittest
from datetime import datetime

from car_parts.batteries import NubbinBattery, SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced_4_yrs(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_be_serviced_5_yrs(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced_2_yrs(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_be_serviced_3_yrs(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()