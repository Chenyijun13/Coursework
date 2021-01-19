"""Name: Yijun Chen; UoBNo:lm20306; StudentID:2033739.
This code is used to check the availability of the program
when incorrect values and information are entered

"""

Customer_Class in Part1,
define customer class with two actions,
renting and returning a car.



class Customer:     
    #Initialized with three parameters: customer name, rental time and type of car
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

class VIP(Customer):
    def __init__(self, name):
        Customer.__init__(self, name)
'''
Inherit the methods of the parent class and define the price separately at the calculates function.
'''



