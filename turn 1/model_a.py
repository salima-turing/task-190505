import pandas as pd
import pytest

@pytest.fixture
def sample_data():
	data = {
		"age": [20, 30, 40, 50, 60],
		"salary": [50000, 60000, 70000, 80000, 90000]
	}
	return pd.DataFrame(data)

def test_vectorized_addition(sample_data):
	# Vectorized addition of a constant to a column
	expected_result = pd.Series([25000, 66000, 77000, 88000, 99000])
	result = sample_data["salary"] + 20000

	pd.testing.assert_series_equal(result, expected_result, check_names=False)

if __name__ == "__main__":
	pytest.main()
