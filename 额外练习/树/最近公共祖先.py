from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        have_find = [0, 0]
        #print(p.val)
        #print(q.val)

        def find_ancestor(node, ancestor, lvl):
            if not node:
                return ancestor
            if node == p or node == q:
                if not ancestor:
                    ancestor = node
                    have_find[1] = lvl
                else:
                    have_find[0] = 1
                    return ancestor

            ancestor = find_ancestor(node.left, ancestor, lvl+1)
            if have_find[0] == 0 and lvl < have_find[1] and ancestor:
                #print(ancestor.val, have_find, lvl)
                ancestor = node
                have_find[1] = lvl
            ancestor = find_ancestor(node.right, ancestor, lvl+1)
            return ancestor

        ans = find_ancestor(root, None, 0)
        return ans
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):  # 找到 p 或 q 就不往下递归了，原因见上面答疑
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # 左右都找到
            return root  # 当前节点是最近公共祖先
        # 如果只有左子树找到，就返回左子树的返回值
        # 如果只有右子树找到，就返回右子树的返回值
        # 如果左右子树都没有找到，就返回 None（注意此时 right = None）
        return left or right



def preorder(node):
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)


def from_list_to_tree(arr: list, p: int, q: int):
    root = TreeNode(arr[0])
    deq = deque()
    node = root
    p_node = None
    q_node = None
    for i in arr[1:]:
        if node.left and node.right:
            if node.val == p:
                p_node = node
            if node.val == q:
                q_node = node
            node = deq.popleft()
        children_node = TreeNode(i)
        if not node.left:
            node.left = children_node
        elif not node.right:
            node.right = children_node
        deq.append(children_node)
    while deq:
        node = deq.popleft()
        if node.val == p:
            p_node = node
        if node.val == q:
            q_node = node
    return root, p_node, q_node



if __name__ == '__main__':
    solut = Solution()
    root, p, q = from_list_to_tree([3,5,1,6,2,0,8,None,None,7,4], p = 0, q = 8)
    preorder(root)
    print()
    print(solut.lowestCommonAncestor(root, p, q).val)
