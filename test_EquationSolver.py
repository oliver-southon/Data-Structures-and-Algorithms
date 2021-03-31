import unittest
from EquationSolver import *

class TestDSAQueue(unittest.TestCase):
    def test_solve(self):
        test = EquationSolver()
        result = test.solve("( 10.3 * ( 14 + 3.2 ) ) / ( 5 + 2 - 4 * 3 )")
        self.assertEqual(result, -35.432)

        test = EquationSolver()
        result = test.solve("( 5 / ( 3 - 1.5 ) ) * ( 8 + 2 - 1 / 5 )")
        self.assertEqual(result, 32.6667)

        test = EquationSolver()
        result = test.solve("( 8 + 2 / 3 ) * ( 2 + 4 - 3 / 2 )")
        self.assertEqual(result, 39)

if __name__ == "__main__":
    unittest.main()


