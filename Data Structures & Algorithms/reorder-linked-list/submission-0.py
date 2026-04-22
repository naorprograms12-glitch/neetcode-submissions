class Solution:
    @staticmethod
    def find_len(head):
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt

    def reorderList(self, head):
        n = Solution.find_len(head)
        if n <= 2:
            return

        lst = []
        p = head
        while p:
            lst.append(p)
            p = p.next

        l, r = 0, n - 1
        dummy = ListNode()
        p = dummy

        while l <= r:
            p.next = lst[l]
            p = p.next
            l += 1

            if l <= r:
                p.next = lst[r]
                p = p.next
                r -= 1

        p.next = None