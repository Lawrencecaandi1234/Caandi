class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")


car1 = Car("Lamborghini", "Revuelto", 2025)
car2 = Car("Nissan", "GT-R", 2025)
car3 = Car("Honda", "Civic Type R", 2024)

print("Car 1 Details:")
car1.display_info()
print("\nCar 2 Details:")
car2.display_info()
print("\nCar 3 Details:")
car3.display_info()
