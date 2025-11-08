class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def node_in_pre_and_mid(mid, parent_pre):
    mid_set = set(mid)
    pre = []
    for i in parent_pre:
        if i in mid_set:
            pre.append(i)
    return pre


def build_tree(pre: list, mid: list):
    root = TreeNode(pre[0])
    index = 0
    for i in range(len(mid)):
        if mid[i] == pre[0]:
            index = i
            break
    left_mid = mid[:index]
    right_mid = mid[index + 1:]
    if len(left_mid) > 0:
        left_pre = node_in_pre_and_mid(left_mid, pre)
        root.left = build_tree(left_pre, left_mid)
    if len(right_mid) > 0 :
        right_pre = node_in_pre_and_mid(right_mid, pre)
        root.right = build_tree(right_pre, right_mid)

    return root


def postorder(node: TreeNode, trace: list):
    if node is not None:
        trace = postorder(node.left, trace)
        trace = postorder(node.right, trace)
        trace.append(node.val)
    return trace


def main():
    while 1:
        try:
            pre, mid = [list(x) for x in input().split()]
            root = build_tree(pre, mid)
            print(''.join(postorder(root, trace=[])))
        except EOFError:
            break


if __name__ == '__main__':
    main()
