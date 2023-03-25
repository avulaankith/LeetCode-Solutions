# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # global l1
        # l1 = []
        
        def getLeaves(node):
            if node == None:
                return []
            if node.left == None and node.right == None:
                return [node.val]
            return getLeaves(node.left) + getLeaves(node.right)
        
        l1 = getLeaves(root1)
        l2 = getLeaves(root2)

        if l1 == l2:
            return True
        else:
            return False