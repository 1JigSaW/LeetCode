class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(head):
        if head is None or head.next is None:
            return head
        prev = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode
        return prev
    

A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)
A.next.next.next = ListNode(4)
A.next.next.next.next = ListNode(5)
print(Solution.reverseList(A))