import unittest
from DSAStack import *
import numpy as np

test1 = DSAStack()
test1.push(1)
test1.push(2)
test1.push(3)
test1.push(4)
test1.push(5)
test2 = DSAStack()

class TestDSAStack(unittest.TestCase):
    def test_getCount(self):
        result = test1.count
        self.assertEqual(result, 5)
        result = test2.count
        self.assertEqual(result, 0)

    def test_isEmpty(self):
        result = test1.isEmpty()
        self.assertEqual(result, False)
        result2 = test2.isEmpty()
        self.assertEqual(result2, True)

    def test_isFull(self):
        result = test1.isFull()
        self.assertEqual(result, False)
        test1.default_cap = 5
        result = test1.isFull()
        self.assertEqual(result, True)
        test1.default_cap = 100 # set back to default
    
    def test_pop(self):
        result = test1.pop()
        self.assertEqual(result, 5)
        result = test2.pop()
        self.assertEqual(result, None)



if __name__ == "__main__":
    unittest.main()

    # COMMENT OUT Line 41 to run the below code... ---- tests push and top methods
    my_test = DSAStack()
    print("Top value is: " + str(my_test.top()) + '\n')
    my_test.push(1)
    print("Adding 1")
    print("Top value is now: " + str(my_test.top()))
