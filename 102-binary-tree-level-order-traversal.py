"""
Given the root of a binary tree, return the level order traversal of
its nodes' values. (i.e., from left to right, level by level).
"""


from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # runtime O(n) memspace O(n)
        if not root:
            return []
        queue = deque([root])
        ans = []

        while queue:
            current_length = len(queue)
            # do logic for current level
            lst = []

            for _ in range(current_length):
                node = queue.popleft()
                # do logic
                if not node:
                    continue
                lst.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(lst)

        return ans