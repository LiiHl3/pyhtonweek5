class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_percent):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_percent = battery_percent

    def make_call(self, number):
        if self.battery_percent > 0:
            print(f"Calling {number} from {self.brand} {self.model}...")
            self.battery_percent -= 5
        else:
            print("Battery is dead. Please charge your phone.")

    def charge(self, amount):
        self.battery_percent = min(100, self.battery_percent + amount)
        print(f"Charging... Battery is now at {self.battery_percent}%")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage_gb}GB storage and {self.battery_percent}% battery"

# Subclass that inherits from Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_percent, cooling_system):
        super().__init__(brand, model, storage_gb, battery_percent)
        self.cooling_system = cooling_system

    # Polymorphism: Override make_call to simulate gaming mode
    def make_call(self, number):
        print("Sorry, gaming mode is ON. Can't make calls now.")

    def activate_cooling(self):
        print(f"Activating {self.cooling_system} cooling system to prevent overheating.")

# Create objects
phone1 = Smartphone("Apple", "iPhone 14", 128, 80)
phone2 = GamingSmartphone("ASUS", "ROG Phone 6", 256, 60, "Liquid Cooling")

# Use methods
print(phone1)
phone1.make_call("123-456-7890")
phone1.charge(15)

print("\n" + str(phone2))
phone2.make_call("987-654-3210")  # Overridden method
phone2.activate_cooling()
phone2.charge(30)