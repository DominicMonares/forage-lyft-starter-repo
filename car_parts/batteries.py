from abc import ABC


class Battery(ABC):
    def needs_service(self):
        pass


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold = 365 * 4
        return (self.current_date - self.last_service_date).days > service_threshold


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold = 365 * 3
        return (self.current_date - self.last_service_date).days > service_threshold
