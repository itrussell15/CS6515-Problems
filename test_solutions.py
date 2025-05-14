import pytest
from dataclasses import dataclass
from Dynamic_Programming.solutions import fibbonacci, lis, knapsack

from typing import Any

@dataclass
class TestCaseData:
    input: Any
    answer: Any

cases = {
    # https://leetcode.com/problems/fibonacci-number/description/
    "fibonacci": {
        "1": {
                "input": 3,
                "answer": 1,
        },
        "2": {
                "input": 4,
                "answer": 2,
        },
        "3": {
                "input": 4,
                "answer": 3,
        }
    },
    # https://leetcode.com/problems/longest-increasing-subsequence/description/
    "lis": {
        "1": {
            "input": [10,9,2,5,3,7,101,18],
            "answer": 4,
        },
        "2": {
            "input": [0,1,0,3,2,3],
            "answer": 4,
        },
        "3": {
            "input": [7,7,7,7,7,7,7],
            "answer": 1,
        }
    },
    # https://leetcode.com/problems/painting-the-walls/description/
    "knapsack":{
        "1": {
            "input": {
                "weights": [1,2,3,2],
                "values": [1,2,3,2]
            },
            "answer": 3
        },
        "2": {
            "input": {
                "weights": [2,3,4,2],
                "values": [1,1,1,1]
            },
            "answer": 4
        }
    }
}

TEST_CASE = "fibonacci"
# Parametrize test cases
@pytest.mark.parametrize("case", cases[TEST_CASE])
def test_fibonacci(case):
    test_data = TestCaseData(**cases[TEST_CASE][case])
    func = fibbonacci
    assert func(test_data.input) == test_data.answer

TEST_CASE = "lis"
# Parametrize test cases
@pytest.mark.parametrize("case", cases[TEST_CASE])
def test_lis(case):
    test_data = TestCaseData(**cases[TEST_CASE][case])
    func = lis
    assert func(test_data.input) == test_data.answer

TEST_CASE = "knapsack"
@pytest.mark.parametrize("case", cases[TEST_CASE])
def test_knapsack(case):
    test_data = TestCaseData(**cases[TEST_CASE][case])
    func = knapsack
    assert func(**test_data.input) == test_data.answer