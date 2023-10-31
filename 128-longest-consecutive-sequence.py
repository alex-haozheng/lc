"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) space O(n) runtime with sets
        table = set(nums)
        ret = 0
        for x in table:
            if x - 1 not in table:
                y = x + 1
                while y in table:
                    y += 1
                ret = max(ret, y-x)
        return ret