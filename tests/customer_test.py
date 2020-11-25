import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Sandy", 10.00)
        self.drink = Drink("Tennants", 2.00)

    def test_customer_has_name(self):
        self.assertEqual("Sandy", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    # def test_can_buy_drink(self):
    #     self.customer.buy_drink(drink)
    #     self.assertEqual(18, self.customer.wallet)
