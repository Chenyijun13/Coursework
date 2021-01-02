class Customer:     #define customer class, with two actions,renting and returning a car
    def __init__(self, name):
        self.name = name
        self.car =  None
        self.day = 0

    def rent_car(self, car, day):
        self.car = car
        self.day = day

    def return_car(self):
        self.car = None
        self.day = 0




