"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray

whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = ret = 0
        csum = nums[0]
        while left < len(nums) and right < len(nums):
            if csum >= target:
                ret = min(ret, right-left+1) if ret != 0 else right-left+1
                csum -= nums[left]
                left += 1
            else:
                right += 1
                if right == len(nums):
                    break
                csum += nums[right]
        return ret