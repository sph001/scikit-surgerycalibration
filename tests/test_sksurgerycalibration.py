# coding=utf-8

"""scikit-surgery-calibration tests"""

from sksurgerycalibration.ui.sksurgerycalibration_demo import run_demo
from sksurgerycalibration.algorithms import addition, multiplication
import six

# Pytest style

def test_using_pytest_sksurgerycalibration():
    x = 1
    y = 2
    verbose = False
    multiply = False

    expected_answer = 3
    assert run_demo(x, y, multiply, verbose) == expected_answer

def test_addition():

    assert addition.add_two_numbers(1, 2) == 3

def test_multiplication():

    assert multiplication.multiply_two_numbers(2, 2) == 4

