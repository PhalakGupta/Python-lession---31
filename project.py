class Cars:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def detail(self):
        return f"Fuel Type: {self.fuel_type}, Max Speed: {self.max_speed}"


class BMW(Cars):
    def __init__(self):
        super().__init__("Premium Gasoline", "307 km/hr")


class Ferrari(Cars):
    def __init__(self):
        super().__init__("Premium Fuel", "355 km/hr")


# Create objects and display details
cars = [BMW(), Ferrari()]
for car in cars:
    print(car.detail())