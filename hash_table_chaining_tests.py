import unittest
from hash_table_chaining inport *

class TestCase(unittest.TestCase):

    def test_classes(self):
        self.assertEqual(empty_hash_table(), HashTable(8, 0, [[] for i in range(8)], 0))
        self.assertEqual(repr(empty_hash_table()), "HashTable({!r}, {!r}, {!r}, {!r})".format(8, 0, [[] for a in range(8)], 0))
        self.assertEqual(Entry(5, 0), Entry(5, 0))
        self.assertEqual(repr(Entry(5, 0)), "Entry({!r}, {!r})".format(5, 0))


if(__name__ == '__main__'):
    unittest.main()
