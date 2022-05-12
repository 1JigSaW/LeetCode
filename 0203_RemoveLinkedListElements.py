
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(head, val):
        temp=head
        while(temp and head):
            if head.val==val:
                head=head.next
                temp=head
            elif temp.next:
                if temp.next.val==val:
                    temp.next=temp.next.next
                else:
                    temp=temp.next
            else:
                break
        return head

A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(6)
A.next.next.next = ListNode(3)
A.next.next.next.next = ListNode(4)
A.next.next.next.next.next = ListNode(5)
A.next.next.next.next.next.next = ListNode(6)
val = 6
print(Solution.removeElements(A, val))