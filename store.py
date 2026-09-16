

class Store:

    def __init__(self):
        self.products = []
        self.customers = []
    
    def add_product(self, product: Product):
        if product.id in self.products:
            return False
        else:
            self.products.append(product.id)
            return True
    
    def find_product(self, product: Product):
        if product.id in self.products:
            return product
        else:
            return None
    
    def add_customer(self, customer: Customer):
        if customer.id in self.customers:                
            return False
        else:
            self.customers.append(customer.id)
            return True
        
    