from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: 
                break
        else: 
            return None 
        while head != slow:
            head, slow = head.next, slow.next
        return head

A = ListNode(1)
A.next = ListNode(2)
print(Solution().detectCycle(A))