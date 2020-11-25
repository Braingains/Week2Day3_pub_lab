import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer_1 = Customer("Sandy", 10.00, 30, 0)
        self.customer_2 = Customer("Billy", 5.00, 12, 0)
        self.drink_1 = Drink("Tennants", 2.00, 2)
        self.drink_2 = Drink("Tennants_Super", 5.00, 20)

    # def test_pub_has_name(self):
    #     self.assertEqual("The Prancing Pony", self.pub.name)

    # def test_pub_takes_money(self):
    #     self.pub.sell_drink(self.drink_1, self.customer_1)
    #     self.assertEqual(102.00, self.pub.till)

    # def test_is_customer_old_enough(self):
    #     self.assertEqual(True, self.pub.check_customer_age(self.customer_1))

    # def test_is_customer_old_enough(self):
    #     self.assertEqual(False, self.pub.check_customer_age(self.customer_2))
        
    # def test_if_customer_is_too_drunk(self):
    #     self.assertEqual(True, self.pub.check_if_customer_is_too_drunk(self.customer))
    