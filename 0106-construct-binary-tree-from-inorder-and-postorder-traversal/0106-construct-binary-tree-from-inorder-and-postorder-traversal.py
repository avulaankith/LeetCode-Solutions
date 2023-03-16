# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        root_val = postorder.pop()

        root = TreeNode(root_val)

        root_indx = inorder.index(root_val)

        linorder = inorder[:root_indx]
        rinorder = inorder[root_indx+1:]

        root.right = self.buildTree(rinorder,postorder)
        root.left = self.buildTree(linorder,postorder)
        

        return root
