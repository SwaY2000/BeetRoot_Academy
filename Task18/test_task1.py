import unittest
import task1

class Test_task1(unittest.TestCase):

    def test_SQUARE(self):
        self.assertEqual(task1.square_nums([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])
        with self.assertRaises(TypeError):
            task1.square_nums(["g", 2, 3, 4, 5])
        self.assertEqual(task1.square_nums([-1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_negative(self):
        self.assertEqual(task1.remove_negatives([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(task1.remove_negatives([-11, 2, 3, 4, 5]), [2, 3, 4, 5])
        with self.assertRaises(TypeError):
            task1.remove_negatives(["t", 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()