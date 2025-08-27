# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Child class (inherits Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)   # Inheriting from Device
        self.os = os
        self.storage = storage
    
    # Encapsulation: controlled access to storage
    def upgrade_storage(self, extra):
        self.storage += extra
        print(f"Storage upgraded! Now you have {self.storage}GB.")

    # A method unique to Smartphone
    def call(self, number):
        print(f"Calling {number}... 📞")


# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S23", "Android", 128)
phone2 = Smartphone("Apple", "iPhone 14", "iOS", 256)

print(phone1.info())   # From parent class
phone1.call("0712345678")
phone1.upgrade_storage(128)
