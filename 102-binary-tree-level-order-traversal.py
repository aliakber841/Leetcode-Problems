# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        result=[]
        queue=deque([root])
        while queue:
            level=[]
            queue_size=len(queue)
            while queue_size>0:
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                queue_size-=1
            result.append(level)
        return result    