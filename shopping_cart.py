class ShoppingCart:
    """Represents cart customers put products into"""
    def __init__(self):
        """constructor for ShoppingCart class"""
        self.items = []
        
    def add_product(self, product):
        self.items.append(product)
        
    def remove_product(self, product_id: str):
        for item in self.items:
            if item.get_id == product_id:
                self.items.remove(item)
        
    def get_items(self):
        return self.items
        
    def calculate_total(self) -> float:
        total = 0
        for item in self.items:
            total += item.get_price()
            
        return total
        
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False