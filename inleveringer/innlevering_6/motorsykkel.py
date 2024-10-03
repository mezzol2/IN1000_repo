#Define a class motorsykkel that models riding a motorcycle
class Motorsykkel:
    #Define the instance variable
    def __init__(self, brand, registration) -> None:
        self._brand = brand
        self._registration = registration
        self._odometer = 0
    
    #Define a method that increases the odometer
    def kjor(self, km):
        self._odometer += km
    
    #Define a method that returns the number of kilometer on the odometer
    def hent_kilometerstand(self):
        return self._odometer

    #Define a method that prints the information on the motorcycle
    def skriv_ut(self):
        print(f"\nBrand: {self._brand}")
        print("Registration number: ", self._registration)
        print(f"Odometer: {self._odometer} km")