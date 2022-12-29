import unittest
import add_func

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add_func.add(10, 15), 15)

if __name__ == '__main__':
    unittest.main()