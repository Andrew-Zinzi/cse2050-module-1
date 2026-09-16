

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