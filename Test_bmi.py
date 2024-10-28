import pytest
from Lab2.bmi import calculate_bmi

def test_bmi_normal_weight():
    result = calculate_bmi(1.77,75)
    assert result == 0

def test_bmi_over_weight():
    result = calculate_bmi(1.77,81)
    assert result == 1

def test_bmi_under_weight():
    result = calculate_bmi(1.77,50)
    assert result == -1        
    