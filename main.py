"""Name: Yijun Chen; UoBNo:lm20306; StudentID:2033739.
This is the main program to handle the whole process of renting a car.

"""



from rentalshop import RentalShop
from customer import Customer,VIP


def find_customer(customers, name):# Determine if the consumer has rented a car
    for customer in customers:
        if customer.name == name:
            return customer


def main():
    shop = RentalShop()
    customers = []
    while True:
        print("Menu:")
        print("1.View available stock")
        print("2.Rent one")
        print("3.Return the car")
        print("4.Quit")
        choice = input("Please enter your choice: ").strip()#Ensure that a single number is entered
        if choice == "1":
            shop.print_stock()
        elif choice == "2":
            name = input("Please enter your name: ")
            customer = find_customer(customers, name)
            if customer is None:
                vip = input("Are you a VIP?(Y|N) ")
                vip = vip.upper()
                if vip == "Y":
                    customer = VIP(name)
                else:
                    customer = Customer(name)
                customers.append(customer)
            if customer.car is not None:
                print("The customer {} had already rent a car".format(customer.name))
            else:
                car = input("Please choose the car type: ")
                while car not in ["Hatchback", "Sedan", "SUV"]:
                    print("The type you entered is not available,please re-enter your choice")
                    car = input("Please choose the car type: ")
                day = input("Please enter the number of days you would like to rent: ")
                while not day.isdigit():
                    print("Please enter a positive integer!")
                    day = input("Please enter the number of days you would like to rent: ")
                day = int(day)
                shop.rent_car(customer, car, day)
        elif choice == "3":
            name = input("Please enter your name: ")
            customer = find_customer(customers, name)
            if customer is None:
                print("The customer does not exist")
            else:
                if customer.car is None:
                    print("The customer {} did not rent a car.".formart(customer.name))
                else:
                    shop.return_car(customer, customer.car, customer.day)
        else:
            print("Bye!")
            break
        print()

''' 
For testing. When the module is run directly, the code will be run, when the module is imported, the code is not run.
'''
if __name__ == "__main__":
    main()
