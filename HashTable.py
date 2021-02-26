from LinkedList import LinkedList

# Shout out to Jordan and Brian!!


class HashTable:

    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    # 1️⃣ TODO: Complete the create_arr method.

    # Each element of the hash table (arr) is a linked list.
    # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

    def create_arr(self, size):
        arr = []

        for i in range(size):
            new_ll = LinkedList()
            arr.append(new_ll)

        return arr

    # 2️⃣ TODO: Create your own hash function.

    # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored.

    def hash_func(self, key):
        # 1. Get the first letter of the key and lower case it
        first_letter = key[0].lower()

        # 2. Calculate the distance from letter a
        distance_from_a = ord(first_letter) - ord('a')

        # 3. Mod it to make sure it is in range
        index = distance_from_a % self.size

        # returns index
        return index

    # 3️⃣ TODO: Complete the insert method.

    # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

    def insert(self, key, value):
        # Find the index where the key value should be placed
        key_hash = self.hash_func(key)
        new_tuple = (key, value)
        # If the find method returns -1, it's empty so create a new tuple and append to the hash table
        if self.arr[key_hash].find(new_tuple) == -1:
            self.arr[key_hash].append(new_tuple)
        # Else if we find an existing tuple, add one to the frequency and return the key hash
        elif self.arr[key_hash].find(new_tuple) == True:
            return self.arr[key_hash]

    # 4️⃣ TODO: Complete the print_key_values method.

    # Traverse through the every Linked List in the table and print the key value pairs.

    # For example:
    # a: 1
    # again: 1
    # and: 1
    # blooms: 1
    # erase: 2

    def print_key_values(self):

        if self.size == None:
            print("empty")
            return -1
        else:
            for i in self.arr:
                i.print_nodes()
