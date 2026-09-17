class ShoppingCart:
    """Represents cart customers put products into"""
    def __init__(self):
        """constructor for ShoppingCart class"""
        self.items = []
        
    def add_product(self, product):
        """Add product to items list"""
        self.items.append(product)
        
    def remove_product(self, product_id: str):
        """Find item in list remove if exists return true/false if successful"""
        for item in self.items:
            if item.get_id == product_id:
                self.items.remove(item)
        
    def get_items(self):
        """Return list of all items in cart"""
        return self.items
        
    def calculate_total(self) -> float:
        """returns total price of all items in cart"""
        total = 0
        for item in self.items:
            total += item.get_price()
            
        return total
        
    def is_empty(self):
        """return wether or not cart is empty"""
        if len(self.items) == 0:
            return True
        else:
            return False