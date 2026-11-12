from entry import Entry

class HashMapping:
    """Implement the Mapping ADT with buckets, separate chaining, and rehashing"""
    def __init__(self, size=2):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        
    def put(self, key, value):
        """Add a new key value pair or update an existing keys value"""
        
        if self.count / self.size > 0.75:
            self.rehash()
        
        bucket_index = hash(key) % self.size
        bucket = self.buckets[bucket_index]
        
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
            
        bucket.append(Entry(key, value))
        self.count += 1
        
    def get(self, key):
        """Return the value associated with key, raise KeyError if not found"""
        bucket_index = hash(key) % self.size
        bucket = self.buckets[bucket_index]
        
        for entry in bucket:
            if entry.key == key:
                return entry.value
            
        raise KeyError(f"Key not found: {key}")
    
    def __contains__(self, key):
        """Return True when key is stored in the mapping; otherwise False"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
        
    def __len__(self):
        """Return the number of key-value pairs currently stored."""
        return self.count
    
    def rehash(self):
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        
        for bucket in old_buckets:
            for entry in bucket:
                self.put(entry.key, entry.value)