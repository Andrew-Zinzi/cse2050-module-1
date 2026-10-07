from Customer import Customer
from Product import Product
class Order():
    def __init__(self, order_id: str, customer: Customer, items: list[Product], status = "PENDING"):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.status = status
    
    def get_id(self):
        return self.order_id

    def get_customer(self):
        return self.customer

    def get_items(self):
        return self.items

    def get_status(self):
        return self.status

    def set_status(self, status: str):
        self.status = status


    def calculate_total(self):
        total = 0

        for p in self.items:
            total += p.get_price()
        return total

