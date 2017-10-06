# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"
class CandyShop(object):

    money = 0
    type_of_sweets = ""
    candy_storage = []

    def __init__(self, sugar):
        self.sugar = sugar
        
    def create_sweets(self, type_of_sweets):
        if self.type_of_sweets == "lollipop":
            self.sugar_needed = 5
            self.price_sale = 10
        if self.type_of_sweets == "candy":
            self.sugar_needed = 10
            self.price_sale = 20
        self.candy_storage.append(self.type_of_sweets)
        self.sugar == self.sugar - self.sugar_needed

    def buy_sugar(self, pack_sugar):
        self.price_sugar = 100
        self.money - self.price_sugar
        self.sugar + pack_sugar
        return self.sugar
    
    def sell(self):
        pass

    def raise_prices(self):
        pass

candy_shop = CandyShop(300)
#candy_shop.create_sweets("candy")
#candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
#candy_shop.create_sweets("lollipop")
print(candy_shop)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
#candy_shop.sell("candy", 1)
#print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 285gr"
#candy_shop.raise_prices(5)
#candy_shop.sell("lollipop", 1)
#print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:35, Sugar: 285gr"
candy_shop.buy_sugar(300)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:5, Sugar: 315gr"
