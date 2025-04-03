import pytest
from patterns._1_pattern_sliding_window._1_average_of_subarray_of_size_k import find_averages

def test_average_of_subarrays():
    assert find_averages(3, [1, 3, 2, 6, -1, 4, 1, 8, 2]) == [2.0, 3.6666666666666665, 2.3333333333333335, 3.0, 1.3333333333333333, 4.333333333333333, 3.6666666666666665]

def test_empty_array():
    assert find_averages(3, []) == []

def test_k_greater_than_array_length():
    assert find_averages(5, [1, 2]) == []

def test_k_equals_zero():
    with pytest.raises(ValueError,match='K must be greater than 0'):
      find_averages(0, [1, 2, 3]) 

# To run the tests, use the command: pytest <filename>.py