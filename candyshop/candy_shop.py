# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the
# amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced
#  by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets
# and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar
# is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce
# the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"


class Sweets(object):
    def __init__(self, type_of_sweets):
        if type_of_sweets == "lollipop":
            self.sugar = 5
            self.price = 10
            self.name = type_of_sweets
        elif type_of_sweets == "candy":
            self.sugar = 10
            self.price = 20
            self.name = type_of_sweets


class CandyShop(object):

    candy_shop_storage = []
    income = 0

    def __init__(self, amount_sugar):
        self.amount_sugar = amount_sugar

    def create_sweets(self, type_of_sweets):
        self.candy_shop_storage.append(Sweets(type_of_sweets))
        self.amount_sugar -= self.candy_shop_storage[-1].sugar

    def raise_prices(self, percentage):
        for sweet in self.candy_shop_storage:
            sweet.price += sweet.price * (percentage / 100)

    def sweet_number_calculator(self, type_of_sweets):
        self.sweet_number = 0
        for sweet in self.candy_shop_storage:
            if sweet.name == type_of_sweets:
                self.sweet_number += 1
        return self.sweet_number

    def sell(self, type_of_sweets, amount):
        while amount > 0 and self.sweet_number_calculator(type_of_sweets) != 0:
            for i in range(len(self.candy_shop_storage)):
                if self.candy_shop_storage[i].name == type_of_sweets:
                    self.income += self.candy_shop_storage[i].price
                    del self.candy_shop_storage[i]
                    amount -= 1
                    break

    def buy_sugar(self, amount):
        self.amount_sugar += amount
        self.income -= (amount / 1000) * 100

    def __repr__(self):
        return "Inventory: {} candies, {}, lollipops, Income: {}, Sugar: {} gr".format(self.sweet_number_calculator("candy"), self.sweet_number_calculator("lollipop"), self.income, self.amount_sugar)  # nopep8


candy_shop = CandyShop(300)
candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")
print(candy_shop)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
candy_shop.sell("candy", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 285gr"
candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:35, Sugar: 285gr"
candy_shop.buy_sugar(300)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:5, Sugar: 315gr"
