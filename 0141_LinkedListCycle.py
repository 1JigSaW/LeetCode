class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(head):
        fast = slow = head
        print(slow.val, fast.val)
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        return False

# A = ListNode(3)
# A.next = ListNode(2)
# A.next.next = ListNode(0)
# A.next.next.next = ListNode(-4)
# A.next.next.next.next = A.next
# print(Solution.hasCycle(A))