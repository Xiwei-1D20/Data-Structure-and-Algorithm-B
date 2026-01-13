class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        last = dummy
        next_val = 0
        while l1 or l2 or next_val:
            if not l2:
                l2 = ListNode()
            if not l1:
                l1 = ListNode()
            cur_val = (l1.val + l2.val + next_val) % 10
            cur = ListNode(cur_val)
            next_val = (l1.val + l2.val + next_val) // 10
            l1 = l1.next
            l2 = l2.next
            last.next = cur
            last = cur
        return dummy.next
