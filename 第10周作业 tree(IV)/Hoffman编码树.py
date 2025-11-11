import heapq

class Node:
    def __init__(self, weight, char=None):
        self.weight = weight
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.weight == other.weight:
            return 0
        return self.weight < other.weight


def min_length(node: Node, depth: int):
    result = 0
    if node.left is None and node.right is None:
        return node.weight * depth
    if node.left is not None:
        result += min_length(node.left, depth + 1)
    if node.right is not None:
        result += min_length(node.right, depth + 1)
    return result


def main():
    n = int(input())
    nums = [Node(int(x)) for x in input().split()]
    heapq.heapify(nums)

    while len(nums) > 1:
        left = heapq.heappop(nums)
        right = heapq.heappop(nums)
        temp_node = Node(left.weight + right.weight)
        temp_node.left = left
        temp_node.right = right
        heapq.heappush(nums, temp_node)

    print(min_length(nums[0], depth=0))


if __name__ == '__main__':
    main()
