import pandas as pd
import unittest

class TestVectorizedOperations(unittest.TestCase):

    def setUp(self):
        # Fixture function to set up the test DataFrame
        self.df = pd.DataFrame({'radius': [1.0, 2.5, 3.3, 4.7, 5.1]})

    def test_vectorized_area_calculation(self):
        # Function to perform vectorized area calculation
        def calculate_area(radius):
            return 3.14 * radius * radius

        # Expected output series
        expected_area = pd.Series([3.14, 19.63, 34.29, 73.92, 81.61])

        # Perform vectorized operation
        actual_area = self.df['radius'].apply(calculate_area)

        # Assertion to compare expected and actual output
        self.assertTrue(expected_area.equals(actual_area), "Area calculation failed")

if __name__ == '__main__':
    unittest.main()
