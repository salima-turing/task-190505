import pandas as pd
import unittest

class TestVectorizedOperations(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'radius': [1.0, 2.5, 3.3, 4.7, 5.1]})

    def test_vectorized_area_calculation(self):
        def calculate_area(radius):
            return 3.14 * radius * radius

        expected_area = pd.Series([3.14, 19.63, 34.29, 73.92, 81.61])
        actual_area = self.df['radius'].apply(calculate_area)

        # Set the precision for comparison
        precision = 0.01

        # Use assertAlmostEqual with a tolerance to compare the series
        for e, a in zip(expected_area, actual_area):
            self.assertAlmostEqual(e, a, places=precision, msg="Area calculation failed")

if __name__ == '__main__':
    unittest.main()
