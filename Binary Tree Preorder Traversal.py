'''Given the root of a binary tree, return the preorder traversal of its nodes' values.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, res):
        if root == None:
            return
        print(root.val)
        res.append(root.val)
        if root.left:
            self.traverse(root.left, res)
        if root.right:
            self.traverse(root.right, res)
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        return self.traverse(root, res)