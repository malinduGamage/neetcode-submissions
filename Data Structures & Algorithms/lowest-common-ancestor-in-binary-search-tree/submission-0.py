# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pPath = []
        self.search(root,p.val,pPath)
        qPath = []
        self.search(root,q.val,qPath)
        i = 0

        limit = min(len(pPath),len(qPath))
        while (i<limit and pPath[i].val == qPath[i].val):
            i +=1
        
        return pPath[i-1]

    def search(self,root,x,path):
        path.append(root)

        if root.val == x:
            return
        
        elif root.val > x:
            return self.search(root.left,x,path)
        else:
            return self.search(root.right,x,path)