#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d=ListNode()
        
        tail=d
        
        while True:
            if list1==None:
                tail.next=list2
                break
            if list2==None:
                tail.next=list1
                break
                
            if(list1.val<=list2.val):
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        
        return d.next

A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(4)
B = ListNode(1)
B.next = ListNode(3)
B.next.next = ListNode(4)
print(Solution.mergeTwoLists(A, B))