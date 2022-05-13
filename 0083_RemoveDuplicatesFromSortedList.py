class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


A = ListNode(1)
A.next = ListNode(1)
A.next.next = ListNode(3)
print(Solution.deleteDuplicates(A))
        