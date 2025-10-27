# 双向链表：
class Node:
    def __init__(self, data):
        self.data = data  # 节点数据
        self.next = None  # 指向下一个节点
        self.prev = None  # 指向前一个节点


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 链表头部
        self.tail = None  # 链表尾部

    # 在链表尾部添加节点
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # 如果链表为空
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node

    # 在链表头部添加节点
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # 如果链表为空
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return new_node

    # 删除链表中的指定节点
    def delete(self, node):
        temp_node_value = node.data
        if not self.head:  # 链表为空
            return
        if node == self.head:  # 删除头部节点
            self.head = node.next
            if self.head:  # 如果链表非空
                self.head.prev = None
        elif node == self.tail:  # 删除尾部节点
            self.tail = node.prev
            if self.tail:  # 如果链表非空
                self.tail.next = None
        else:  # 删除中间节点
            node.prev.next = node.next
            node.next.prev = node.prev
        node = None  # 删除节点
        return temp_node_value

    # 打印链表中的所有元素，从头到尾
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # 打印链表中的所有元素，从尾到头
    def print_reverse(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.full = 0
        self.DoubleLink = DoublyLinkedList()
    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.DoubleLink.delete(self.cache[key][1])
            temp_node = self.DoubleLink.append(key)
            self.cache[key] = [self.cache[key][0], temp_node]
            return self.cache[key][0]
            #print(self.cache, self.full)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            self.full += 1
        temp_node = self.DoubleLink.append(key)
        if key in self.cache.keys():
            self.DoubleLink.delete(self.cache[key][1])
        self.cache[key] = [value, temp_node]
        if self.full > self.capacity:
            self.full -= 1
            deleted_key = self.DoubleLink.delete(self.DoubleLink.head)
            if self.DoubleLink.tail.data != deleted_key:
                del self.cache[deleted_key]
        #self.DoubleLink.print_list()
        #print(self.cache, self.full)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
def test_lru_cache():
    """测试 LRU 缓存的函数"""
    test_cases = [
        # 测试用例 1：基础功能测试
        (
            ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],
            [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]],
            [None, None, None, 1, None, -1, None, -1, 3, 4]
        ),
        # 测试用例 2：容量为1的特殊情况
        (
            ["LRUCache", "put", "get", "put", "get", "get"],
            [[1], [1, 1], [1], [2, 2], [1], [2]],
            [None, None, 1, None, -1, 2]
        ),
        # 测试用例 3：更新已存在键的值
        (
            ["LRUCache","put","put","put","put","get","get"],
            [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]],
            [None,None,None,None,None,-1,3]
        ),
    ]

    for i, (operations, params, expected) in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"操作序列: {operations}")
        print(f"参数序列: {params}")
        print(f"预期结果: {expected}")

        cache = None
        actual = []

        for op, param in zip(operations, params):
            if op == "LRUCache":
                cache = LRUCache(param[0])
                actual.append(None)
            elif op == "put":
                cache.put(param[0], param[1])
                actual.append(None)
            elif op == "get":
                result = cache.get(param[0])
                actual.append(result)

        print(f"实际结果: {actual}")
        print(f"测试结果: {'通过' if actual == expected else '失败'}")
        print("-" * 50)


if __name__ == "__main__":
    test_lru_cache()