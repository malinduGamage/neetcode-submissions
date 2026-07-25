# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:
            return True

        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        a = self.isSameTree(p.left,q.left)
        if a == False:
            return False
        b = self.isSameTree(p.right,q.right)
        if b == False:
            return False

        return True