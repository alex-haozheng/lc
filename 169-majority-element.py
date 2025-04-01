"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(1) memspace O(1) runtime
        element, freq = 0, 0

        for num in nums:
            if freq == 0:
                element = num
            freq += 1 if num == element else -1
        return element