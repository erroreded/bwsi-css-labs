"""
tests_1d.py

This module contains unit tests for the two_sums function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_normal():
    assert two_sum([2, 7, 11, 15],9) == [0,1]
    assert two_sum([2, 7, 11, 15],17) == [0,3]
    assert two_sum([2, 7, 11, 15],26) == [2,3]


def test_zero():
    assert two_sum([0, 7, 6],6) == [0,2]
    assert two_sum([1, 8, 0, 17], 1) == [0,2]
    assert two_sum([5,16,2,3,6,0], 16) == [1,5]

def test_negative():
    assert two_sum([-5,-2,7,17], 5) == [1,2]
    assert two_sum([-5,-2,-7,-8,7,-9], -11) == [1,5]
    assert two_sum([-5,2,-3,0], -5) == [0,3]

if __name__ == "__main__":
    pytest.main()