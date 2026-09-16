

class Store:

    def __init__(self):
        """constructor for Store class"""
        self.products = []
        self.customers = []
    
    def add_product(self, product: Product):
        """Add product to products list if not already in list

        Args:
            product (Product): instance of product class

        Returns:
            bool: was product added to list, returns true if successful or false if not successful
        """
        if product.id in self.products:
            return False
        else:
            self.products.append(product.id)
            return True
    
    def find_product(self, product: Product):
        """Find product in products list

        Args:
            product (Product): instance of product class

        Returns:
            bool, Product: returns false if not in list, returns instance of product if in list 
        """
        if product.id in self.products:
            return product
        else:
            return None
    
    def add_customer(self, customer: Customer):
        """Add customer to customer list

        Args:
            customer (Customer): instance of customer class 

        Returns:
            bool: was customer added to list, returns true if successful or false if not successful
        """
        if customer.id in self.customers:                
            return False
        else:
            self.customers.append(customer.id)
            return True
        
    def find_customer(self, customer: Customer):
        """Find customer in customers list 

        Args:
            customer (Customer): instance of customer class

        Returns:
            bool, Customer: returns false if not in list, returns instance of customer if in list
        """
        if customer.id in self.customers:
            return customer
        else:
            return None