"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    # use <= in while when searching for a specific element (not skipping a single index)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                # excluding m from search
                l = m + 1        
            else:
                # excluding m from search
                r = m - 1
        return -1