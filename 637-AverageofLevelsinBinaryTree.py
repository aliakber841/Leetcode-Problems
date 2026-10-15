# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def levelOrder(queue,front,result):
    if front==len(queue):
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
    
    i=0
    sum_num=0.00000
    while i<len(list_values):
        sum_num+=list_values[i]
        i+=1
    avg=sum_num/i
    result.append(avg)
    levelOrder(queue,front,result)
class Solution(object):
    def averageOfLevels(self, root):
        queue=[]
        result=[]
        queue.append(root)
        levelOrder(queue,0,result)
        return result