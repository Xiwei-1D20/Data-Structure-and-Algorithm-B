# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def reverseList(self, head):
        def reverse(node, next):
            if next:
                first = reverse(next, next.next)
                next.next = node
                return first
            else:
                return node
        return(reverse(None, head))

