import pytest
from typing import List
from patterns._2_pattern_two_pointers._1_pair_with_target_sum import PairWithTargetSum  # Replace 'your_module' with the actual module name

def test_valid_pair():
    """Test case where a valid pair exists."""
    result = PairWithTargetSum.find_pair_with_target_sum([1, 2, 3, 4, 6], 6)
    assert result == (1, 3)  # Indices of 2 and 4

def test_no_pair():
    """Test case where no valid pair exists."""
    result = PairWithTargetSum.find_pair_with_target_sum([1, 2, 3, 4, 5], 10)
    assert result == (-1, -1)  # No pair found

def test_empty_array():
    """Test case for an empty array."""
    with pytest.raises(ValueError):
        PairWithTargetSum.find_pair_with_target_sum([], 5)

def test_single_element_array():
    """Test case for an array with a single element."""
    with pytest.raises(ValueError):
        PairWithTargetSum.find_pair_with_target_sum([1], 5)

def test_two_elements_with_pair():
    """Test case for an array with two elements that form a valid pair."""
    result = PairWithTargetSum.find_pair_with_target_sum([1, 2], 3)
    assert result == (0, 1)  # Indices of 1 and 2

def test_two_elements_without_pair():
    """Test case for an array with two elements that do not form a valid pair."""
    result = PairWithTargetSum.find_pair_with_target_sum([1, 2], 5)
    assert result == (-1, -1)  # No pair found

# To run the tests, use the command: pytest <filename>.py