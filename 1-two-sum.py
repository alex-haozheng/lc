"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) memspace O(n) runtime
        composite = {}
        for i, n in enumerate(nums):
            if n not in composite:
                composite[target-n] = i
            else:
                return [composite[n], i]
        return None