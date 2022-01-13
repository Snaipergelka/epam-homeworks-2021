"""
    Given a list of integers numbers "nums".
    You need to find a sub-array with length less equal to "k",
    with maximal sum.
    The written function should return the sum of this sub-array.
    Examples:
        nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
        result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) == 0 or k <= 0:
        return None
    max_subarray_sum = nums[0]
    for i in range(len(nums)):
        for j in range(1, k + 1):
            current_subarray_sum = sum(nums[i:i + j])
            if current_subarray_sum > max_subarray_sum:
                max_subarray_sum = current_subarray_sum
    return max_subarray_sum
