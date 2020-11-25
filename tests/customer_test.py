import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Sandy", 10.00, 40, 0)
        self.customer_2 = Customer("Billy", 5.00, 12, 0)
        self.customer_3 = Customer("Ewan", 4.00, 30, 10)
        self.drink_1 = Drink("Tennants", 2.00, 2)
        self.drink_2 = Drink("Tennants_Super", 5.00, 20)
        self.food_1 = Food("Wasabi_Peas", 2, 1)

    def test_customer_has_name(self):
        self.assertEqual("Sandy", self.customer_1.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer_1.wallet)

    def test_can_buy_drink(self):
        self.customer_1.buy_drink(self.drink_1)
        self.assertEqual(8, self.customer_1.wallet)

    def test_can_underager_buy_drink(self):
        self.assertEqual(False, (self.customer_2.buy_drink(self.drink_1)))

    def test_customer_can_afford_drink(self):
        self.assertEqual(self.customer_1.can_afford(self.drink_1), True)

    def test_customer_cannot_afford_drink(self):
        self.assertEqual(self.customer_3.can_afford(self.drink_2), False)

    def test_does_customers_drunkenness_increase(self):
        self.customer_1.buy_drink(self.drink_1)
        self.assertEqual(2, self.customer_1.drunkenness)

    def test_is_wasted_person_refused_service(self):
        self.assertEqual(False, (self.customer_3.buy_drink(self.drink_2)))

    def test_customer_can_buy_food(self):
        self.assertEqual(True, (self.customer_1.buy_food(self.food_1)))
        
    def test_food_rejuvinates_customer(self):
        self.customer_3.buy_food(self.food_1)
        self.assertEqual(9, self.customer_3.drunkenness)

          
