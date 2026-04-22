# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        if p1 is None:
            return p2
        if p2 is None:
            return p1

        if p1.val < p2.val:
            head = p1
            p1 = p1.next
        else: 
            head = p2
            p2 = p2.next
        
        p3 = head

        while p1 is not None or p2 is not None:
            if p1 is None:
                p3.next = p2
                return head
            if p2 is None:
                p3.next = p1
                return head
            
            val1 = p1.val
            val2 = p2.val

            if val1<val2:
                p3.next = p1
                p3 = p3.next
                p1 = p1.next

            else:
                p3.next = p2
                p3 = p3.next
                p2 = p2.next
            
        return head
