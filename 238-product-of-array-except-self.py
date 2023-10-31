"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) space O(n) runtime
        # left and right running products
        ret = [1 for _ in nums]
        left = right = 1

        for i in range(len(nums)):
            ret[i] *= left
            ret[~i] *= right
            left *= nums[i]
            right *= nums[~i]
        return ret