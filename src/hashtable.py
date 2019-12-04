import hashlib
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return f"(Key: {self.key}, Value: {self.value}, Next: {self.next})"

    def __str__(self):
        return f"{self.value}"

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        #################
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        '''
        hash_value = 5381
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
        # print(f"index: {index}")
        # print(f"self.count: {self.count}")
        # print(f"self.capacity: {self.capacity}")

        index = self._hash_mod(key)
        item = self.storage[index]

        while item is not None and item.key != key:
            item = item.next

        if item is not None:
            item.value = value

        else:
            new_pair = LinkedPair(key, value)
            new_pair.next = self.storage[index]
            self.storage[index] = new_pair


        ###########################

        # index = self._hash_mod(key)
        # print(f"self.storage in insert: {self.storage}")

        # if self.count >= self.capacity:
        #     self.resize()
        # if self.storage[index] is not None:
        #     # print(f"Warning: Overwriting data at {index}")
        #     # chain here
        #     # print(f"self.storage[index - 1]: {self.storage[index - 1]}")
        #     if self.storage[index - 1] is not None:
        #         self.storage[index - 1].next = self.storage[index]
        #         return
        #     # while self.storage[index].next is not None
        #     # self.storage[index].value = value

        # self.storage[index] = LinkedPair(key, value)
        # self.count += 1

        ###################################

        # index = self._hash_mod(key)
        # if self.count >= self.capacity:
        #     # resize
        #     # self.resize()
        #     return f"Error: hashtable at max capacity"

        # if index > self.capacity:
        #     return f"Error: Out of range"

        # self.storage[index] = value
        # self.count += 1



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        if self.storage[index] is None:
            return f"Warning: Key not found"
        self.storage[index] = None
        self.count -= 1

        ##################################
        # # print(f"self.storage before: {self.storage}")
        # index = self._hash_mod(key)
        # if index > self.count:
        #     return f"Error: Out of range"
        # if index == None:
        #     return f"Error: Given key not found"
        # del self.storage[index]
        # # print(f"self.storage after: {self.storage}")
        # self.count -= 1
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        print(f"self.storage[index] in retrieve: {self.storage[index]}")
        if self.storage[index] is not None:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                # print(f"Warning: Key doesn't match")
                # return None
                # loop through the LL at this index?
                current = self.storage[index]
                print(f"current.key: {current.key}")
                print(f"key: {key}")
                print(f"current.next: {current.next}")
                while current.next is not None:
                    if current.key == key:
                        return self.storage[index].value
                    current = current.next
        else:
            return None

        # index = self._hash_mod(key)
        # if index == None:
        #     return f"Error: Given key not found"
        # return self.storage[index]
        # return self.storage[self._hash_mod(key)].value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for bucket_item in self.storage:
            if bucket_item is not None:
                new_index = self._hash_mod(bucket_item.key)
                new_storage[new_index] = LinkedPair(bucket_item.key, bucket_item.value)
        self.storage = new_storage

        #########################

        # self.capacity *= 2
        # new_storage = [None] * self.capacity

        # for i in range(self.count):
        #     new_storage[i] = self.storage[i]
        #     # new_storage.insert(i, self.storage[i])
        # self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print("r1: ", ht.retrieve("line_1"), "<-- should be 'Tiny hash table'")
    print("r2: ",ht.retrieve("line_2"), "<-- should be 'Filled beyond capacity'")
    print("r3: ",ht.retrieve("line_3"), "<-- should be 'Linked list saves the day!'")

    print(f"BEFORE resize ht.storage: {ht.storage}")

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))
    print("2r1: ", ht.retrieve("line_1"), "<-- should be 'Tiny hash table'")
    print("2r2: ",ht.retrieve("line_2"), "<-- should be 'Filled beyond capacity'")
    print("2r3: ",ht.retrieve("line_3"), "<-- should be 'Linked list saves the day!'")

    print(f"AFTER resize ht.storage: {ht.storage}")

    print("")
