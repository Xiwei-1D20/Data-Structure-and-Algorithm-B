class TreeNode:
    def __init__(self, val=None, left=None, right=None, have_not=0):
        self.val = val
        self.left = left
        self.right = right
        self.have_not = have_not


def isTreeNode(node_or_s):
    if isinstance(node_or_s, TreeNode):
        return node_or_s
    else:
        return TreeNode(node_or_s)


def middle_to_node(s):
    j = 0
    while j < len(s):
        if s[j] == 'not':
            temp = isTreeNode(s[j+1])
            temp.have_not = 1
            del s[j:j+2]
            s.insert(j, temp)
        j += 1

    sign = ['and', 'or']
    for i in range(2):
        j = 0
        while j < len(s):
            if s[j] == sign[i]:
                temp = TreeNode(s[j])
                temp.left = isTreeNode(s[j - 1])
                temp.right = isTreeNode(s[j + 1])
                del s[j-1:j+2]
                s.insert(j-1, temp)
                j -= 1
            j += 1
    return s[0]


def need_brackets(val1, val2):
    temp = ['and', 'or']
    if val1 not in temp:
        return 0
    if val1 == val2:
        return 0
    if val1 == 'and' and val2 == 'or':
        return 0
    return 1


def midorder(trace, node: TreeNode, parent_node: TreeNode, deepth: int):
    if node is None:
        return trace
    deepth += 1
    if node.have_not == 1:
        trace.append('not')
    if deepth > 1 and need_brackets(node.val, parent_node.val):
        trace.append('(')
    trace = midorder(trace, node.left, node, deepth)
    trace.append(node.val)
    trace = midorder(trace, node.right, node, deepth)
    if deepth > 1 and need_brackets(node.val, parent_node.val):
        trace.append(')')
    return trace


def main():
    s = input().split()
    stack = []
    j = 0
    while 1:
        if s[j] == '(':
            stack.append(j)
        elif s[j] == ')':
            index = stack.pop()
            temp = middle_to_node(s[index + 1:j])
            del s[index:j + 1]
            s.insert(index, temp)
            j -= (j - index + 1)
        j += 1
        if j == len(s):
            break
    s = middle_to_node(s)
    trace = []
    print(' '.join(midorder(trace, s, parent_node=TreeNode(), deepth=0)))
    return 0


if __name__ == '__main__':
    main()
