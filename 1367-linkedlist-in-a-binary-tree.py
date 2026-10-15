# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(root,path,list_values,size):
    if root is None:
        return False
    path.append(root.val)
    if len(path)>=size:
        start=len(path)-size
        if path[start:]==list_values:
            return True
    if dfs(root.left,path,list_values,size):
        return True
    if dfs(root.right,path,list_values,size):
        return True
    path.pop()
    return False
    
class Solution(object):
    def isSubPath(self, head, root):
        list_values=[]
        current=head
        while current:
            list_values.append(current.val)
            current=current.next
        size=len(list_values)
        path=[]
        return dfs(root,path,list_values,size)