"""
tests_1c.py

This module contains unit tests for the max subarray sums function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_positive_list():
    assert max_subarray_sum([2,6,2,8,1,7,5]) == 31
    assert max_subarray_sum([1,1,1,1,1]) == 5
    assert max_subarray_sum([100,5,6]) == 111

def test_mixed_list():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 4
    assert max_subarray_sum([-2,1,5,6,-7,8,1]) == 12
    assert max_subarray_sum([-5,6,1]) == 7

def edge_cases():
    assert max_subarray_sum([-1,-2,-3,-4,-5]) == -1
    assert max_subarray_sum([1]) == 1

if __name__ == "__main__":
    pytest.main()