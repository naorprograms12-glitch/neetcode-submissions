# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        size = 0
        p = head
        while p:
            size+=1
            p = p.next

        if n == size:
            return head.next

        prev = head
        for i in range(size-n-1):
            prev=prev.next
        print(prev.val)
        curr = prev.next
        nxt = curr.next
        prev.next = nxt
        curr.next = None

        return head
        