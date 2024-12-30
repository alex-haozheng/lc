"""Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order."""


# recursive
class Solution:
    def subsets(self, nums):
            ret = []
            self.dfs(nums, [], ret)
            return ret
        
        def dfs(self, nums, path, ret):
            ret.append(path)
            for i in range(len(nums)):
                self.dfs(nums[i+1:], path+[nums[i]], ret)
            
# iterative    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res
