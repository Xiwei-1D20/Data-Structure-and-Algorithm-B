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


def main():
    while 1:
        n, m = [int(x) for x in input().split()]
        if n == 0 and m == 0:
            break
        else:
            monkeys = list(range(1, n+1))
            head = ListNode(monkeys[0])
            last = head
            for i in range(1, n):
                cur = ListNode(monkeys[i])
                last.next = cur
                last = cur
            last.next = head
            cur = head
            num = n
            count = 1
            while num > 1:
                if count == m:
                    num -= 1
                    count = 1
                    cur = cur.next
                    last.next = cur
                    continue
                last = cur
                cur = cur.next
                count += 1
            else:
                print(cur.val)


# 运行测试
if __name__ == "__main__":
    main()