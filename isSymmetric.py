# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = deque([root.left, root.right])
        lv, rv = [], []
        while queue:
            lv, rv = [], []
            temp = deque([])
            for _ in range(len(queue) / 2):
                root = queue.popleft()
                val = None
                if root:
                    temp += [root.left, root.right]
                    val = root.val
                lv += [val]
            while queue:
                root = queue.popleft()
                val = None
                if root:
                    temp += [root.left, root.right]
                    val = root.val
                rv += [val]
            if lv != rv[::-1]:
                return False
            queue = temp
        return lv == rv[::-1]
                
