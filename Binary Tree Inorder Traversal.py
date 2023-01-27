'''Given the root of a binary tree, return the inorder traversal of its nodes' values.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def trnode(root):
            if root == None:
                return
            if root:
                trnode(root.left)
                res.append(root.val)
                print(root.val)
                trnode(root.right)
            return res

        return trnode(root)

