# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        if root == None or root.val == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))    

# root = TreeNode(None)
# print(Solution().maxDepth(root)) # expects 0

# root2 = TreeNode(1)
# print(maxDepth(root2)) # expects 1

# root2.left = TreeNode(2)
# print(maxDepth(root2)) # expects 2

# root6 = TreeNode(15)
# root7 = TreeNode(7)
# root4 = TreeNode(9)
# root5 = TreeNode(20, root6, root7)
# root3 = TreeNode(3, root4, root5)
# print(maxDepth(root3)) # expects 3
