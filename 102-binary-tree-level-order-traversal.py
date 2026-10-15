# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def level(queue,front,result):
    if len(queue)==front:
        return
    count=len(queue)-front
    list_values=[]
    while count>0:
        node=queue[front]
        list_values.append(node.val)
        front+=1
        count-=1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    result.append(list_values)
    level(queue,front,result)
    
class Solution(object):
    def levelOrder(self, root):
        queue=[]
        front=0
        result=[]
        if not root:
            return []
        queue.append(root)
        level(queue,front,result)
        return result
    
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

