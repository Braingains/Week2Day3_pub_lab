class Customer():

    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness


    def buy_drink(self, drink):
        if self.can_afford and self.age >= 18 and self.drunkenness < 10:
            self.wallet -= drink.price
            self.drunkenness += drink.alcohol_level 
        return False

    def buy_food(self, food):
        if self.can_afford:
            self.drunkenness -= food.rejuvination_level
            return True
        return False

    def can_afford(self, item):
        if self.wallet >= item.price:
            return True
        return False

    