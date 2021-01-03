from customer import *

class RentalShop:
    def __init__(self):
        '''
        itialize the car pool
        '''
        self.cars = {
            "Hatchback":4,
            "Sedan":3, 
            "SUV": 3
        }


    def print_stock(self):
        '''
        show the available cars  in the pool
        '''
        count = 0
        for key, value in self.cars.items():
            if value > 0:
                count += 1
                print("There are {} {}".format(value, key))
                print("\tRent for less than a week: ${}".format(self.get_price(key, "short")))
                print("\tRent for a longer period: ${}".format(self.get_price(key, "long")))

        if count  == 0:
            print("Sorry,All cars are rented out!")


    def get_price(self, car, period, customer=None):
        '''
         Return different prices for different rental periods and for VIPs or not.
        '''
        if isinstance(customer, VIP):
            if car == "Hatchback":
                return 20
            elif car  == "Sedan":
                return 35
            else:
                return 80
        if period == "short":
            if car == "Hatchback":
                return 30
            elif car == "Sedan":
                return 50
            else:
                return 100
        else:
            if car == "Hatchback":
                return 25
            elif car == "Sedan":
                return 40
            else:
                return 90

    def rent_car(self, customer, car, day):
        if self.cars[car] > 0:
            self.cars[car] = self.cars[car] - 1
            customer.rent_car(car, day)
            print("Dear {},you has rent the {} for {} days".format(customer.name, car, day))
            return True
        else:
            print("No such type of car available now")
            return False


    def return_car(self, customer, car, day):
        if car not in self.cars:
            print("Sorry,this type is not rent in my shop")
            return False
        period = "long"
        if day < 7:
            period = "short"
        price = self.get_price(car, period, customer)
        total = price*day
        print("{} had rented the {} for {} days, You will be charged ${},We hope that you enjoy our service!".format(customer.name, car, day, total))
        print("The car has returned to the shop")
        self.cars[car] = self.cars[car] + 1
        customer.return_car()
        return True