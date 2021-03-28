from DSAQueue import DSAShuffleQueue
import unittest
from DSAQueue import *
import numpy as np

class TestDSAQueue(unittest.TestCase):
    def test_isEmpty(self):
        test = DSAQueue()
        result = test.isEmpty()
        self.assertEqual(result, True)

    def isFull(self):
        test = DSAQueue()
        result = test.isFull()
        self.assertEqual(result, False)
        test.set_default_capacity(0)
        result = test.isFull()
        self.assertEqual(result, True)

    def test_shuffle_enqueue(self): # also tests peek
        test = DSAShuffleQueue()
        test.enqueue(1)
        result = test.peek()
        self.assertEqual(result, 1)

    def test_circular_enqueue(self): # also tests peek
        test = DSACircularQueue()
        test.enqueue(1)
        result = test.peek()
        self.assertEqual(result, 1)

    def test_shuffle_dequeue(self):
        test = DSAShuffleQueue()
        test.set_default_capacity(3)
        test.enqueue(1)
        test.enqueue(2)
        test.enqueue(3)
        test.dequeue()

        testQueue = []
        for el in test.queue:
            testQueue.append(el)

        testArr = [2, 3, None]
        result = (testArr == testQueue)
        self.assertEqual(result, True)

    def test_shuffle_dequeue(self):
        Q = DSACircularQueue()
        Q.set_default_capacity(3)
        Q.enqueue(1)
        Q.enqueue(2)
        Q.enqueue(3)
        Q.dequeue()
        Q.enqueue(1)

        testQueue = []
        for el in Q.queue:
            testQueue.append(el)

        testArr = [1, 2 ,3]
        result = (testArr == testQueue)
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()

