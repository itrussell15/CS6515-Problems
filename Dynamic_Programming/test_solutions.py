import pytest
from dataclasses import dataclass, field
import solutions as DP

from typing import Any

@dataclass
class TestCaseData:
    input: Any
    answer: Any
    other_args: field(default_factory=dict) = None

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
    # https://leetcode.com/problems/word-break/
    "corrupted_text": {
        "1": {
            "input": {
                "x": "itwasthebestoftimes",
                "valid_words": ["it", "was", "the", "best", "of", "times"]
            },
            "answer": True
        },
        "2": {
            "input":{
                "x": "abcdefghijk",
                "valid_words": ["it", "was", "the", "best", "of", "times"]
            },
            "answer": False
        },
        "3": {
            "input": {
                "x": "didyougetitright",
                "valid_words": ["did", "you", "get", "it", "right"],
            },
            "answer": True
        },
        "4": {
            "input": {
                "x": "aaaaaaa",
                "valid_words": ["aaaa","aaa"]
            },
            "answer": True
        },
        "5": {
            "input": {
                "x": "catsandog",
                "valid_words": ["cats","dog","sand","and","cat"]
            },
            "answer": True
        },
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
    "longest_common_subsequence": {
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
    "making_change": {
        "1": {
            "input": {
                "denominations": [1, 5, 10, 20],
                "value": 16
            },
            "answer": True
        },
        "2": {
            "input": {
                "denominations": [1, 5, 10, 20],
                "value": 31
            },
            "answer": True
        },
        "3": {
            "input": {
                "denominations": [1, 5, 10, 20],
                "value": 40
            },
            "answer": True
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
    func = DP.fibonacci
    assert func(test_data.input) == test_data.answer

@pytest.mark.parametrize("case", cases["lis"])
def test_lis(case):
    test_data = TestCaseData(**cases["lis"][case])
    func = DP.lis
    assert func(test_data.input) == test_data.answer

@pytest.mark.parametrize("case", cases["corrupted_text"])
def test_corrupted_text(case):
    test_data = TestCaseData(**cases["corrupted_text"][case])
    func = DP.corrupted_text
    assert func(**test_data.input) == test_data.answer

@pytest.mark.parametrize("case", cases["longest_common_subsequence"])
def test_longest_common_subsequence(case):
    test_data = TestCaseData(**cases["longest_common_subsequence"][case])
    func = DP.longest_common_subsequence
    assert func(**test_data.input) == test_data.answer

@pytest.mark.parametrize("case", cases["making_change"])
def test_knapsack(case):
    test_data = TestCaseData(**cases["making_change"][case])
    func = DP.making_change
    assert func(**test_data.input) == test_data.answer

@pytest.mark.parametrize("case", cases["knapsack"])
def test_knapsack(case):
    test_data = TestCaseData(**cases["knapsack"][case])
    func = DP.knapsack
    assert func(**test_data.input) == test_data.answer