from collections import deque
from typing import List, Optional
import sys
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = []
        self.file = []


def build_tree(node: TreeNode, input_list: list, index):
    while index < len(input_list):
        if input_list[index][0] == 'f':
            node.file.append(input_list[index])
            index += 1
        elif input_list[index][0] == 'd':
            child_node = TreeNode(input_list[index])
            index += 1
            child_node, index = build_tree(child_node, input_list, index)
            node.children.append(child_node)
        elif input_list[index] == ']':
            index += 1
            return node, index
    return node, index


def output(node: TreeNode, data_set_num):
    print(f'DATA SET {data_set_num}:')
    print(f'ROOT')
    output_list = []

    def backtrack(node1, depth):
        for i in node1.children:
            output_list.append([depth, i.val])
            backtrack(i, depth + 1)
        node1.file = sorted(node1.file)
        for j in node1.file:
            output_list.append([depth - 1, j])

    backtrack(node, depth=1)
    for i in output_list:
        print('|     '*i[0] + i[1])


def main():
    lines = sys.stdin.read().splitlines()
    dataset_count = 0
    first_dataset = True

    i = 0
    index_left = 0
    while i < len(lines) and lines[i] != "#":
        if lines[i] == "*":
            dataset_count += 1
            root = TreeNode()
            root, _ = build_tree(root, lines[index_left:i], index=0)
            index_left = i+1
            # 在非第一个数据集前输出空行
            if not first_dataset:
                print()
            first_dataset = False

            output(root, dataset_count)

            # 输出数据集内容...

        i += 1

if __name__ == '__main__':
    main()
