# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    """从列表构建链表"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def linked_list_to_list(head):
    """将链表转换为列表（用于验证）"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution:
    def isPalindrome(self, head) -> bool:
        q = head
        length = 0
        while q:
            q = q.next
            length += 1
        q = head
        temp1 = None
        for i in range(length-1):
            if i >= length // 2:
                temp = q
                if temp1:
                    q = temp1
                else:
                    q = q.next
                temp1 = q.next
                q.next = temp
            else:
                q = q.next
        first = q
        second = head
        for i in range(length//2):
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                return False
        return True

def run_tests():
    test_cases = [
        ([], True),  # 空链表
        ([1], True),  # 单节点
        ([1, 2], False),  # 非回文
        ([1, 1], True),  # 回文
        ([1, 2, 1], True),  # 回文
        ([1, 2, 3], False),  # 非回文
        ([1, 2, 2, 1], True),  # 回文
    ]

    for i, (values, expected) in enumerate(test_cases):
        head = create_linked_list(values)
        result = solution.isPalindrome(head)
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {status} Input: {values} -> Expected: {expected}, Got: {result}")


# 运行测试
if __name__ == "__main__":
    solution = Solution()
    run_tests()