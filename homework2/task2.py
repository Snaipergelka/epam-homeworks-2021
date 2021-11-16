"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    count = {}
    for x in inp:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    # Check which element is most common and rarest
    common = 0
    result_common = 0
    result_rare = 0
    rare = count[inp[0]]
    for key in count:
        if count[key] >= (len(inp) // 2) and count[key] > common:
            common = count[key]
            result_common = key
        elif count[key] < rare:
            rare = count[key]
            result_rare = key
    return result_common, result_rare
