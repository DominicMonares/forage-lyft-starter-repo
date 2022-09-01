import unittest

from car_parts.tires import CarriganTires, OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear = [0, 0, 0, 0.9]

        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear = [0.1, 0, 0.3, 0.7]

        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear = [1, 1, 0.1, 0.9]

        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear = [0.1, 0, 0.3, 0.7]

        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
