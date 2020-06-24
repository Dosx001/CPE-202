class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None] * table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered,
        and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted,
        and the value is used as the first line number in the list of line numbers.
        If the key is in the table, then the value is appended to that key’s list of line numbers.
        If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion,
        hash table size should be increased (doubled + 1)."""
        loc = self.horner_hash(key)
        if self.hash_table[loc] == None:
            self.hash_table[loc] = (key, {value})
            self.num_items += 1
        elif key == self.hash_table[loc][0]:
            self.hash_table[loc][1].add(value)
        else:
            if self.quad_probe(key, value, loc):
                self.num_items += 1
        if .5 < self.num_items / self.table_size:
            self.table_size *= 2
            self.table_size += 1
            storage = self.hash_table
            self.hash_table = [None] * self.table_size
            self.num_items = 0
            for key_value in storage:
                if key_value != None:
                    for value in key_value[1]:
                        self.insert(key_value[0], value)

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        return sum([ord(key[i]) * 31 ** (len(key) - 1 - i) for i in range(len(key) if len(key) < 9 else 8)]) % self.table_size
   
    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        loc = self.horner_hash(key)
        if self.hash_table[loc] == None:
            return False
        if self.hash_table[loc][0] == key:
           return True
        loc = self.quad_key_finder(key,loc)
        if loc == None:
            return False
        return True

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        loc = self.horner_hash(key)
        if self.hash_table[loc] == None:
            return None
        if self.hash_table[loc][0] == key:
            return loc
        loc = self.quad_key_finder(key, loc)
        if loc == None:
            return None
        return loc

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        return [i[0] for i in self.hash_table if i != None]

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        loc = self.horner_hash(key)
        if self.hash_table[loc] == None:
            return None
        if self.hash_table[loc][0] == key:
            return sorted(list(self.hash_table[loc][1]))
        loc = self.quad_key_finder(key, loc)
        if loc == None:
            return None
        return sorted(list(self.hash_table[loc][1]))

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size

    def quad_probe(self, key, value, loc, n=1):
        loc_q = (loc + n ** 2) % self.table_size
        if self.hash_table[loc_q] == None:
            self.hash_table[loc_q] = (key,{value})
            return True
        if self.hash_table[loc_q][0] == key:
            self.hash_table[loc_q][1].add(value)
            return False
        n+=1
        return self.quad_probe(key, value, loc, n)

    def quad_key_finder(self, key, loc, n=1):
        loc_q = (loc + n ** 2) % self.table_size
        if self.hash_table[loc_q] == None:
            return None
        if self.hash_table[loc_q][0] == key:
            return loc_q
        n+=1
        return self.quad_key_finder(key, loc, n)
