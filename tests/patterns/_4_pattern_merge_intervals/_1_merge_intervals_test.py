import pytest
from patterns._4_pattern_merge_intervals._1_merge_intervals import Interval, merge_intervals

def test_no_intervals():
    assert merge_intervals([]) == []

def test_single_interval():
    intervals = [Interval(1, 3)]
    assert merge_intervals(intervals) == [Interval(1, 3)]

def test_non_overlapping_intervals():
    intervals = [Interval(1, 2), Interval(3, 4), Interval(5, 6)]
    assert merge_intervals(intervals) == [Interval(1, 2), Interval(3, 4), Interval(5, 6)]

def test_overlapping_intervals():
    intervals = [Interval(1, 3), Interval(2, 4), Interval(5, 7), Interval(6, 8)]
    assert merge_intervals(intervals) == [Interval(1, 4), Interval(5, 8)]

def test_all_intervals_overlapping():
    intervals = [Interval(1, 4), Interval(2, 5), Interval(3, 6)]
    assert merge_intervals(intervals) == [Interval(1, 6)]

def test_mixed_intervals():
    intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18), Interval(17, 20)]
    assert merge_intervals(intervals) == [Interval(1, 6), Interval(8, 10), Interval(15, 20)]

# To run the tests, use the command: pytest <filename>.py