import unittest
from product import Product
from algorithms import *
from store import Store

class TestRecursionCatalogueTotal(unittest.TestCase):
    """Test suite for recursive catalog total (Minimum 2 tests)."""
    
    def test_recursive_total_empty_list(self):
        """Test recursive total with an empty product list returns 0.0."""
        products = []
        result = recursive_total_price(products)
        self.assertEqual(result, 0.0)    

    def test_recursive_total_multiple_products(self):
        """Test recursive total correctly sums multiple products."""
        p1 = Product("P100", "Keyboard", 59.99)
        p2 = Product("P200", "Headphones", 39.99)
        p3 = Product("P300", "Mouse", 29.99)
        
        products = [p1, p2, p3]
        excepted_total = 59.99 + 39.99 + 29.99
        
        result = recursive_total_price(products)
        self.assertEqual(result, excepted_total)
    
class TestFewestCoins(unittest.TestCase):
    """Test suite for fewest coins / change calculation (Minimum 3 tests)."""

    def test_fewest_coins_zero_amount(self):
        """Test fewest coins when amount is 0 returns 0."""
        coins = [1, 5, 10, 25]
        amount = 0
        result = fewest_coins(coins, amount)
        self.assertEqual(result, 0)

    def test_fewest_coins_exact_and_standard(self):
        """Test fewest coins with standard coin denominations."""
        coins = [1, 5, 10, 25]
        amount = 12
        result = fewest_coins(coins, amount)
        self.assertEqual(result, 3)

    def test_fewest_coins_memoized_and_impossible(self):
        """Test larger memoized amounts and impossible change cases."""
        coins = [1, 5, 10, 25]
        amount = 63
        result = fewest_coins(coins, amount)
        self.assertEqual(result, 6)
    
import unittest
from product import Product
from algorithms import bubble_sort, selection_sort, insertion_sort

class TestSortingAlgorithms(unittest.TestCase):
    """Test suite for the three quadratic sorting algorithms."""

    def setUp(self):
        """Set up standard unsorted, already sorted, and reverse sorted product lists."""
        self.p1 = Product("P100", "Keyboard", 59.99)
        self.p2 = Product("P200", "Headphones", 39.99)
        self.p3 = Product("P300", "Mouse", 29.99)

    def test_bubble_sort(self):
        """Test bubble sort sorts products in place by product ID."""
        products = [self.p3, self.p1, self.p2] # Unsorted
        bubble_sort(products)
        ids = [p.get_id() for p in products]
        self.assertEqual(ids, ["P100", "P200", "P300"])

    def test_selection_sort(self):
        """Test selection sort sorts products in place by product ID."""
        products = [self.p2, self.p3, self.p1] # Unsorted
        selection_sort(products)
        ids = [p.get_id() for p in products]
        self.assertEqual(ids, ["P100", "P200", "P300"])

    def test_insertion_sort(self):
        """Test insertion sort sorts products in place by product ID."""
        products = [self.p3, self.p2, self.p1] # Unsorted
        insertion_sort(products)
        ids = [p.get_id() for p in products]
        self.assertEqual(ids, ["P100", "P200", "P300"])

    def test_sorting_edge_cases(self):
        """Test sorting behavior with already-sorted and reverse-sorted lists."""
        sorted_list = [self.p1, self.p2, self.p3]
        insertion_sort(sorted_list)
        self.assertEqual([p.get_id() for p in sorted_list], ["P100", "P200", "P300"])

        reverse_list = [self.p3, self.p2, self.p1]
        bubble_sort(reverse_list)
        self.assertEqual([p.get_id() for p in reverse_list], ["P100", "P200", "P300"])
    
class TestBinarySearch(unittest.TestCase):
    """Test suite for binary search."""

    def setUp(self):
        """Set up a sorted list of products for binary search tests."""
        self.p1 = Product("P100", "Keyboard", 59.99)
        self.p2 = Product("P200", "Headphones", 39.99)
        self.p3 = Product("P300", "Mouse", 29.99)
        self.sorted_products = [self.p1, self.p2, self.p3]

    def test_binary_search_first_item(self):
        """Test binary search finding the first item in a sorted list."""
        index = binary_search(self.sorted_products, "P100")
        self.assertEqual(index, 0)

    def test_binary_search_middle_item(self):
        """Test binary search finding a middle item in a sorted list."""
        index = binary_search(self.sorted_products, "P200")
        self.assertEqual(index, 1)

    def test_binary_search_not_found(self):
        """Test binary search returns -1 when the product ID does not exist."""
        index = binary_search(self.sorted_products, "P999")
        self.assertEqual(index, -1)


class TestStoreIntegration(unittest.TestCase):
    """Test suite for Store integration methods."""

    def setUp(self):
        """Set up a sample Store instance and products for integration tests."""
        self.store = Store()
        self.p1 = Product("P100", "Keyboard", 59.99)
        self.p2 = Product("P200", "Headphones", 39.99)
        self.p3 = Product("P300", "Mouse", 29.99)

    def test_store_sorting_integration(self):
        """Test Store sorting wrapper methods correctly sort products in place."""
        self.store.add_product(self.p3)
        self.store.add_product(self.p1)
        self.store.add_product(self.p2)
        

        self.store.insertion_sort_products()
        ids = [p.get_id() for p in self.store.products]
        self.assertEqual(ids, ["P100", "P200", "P300"])

    def test_store_binary_lookup_integration(self):
        """Test Store binary search product lookup returns the Product or None."""
        self.store.add_product(self.p1)
        self.store.add_product(self.p2)
        self.store.add_product(self.p3)
        
        found = self.store.binary_search_product("P200")
        self.assertIsNotNone(found)
        self.assertEqual(found.get_name(), "Headphones")
        
        missing = self.store.binary_search_product("P999")
        self.assertIsNone(missing)

    def test_store_recursive_total_and_change_integration(self):
        """Test Store integration for recursive catalog total and change calculation."""
        self.store.add_product(self.p1)
        self.store.add_product(self.p2)
        
        # Test recursive catalog total integration[cite: 2, 3, 4]
        total = self.store.recursive_catalog_total()
        self.assertAlmostEqual(total, 99.98, places=2)
        
        # Test change calculation integration[cite: 2, 3, 4]
        coins = [1, 5, 10]
        change = self.store.calculate_change(coins, 12)
        self.assertEqual(change, 3)
    
if __name__ == "__main__":
    unittest.main()