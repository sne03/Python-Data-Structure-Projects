import unittest

import MinimumSpanningTree
import self as self


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    G = {0: {1: 11, 2: 13, 3: 12}, 1: {0: 11, 3: 14}, 2: {0: 13, 3: 10}, 3: {0: 12, 1: 14, 2: 10}}
    T = [(2, 3), (0, 1), (0, 3)]
    for e, f in zip(MinimumSpanningTree(G), T):
        self.assertEqual(min(e), min(f))
        self.assertEqual(max(e), max(f))

if __name__ == '__main__':
    unittest.main()
