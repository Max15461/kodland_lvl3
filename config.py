token = ''

class Car:

    def __init__(self, year, color, car_brand = "mercedes"):
        self.year = year
        self.color = color
        self.car_brand = car_brand
       

    def info(self):
        return (
            f"Year of car: {self.year}\n"
            f"Color: {self.color}\n"
            f"Car brand: {self.car_brand}"
        )


