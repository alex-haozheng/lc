# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) runtime O(1) memspace
        # floyds cycle algorithm
        if not head:
            return False
        h = t = head
        while t.next != None and t.next.next != None:
            h = h.next
            t = t.next.next
            if h == t:
                return True
        return False