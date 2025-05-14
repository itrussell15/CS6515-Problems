import pytest
from dataclasses import dataclass
import solutions as DP

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
    # https://leetcode.com/problems/longest-common-subsequence/
    "lcs": {
        "1": {
            "input": {
                "x": "abcde",
                "y": "ace"
            },
            "answer": 3
        },
        "2": {
            "input": {
                "x": "abc",
                "y": "abc"
            },
            "answer": 4
        },
        "3": {
            "input": {
                "x": "abc",
                "y": "def"
            },
            "answer": 0
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

@pytest.mark.parametrize("case", cases["fibonacci"])
def test_fibonacci(case):
    test_data = TestCaseData(**cases["fibonacci"][case])
    func = DP.fibbonacci
    assert func(test_data.input) == test_data.answer

@pytest.mark.parametrize("case", cases["lis"])
def test_lis(case):
    test_data = TestCaseData(**cases["lis"][case])
    func = DP.lis
    assert func(test_data.input) == test_data.answer

@pytest.mark.parametrize("case", cases["lcs"])
def test_lcs(case):
    test_data = TestCaseData(**cases["lcs"][case])
    func = DP.lcs
    assert func(**test_data.input) == test_data.answer

@pytest.mark.parametrize("case", cases["knapsack"])
def test_knapsack(case):
    test_data = TestCaseData(**cases["knapsack"][case])
    func = DP.knapsack
    assert func(**test_data.input) == test_data.answer