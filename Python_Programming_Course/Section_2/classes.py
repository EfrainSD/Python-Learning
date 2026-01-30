class Vehicle:
    # Builder always like this, with 2 _ and the self argument
    def __init__(self, color, maxSpeed, brand):
        self.color = color
        self.speed = 0
        self.maxSpeed = maxSpeed
        self.brand = brand
        # IMPORTANT: If we put the names of the attributes with __ (double _), we force the attributes to only be changeable from within the class,
        # not from outside with an assignment. In other words, they can only be changed with a setter.
    
    # Inside the class you can have variables
    variable = 0
        
    # You can create son functions inside the class
    def start(self):
        print("Started")
    def accelerate(self):
        if self.speed == 0:
            self.speed = 10
        else:
            self.speed = self.speed + 10
        print("Speed = " + str(self.speed))
    def brake(self):
        if self.speed > 10:
            self.speed = self.speed - 10
        else:
            self.speed = 0
        print("Speed = " + str(self.speed))
    def getInfo(self):
        print(f"COLOR: {self.color} MAXSPEED: {self.maxSpeed} BRAND: {self.brand}")
        
    # You can create getters
    def getColor(self):
        return self.color
    
    # Or setters
    def setColr(self, color):
        self.color = color
        
# How to call our class -> Instance of our class
myVehicule = Vehicle("red", 120, "seat")
print(myVehicule.variable) # You can just access to a variable like that
myVehicule.start()
myVehicule.accelerate()
myVehicule.getInfo()

# Inheritance
class Moto(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self, color, maxSpeed, brand, tires=4):
        super().__init__(color, maxSpeed, brand)
        self.tires = tires
    
    def getInfo(self):
        print(f"COLOR: {self.color} MAXSPEED: {self.maxSpeed} BRAND: {self.brand} TIRES: {self.tires}")
        
myCar = Car("blue", 130, "kia", 4)
myCar.getInfo()

# Multiple Inheritance
class Transport:
    def __init__(self, capacity):
        self.capacity = capacity
        
class Truck(Vehicle, Transport):
    def __init__(self, color, maxSpeed, brand, capacity, load):
        Vehicle.__init__(color, maxSpeed, brand)
        Transport.__init__(self, capacity)
        self.load = load