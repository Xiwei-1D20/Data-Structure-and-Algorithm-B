from collections import deque
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next
            if fast == slow:
                return True
            fast = fast.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # 将慢指针指定为新指针
                slow = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                else:
                    return fast
        return None
