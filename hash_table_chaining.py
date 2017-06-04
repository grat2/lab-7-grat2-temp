# a HashTable is a HashTable(positions)
class HashTable:
    def __init__(self, size = 8, slots = [None] * 8, data = [None] * 8, hashFunc = None):
        self.size = size # an integer
        self.slots = slots # 
        self.data = data
    def __eq__(self, other):
        return (type(other) == HashTable
                and self.size == other.size
                and self.slots == other.slots
                and self.data == other.data)
    def __repr__(self):
        return "HashTable({!r}, {!r}, {!r})".format(self.size, self.slots, self.data)

# None -> HashTable
# returns an empty HashTable
def empty_hash_table():
    return HashTable()

# HashTable key item
