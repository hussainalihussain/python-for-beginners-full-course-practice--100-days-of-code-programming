class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")


unknownVehicle = Vehicle()
car = Car()
bike = Bike()

unknownVehicle.start()
car.start()
bike.start()