class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p, q= headA, headB
        list_p = []
        list_q = []
        while p:
            list_p.append(p)
            p = p.next
        while q:
            list_q.append(q)
            q = q.next
        index_p = len(list_p)
        index_q = len(list_q)
        if list_q[index_q - 1] != list_p[index_p - 1]:
            return None
        while index_p and index_q:
            if list_q[index_q - 1] != list_p[index_p - 1]:
                return list_q[index_q]
            index_p, index_q = index_p - 1, index_q - 1
        return list_q[index_q]
