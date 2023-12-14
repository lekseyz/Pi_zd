import unittest
import main as module

class Testing(unittest.TestCase):
    def test_sum(self):
        self.assertTrue(module.sum(2, 2) == 4, "must be 4")
        self.assertTrue(module.sum(2, 1) == 3, "must be 3")
        self.assertTrue(module.sum(-1, 2) == 1, "must be 1")
        self.assertTrue(module.sum(2, 100) == 102, "must be 102")


if __name__ == '__main__':
    unittest.main()