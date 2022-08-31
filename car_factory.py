from car import Car
from car_parts.batteries import NubbinBattery, SpindlerBattery
from car_parts.engines import CapuletEngine, SternmanEngine, WilloughbyEngine


class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            battery = SpindlerBattery(current_date, last_service_date),
            engine = CapuletEngine(last_service_mileage, current_mileage)
        )

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            battery = SpindlerBattery(current_date, last_service_date),
            engine = WilloughbyEngine(last_service_mileage, current_mileage)
        )

    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(
            battery = SpindlerBattery(current_date, last_service_date),
            engine = SternmanEngine(warning_light_on)
        )

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            battery = NubbinBattery(current_date, last_service_date),
            engine = WilloughbyEngine(last_service_mileage, current_mileage)
        )

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            battery = NubbinBattery(current_date, last_service_date),
            engine = CapuletEngine(last_service_mileage, current_mileage)
        )
