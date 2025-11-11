from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def node_in_post_and_mid(mid, parent_post):
    mid_set = set(mid)
    post = []
    for i in parent_post:
        if i in mid_set:
            post.append(i)
    return post


def build_tree(post: str, mid: str):
    root = TreeNode(post[-1])
    index = 0
    for i in range(len(mid)):
        if mid[i] == post[-1]:
            index = i
            break
    left_mid = mid[:index]
    right_mid = mid[index + 1:]
    if len(left_mid) > 0:
        left_post = node_in_post_and_mid(left_mid, post)
        root.left = build_tree(left_post, left_mid)
    if len(right_mid) > 0:
        right_post = node_in_post_and_mid(right_mid, post)
        root.right = build_tree(right_post, right_mid)

    return root


def levelorder(node: TreeNode, trace: list):
    if node:
        q = deque([node])
        while q:
            temp_node = q.popleft()
            trace.append(temp_node.val)
            if temp_node.left is not None:
                q.append(temp_node.left)
            if temp_node.right is not None:
                q.append(temp_node.right)
    return trace


def main():
    n = int(input())
    for i in range(n):
        mid = input()
        post = input()
        root = build_tree(post, mid)
        print(''.join(levelorder(root, trace=[])))


if __name__ == '__main__':
    main()
