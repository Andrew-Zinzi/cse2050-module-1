import unittest
from product import Product
from store import Store
from algorithms import merge_sort, quick_sort, quick_select
from hash_mapping import HashMapping



class TestMergeSort(unittest.TestCase):
    """Test suite for Merge Sort (Minimum 3 tests)."""

    def test_merge_sort_empty_or_single(self):
        """Test merge sort with empty and single-item product lists[cite: 13]."""
        empty_list = []
        merge_sort(empty_list)
        self.assertEqual(empty_list, [])

        single_list = [Product("P100", "Keyboard", 59.99)]
        merge_sort(single_list)
        self.assertEqual([p.get_id() for p in single_list], ["P100"])

    def test_merge_sort_reverse_order(self):
        """Test merge sort sorts a reverse-sorted product list in place[cite: 13]."""
        p1 = Product("P100", "Keyboard", 59.99)
        p2 = Product("P200", "Headphones", 39.99)
        p3 = Product("P300", "Mouse", 29.99)
        
        products = [p3, p2, p1]
        merge_sort(products)
        self.assertEqual([p.get_id() for p in products], ["P100", "P200", "P300"])

    def test_merge_sort_duplicates(self):
        """Test merge sort handles duplicate product IDs correctly[cite: 13]."""
        p1 = Product("P100", "Keyboard A", 59.99)
        p2 = Product("P100", "Keyboard B", 49.99)
        p3 = Product("P200", "Headphones", 39.99)
        
        products = [p3, p1, p2]
        merge_sort(products)
        self.assertEqual([p.get_id() for p in products], ["P100", "P100", "P200"])


class TestQuickSort(unittest.TestCase):
    """Test suite for Quick Sort (Minimum 3 tests)."""

    def test_quick_sort_empty_or_single(self):
        """Test quick sort with empty and single-item product lists[cite: 13]."""
        empty_list = []
        quick_sort(empty_list)
        self.assertEqual(empty_list, [])

        single_list = [Product("P100", "Keyboard", 59.99)]
        quick_sort(single_list)
        self.assertEqual([p.get_id() for p in single_list], ["P100"])

    def test_quick_sort_reverse_order(self):
        """Test quick sort sorts a reverse-sorted product list in place[cite: 13]."""
        p1 = Product("P100", "Keyboard", 59.99)
        p2 = Product("P200", "Headphones", 39.99)
        p3 = Product("P300", "Mouse", 29.99)
        
        products = [p3, p2, p1]
        quick_sort(products)
        self.assertEqual([p.get_id() for p in products], ["P100", "P200", "P300"])

    def test_quick_sort_duplicates(self):
        """Test quick sort handles duplicate product IDs correctly[cite: 13]."""
        p1 = Product("P100", "Keyboard A", 59.99)
        p2 = Product("P100", "Keyboard B", 49.99)
        p3 = Product("P200", "Headphones", 39.99)
        
        products = [p2, p3, p1]
        quick_sort(products)
        self.assertEqual([p.get_id() for p in products], ["P100", "P100", "P200"])


class TestQuickSelect(unittest.TestCase):
    """Test suite for QuickSelect (Minimum 3 tests)."""

    def setUp(self):
        self.p1 = Product("P100", "Keyboard", 59.99)
        self.p2 = Product("P200", "Headphones", 39.99)
        self.p3 = Product("P300", "Mouse", 29.99)
        self.products = [self.p3, self.p1, self.p2]

    def test_quick_select_first_rank(self):
        """Test quick select returns the smallest product (k=1)[cite: 10, 13]."""
        result = quick_select(self.products, 1)
        self.assertEqual(result.get_id(), "P100")

    def test_quick_select_middle_rank(self):
        """Test quick select finds a product at a middle rank[cite: 13]."""
        result = quick_select(self.products, 2)
        self.assertEqual(result.get_id(), "P200")

    def test_quick_select_invalid_rank(self):
        """Test quick select returns None for invalid ranks (k < 1 or k > len)[cite: 10, 13]."""
        self.assertIsNone(quick_select(self.products, 0))
        self.assertIsNone(quick_select(self.products, 5))


class TestHashMapping(unittest.TestCase):
    """Test suite for HashMapping, Entry, Collisions, and Rehashing (Minimum 3 tests)[cite: 13, 14]."""

    def test_hash_mapping_put_and_get(self):
        """Test basic putting and getting of key-value pairs[cite: 13]."""
        mapping = HashMapping(size=3)
        mapping.put("P100", "Keyboard")
        mapping.put("P200", "Headphones")
        
        self.assertEqual(mapping.get("P100"), "Keyboard")
        self.assertEqual(mapping.get("P200"), "Headphones")
        self.assertIn("P100", mapping)
        self.assertEqual(len(mapping), 2)

    def test_hash_mapping_update(self):
        """Test updating values for existing keys[cite: 13]."""
        mapping = HashMapping(size=3)
        mapping.put("P100", "Keyboard")
        mapping.put("P100", "Wireless Keyboard")
        
        self.assertEqual(mapping.get("P100"), "Wireless Keyboard")
        self.assertEqual(len(mapping), 1)  # Count should not increase on update

        # Test KeyError for missing key
        with self.assertRaises(KeyError):
            mapping.get("P999")

    def test_hash_mapping_collisions_and_rehash(self):
        """Test collision handling via separate chaining and automatic rehashing[cite: 13]."""
        # Using a tiny initial size to force collisions and rapid growth
        mapping = HashMapping(size=2)
        mapping.put("A", 10)
        mapping.put("D", 20)
        mapping.put("G", 30)
        mapping.put("J", 40)
        
        self.assertEqual(mapping.get("A"), 10)
        self.assertEqual(mapping.get("D"), 20)
        self.assertEqual(mapping.get("G"), 30)
        self.assertEqual(mapping.get("J"), 40)
        self.assertEqual(len(mapping), 4)


class TestStoreIntegration(unittest.TestCase):
    """Test suite for Store integration methods in Milestone 4 (Minimum 3 tests)[cite: 14]."""

    def setUp(self):
        self.store = Store()
        self.p1 = Product("P100", "Keyboard", 59.99)
        self.p2 = Product("P200", "Headphones", 39.99)
        self.p3 = Product("P300", "Mouse", 29.99)

    def test_store_sorting_integration(self):
        """Test store sorting wrapper methods call merge/quick sort correctly[cite: 11, 14]."""
        self.store.add_product(self.p3)
        self.store.add_product(self.p1)
        self.store.add_product(self.p2)
        
        self.store.merge_sort_products()
        self.assertEqual([p.get_id() for p in self.store.products], ["P100", "P200", "P300"])

        # Re-scramble and test quick sort integration
        self.store.products = [self.p3, self.p1, self.p2]
        self.store.quick_sort_products()
        self.assertEqual([p.get_id() for p in self.store.products], ["P100", "P200", "P300"])

    def test_store_quick_select_integration(self):
        """Test store quick select product method integration[cite: 11, 14]."""
        self.store.add_product(self.p3)
        self.store.add_product(self.p1)
        self.store.add_product(self.p2)
        
        result = self.store.quick_select_product(1)
        self.assertEqual(result.get_id(), "P100")

    def test_store_hash_lookup_integration(self):
        """Test store find_product uses HashMapping instead of linear scanning[cite: 11, 14]."""
        self.store.add_product(self.p1)
        self.store.add_product(self.p2)
        
        found = self.store.find_product("P200")
        self.assertIsNotNone(found)
        self.assertEqual(found.get_name(), "Headphones")
        
        missing = self.store.find_product("P999")
        self.assertIsNone(missing)


if __name__ == "__main__":
    unittest.main()