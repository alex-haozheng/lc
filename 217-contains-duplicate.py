"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) memspace O(1) runtime
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(1) memspace O(n) runtime
        nums.sort()
        for n1, n2 in zip(nums, nums[1:]):
            if n1 == n2:
                return True
        return False