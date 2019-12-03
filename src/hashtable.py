import hashlib
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # b_key = b
        # sha256_key = hashlib.sha256(key).hexdigest()
        # return sha256_key
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        '''
        hash_value = 5381
        # b_key = bkey
        # print(f"djb2 str(key): {str(key)}")
        new_key = str(key)

        for char in new_key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
            return hash_value

        '''
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        # print(f"_hash_mod key: {key}")
        # return self._hash(key) % self.capacity
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # new = LinkedPair(key, value) maybe ??
        # hash the key, put it in storage at hashed key?
        # print(f"key, value: {key, value}")
        index = self._hash_mod(key)
        # print(f"index: {index}")
        # print(f"self.count: {self.count}")
        # print(f"self.capacity: {self.capacity}")
        
        if self.count >= self.capacity:
            # resize
            # self.resize()
            return f"Error: hashtable at max capacity"

        if index > self.capacity:
            return f"Error: Out of range"

        self.storage[index] = value
        self.count += 1



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # print(f"self.storage before: {self.storage}")
        index = self._hash_mod(key)
        if index > self.count:
            return f"Error: Out of range"
        if index == None:
            return f"Error: Given key not found"
        # self.storage.remove(index)
        del self.storage[index]
        # print(f"self.storage after: {self.storage}")
        self.count -= 1
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)
        # if index == None:
        #     return f"Error: Given key not found"
        # return self.storage[index]
        return self.storage[self._hash_mod(key)]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]
            # new_storage.insert(i, self.storage[i])

        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")
    print(f"154 ht.storage: {ht.storage}")

    # Test storing beyond capacity
    print("r1", ht.retrieve("line_1"))
    print("r2",ht.retrieve("line_2"))
    print("r3",ht.retrieve("line_3"))

    # print(ht.remove("line_2"))
    print(f"162 ht.storage: {ht.storage}")


    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"170 ht.storage: {ht.storage}")


    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
