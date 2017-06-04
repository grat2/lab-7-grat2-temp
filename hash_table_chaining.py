# a HashTable is a HashTable(positions)
class HashTable:
    def __init__(self, size = 8, keys = [None] * 8, data = [None] * 8):
        self.size = size # an integer
        self.keys = keys # list that contains keys of actual data
        self.data = data # list that contains actual data
    def __eq__(self, other):
        return (type(other) == HashTable
                and self.size == other.size
                and self.keys == other.keys
                and self.data == other.data)
    def __repr__(self):
        return "HashTable({!r}, {!r}, {!r})".format(self.size, self.keys, self.data)
    # key length ->

# None -> HashTable
# returns an empty HashTable
def empty_hash_table():
    return HashTable()

# HashTable key item -> HashTable
# inserts a value based on its hashed key value
def insert(h_t, key, item):
