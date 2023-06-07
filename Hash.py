# a hash table data structure is being created to hold the package data that are being loaded into a given delivery truck
# **!!CITATION!!** C950 - Webinar-1 - Let’s Go Hashing - Complete Python Code
# **!!ARTICLE LINK!!** https://srm--c.na127.visual.force.com/apex/coursearticle?Id=kA03x000000e1fuCAA
class hash_table_initiate:

    def __init__(self, capacity = 16):  # constructor and initialize the capacity of the trucks to be 16 (max truck load)
        self.list = []  # initializes an empty hash table
        for i in range(capacity):  # declare that the append will be with the range of the max capacity of a truck
            self.list.insert(i,[])  # insert the number of packages up to the amount of the capacity into the truck

    # private method to retrieve hash keys
    def get_hash_key(self, key):  # method that retrieves the hash key where an item will go
        return int(key) % len(self.list)

    # to insert an item into the hash table
    def insert_into_hash(self, key, value):
        while self.list[self.get_hash_key(key)] is None:  # while the hash table that stores the key is None
            self.list[self.get_hash_key(key)] = list([key, value])  # the initial value entered becomes the 1st hash key
            return True
        for dual_data in self.list[self.get_hash_key(key)]:  # hash table data comes in duals: key, data pointer
            while dual_data[0] == key:  # this is the hash key
                dual_data[1] = [key, value]  # this is the value that points to a data
                return True
        self.list[self.get_hash_key(key)].append([key, value])  # insert/add both the key and value to the hash table
        return True

    # lookup an item from the hash table based on the key entered
    def lookup_key(self, key):  # a search method that looks and pulls up the data
        for pair in self.list[hash(key) % len(self.list)]:  # using for loop to indicate the range of search
            while key == pair[0]:  # when they key entered matches the key in hash table
                return pair[1]  # pull up the value that's being pointed to by the hash key
        return None