# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        x=  self.isSameTree(root,subRoot)
        if x:
            return True
        if root.left:
            y = self.isSubtree(root.left,subRoot)
            if y:
                return True
        if root.right:
            z = self.isSubtree(root.right,subRoot)
            if z:
                return True
        return False

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