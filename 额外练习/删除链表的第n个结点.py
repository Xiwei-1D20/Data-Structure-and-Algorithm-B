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
    def removeNthFromEnd(self, head, n: int):

        def backstack(current_node=head, count=0):
            if current_node:
                count += 1
                backstack(current_node.next, count)
                print(linked_list_to_list(current_node))
            else:
                size = count
            if size - count + 1 == n:
                temp = current_node.next
            elif size - count + 1 == n - 1:
                current_node.next = temp
        backstack()
        return head


def run_tests():
    test_cases = [
        ([1], 1, []),  # 单节点
        ([1, 2], 1, [1]),  # 非回文
        ([1, 2], 2, [2]),  # 回文
        ([1, 2, 1], 2, [1, 1]),  # 回文
        ([1, 2, 3], 3, [2, 3]),  # 非回文
    ]

    for i, (values, n, expected) in enumerate(test_cases):
        head = create_linked_list(values)
        result = linked_list_to_list(solution.removeNthFromEnd(head, n))
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {status} Input: {values} -> Expected: {expected}, Got: {result}")


# 运行测试
if __name__ == "__main__":
    solution = Solution()
    run_tests()
