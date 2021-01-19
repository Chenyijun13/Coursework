"""
Name: Yijun Chen; UoBNo:lm20306; StudentID:2033739.
This code is used to check the availability of the program
when incorrect values and information are entered

"""

import unittest
from rentalshop import *
from customer import *

class TestCarRental(unittest.TestCase):

    def test_rent_car_with_negative_days(self):
        shop = RentalShop()
        customer = Customer("Jim")
        self.assertEqual(shop.rent_car(customer, "Hatchback", -1), True)
        shop.cars["Hatchback"] = 0
        self.assertEqual(shop.rent_car(customer, "Hatchback", -1), False)

    def test_return_car(self):
        shop = RentalShop()
        customer = Customer("Jim")
        shop.rent_car(customer, "Hatchback", 10)
        self.assertEqual(shop.return_car(customer, "Hatchback", 10),  True)

    def test_return_empty_car(self):
        shop = RentalShop()
        customer = Customer("Jim")
        shop.rent_car(customer, "Hatchback", 10)
        self.assertEqual(shop.return_car(customer, "", 10),  False)

if __name__ == '__main__':  
    unittest.main()
