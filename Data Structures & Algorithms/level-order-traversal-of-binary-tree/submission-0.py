# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        r = [[root]]
        p = [[root.val]]
        lvl = 0
        while len(r[lvl])>0:
            nodes = r[lvl]
            s = []
            t = []
            for node in nodes:
                if node.left:
                    s.append(node.left)
                    t.append(node.left.val)
                if node.right:
                    s.append(node.right)
                    t.append(node.right.val)
            if len(t)==0:
                break
            r.append(s)
            p.append(t)
            lvl+=1
        return p
