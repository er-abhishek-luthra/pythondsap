import unittest
from patterns._1_pattern_sliding_window._1_average_of_subarray_of_size_k import find_averages

class TestAverageOfSubarrayOfSizeK(unittest.TestCase):
    def test_find_averages(self):
        self.assertEqual(find_averages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]), [2.2, 2.8, 2.4, 3.6, 2.8])
        self.assertEqual(find_averages(3, [1, 2, 3, 4, 5]), [2.0, 3.0, 4.0])
        self.assertEqual(find_averages(1, [1, 2, 3, 4, 5]), [1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertEqual(find_averages(4, [1, 3, 2, 6, -1, 4, 1, 8, 2]), [3.0, 2.5, 2.75, 2.5, 3.0, 3.75])

if __name__ == '__main__':
    unittest.main()