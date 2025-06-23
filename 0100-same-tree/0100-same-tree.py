# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Base case 1: both nodes are None -> trees are identical at this point
        if not p and not q:
            return True
        
        # Base case 2: one is None and the other isn't -> trees differ
        if not p or not q:
            return False
        
        # Base case 3: values differ -> tree differ
        if p.val != q.val:
            return False
        
        # Recursive step: check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)