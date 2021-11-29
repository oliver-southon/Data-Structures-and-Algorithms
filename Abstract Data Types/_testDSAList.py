# DOUBLE LINKED LIST

# NOTE: This applies for DSAQueue

from dblDSAList import *
import unittest

ll = DSALinkedList()
ll.insertLast("2") # automatically tests insertLast here
ll.insertLast("3")
ll.insertLast("4")
ll.insertLast("5")

class TestDSAList(unittest.TestCase):
    def test_insertFirst(self):
        ll.insertFirst("1")
        result = "1 -> 2 -> 3 -> 4 -> 5 -> None"
        self.assertEqual(result, str(ll))

    def test_peekFirst(self):
        result = ll.peekFirst()
        self.assertEqual(result, "1")

    def test_peekLast(self):
        result = ll.peekLast()
        self.assertEqual(result, "5")

    def test_removeFirst(self):
        ll.removeFirst()
        result = "2 -> 3 -> 4 -> 5 -> None"
        self.assertEqual(result, str(ll))

    def test_removeLast(self):
        ll.removeLast()
        result = "2 -> 3 -> 4 -> None"
        self.assertEqual(result, str(ll))

if __name__ == "__main__":
    unittest.main()

    ll = DSALinkedList()