# -*- coding:utf-8 -*-
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = list()

        if root:
            self.core(root, output)

        return output

    def core(self, cur_root, output):
        if cur_root:
            self.core(cur_root.left, output)
            output.append(cur_root.val)
            self.core(cur_root.right, output)
        return None
