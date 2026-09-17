import unittest
class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("1", "Febreeze", 2)
    def test_get_id(self):
        self.assertEqual("1", self.product.get_id())
    def test_get_name(self):
        self.assertEqual("Febreeze", self.product.get_name())
    def get_price(self):
        self.assertEqual(1, self.product.get_price())

class Product:
    def __init__(self, product_id: str, name: str, price: float):
        self.product = product_id
        self.names = name
        self.prices = price

    def get_id(self):
        return self.product

    def get_name(self):
        return self.names

    def get_price(self):
        return self.prices
if __name__ == "__main__":
    unittest.main()
    