from typing import List

def fibonacci(n: int) -> int:
    """
    Fibonacci Numbers -> [0, 1, 1, 2, 3, 5, 8, 13, ...]
        Runtime: O(?)
        Memory:  O(?)
    Leetcode: https://leetcode.com/problems/fibonacci-number/description/
    Neetcode:
    """
    if n == 0 or n == 1:
        return n
    cache = [0, 1]
    for i in range(1, n):
        old_item = cache.pop(0)
        cache.append(old_item + cache[0])
    return cache[-1]

def corrupted_text(x: str, valid_words: List[str]) -> bool:
    """
    Corrupted Text (DPV 6.4) / Word Break
        Runtime: O(n^2)
        Memory:  O(?)
    Leetcode: https://leetcode.com/problems/word-break/
    Neetcode: https://www.youtube.com/watch?v=Sx9NNgInc3A
    """
    head = 0
    tail = 1

    while tail <= len(x):
        if tail == len(x):
            break

        if x[head:tail] in valid_words:
            head = tail
            tail = head + 1
        else:
            tail += 1
    return x[head:tail] in valid_words

def lis(x: List[int]) -> int:
    """
    Longest Increasing Subsequence
        Runtime: O(?)
        Memory:  O(?)
    Leetcode: https://leetcode.com/problems/longest-increasing-subsequence/description/
    Neetcode: https://www.youtube.com/watch?v=cjWnW0hdF1Y
    """
    nums_loop = range(len(x))
    lens = [1 for _ in nums_loop]
    for i in nums_loop:
        for j in range(i):
            if x[j] < x[i] and lens[i] < 1 + lens[j]:
                lens[i] = lens[j] + 1
    return max(lens)

def longest_common_substring(x: str, y: str) -> int:
    """
    Longest Common Substring
        Runtime: O(?)
        Memory:  O(?)
    Leetcode:
    Neetcode:
    """
    return None

def longest_common_subsequence(x: str, y: str) -> int:
    """
    Longest Common Subsequence
        Runtime: O(?)
        Memory:  O(?)
    Leetcode: https://leetcode.com/problems/longest-common-subsequence/
    Neetcode: https://www.youtube.com/watch?v=Ua0GhsJSlWM
    """
    return None

def making_change(denominations: List[int], value: int) -> bool:
    """
    Making Change II
        Runtime: O(?)
        Memory:  O(?)
    Leetcode: N/A
    Neetcode: N/A
    """
    return None

def knapsack(weights: List[int], values: List[int]) -> int:
    """
    Knapsack Problem / Painting the Walls
        Runtime: O(?)
        Memory:  O(?)
    Leetcode: https://leetcode.com/problems/painting-the-walls/description/
    Neetcode: https://www.youtube.com/watch?v=Ua0GhsJSlWM
    """
    return None