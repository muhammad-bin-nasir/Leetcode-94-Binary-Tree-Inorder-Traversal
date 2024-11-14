# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l1 = []
        def inord (node):
            if (node):
                inord(node.left)
                l1.append(node.val)
                inord(node.right)
        inord(root)
        return l1  
