class Node(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class MyLinkedList(object):

    def __init__(self):
        self.head=None
        

    def get(self, index):
        if index==-1 or self.head is None:
            return -1
        count=0
        current=self.head
        while current:
            if index==count:
                return current.val
            count+=1
            current=current.next
        return -1
        

    def addAtHead(self, val):
        dummyNode=Node(val)
        dummyNode.next=self.head
        self.head=dummyNode


        

    def addAtTail(self, val):
        dummyNode=Node(val)
        if self.head is None:
            self.head=dummyNode
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=dummyNode
        

    def addAtIndex(self, index, val):
        # index is negative: nothing is inserted
        if index<0:
            return
        # index is 0: insert before the 0th node, so the new node becomes the head
        if index==0:
            self.addAtHead(val)
            return
        count=0
        newNode=Node(val)
        previous=None
        current=self.head
        while current:
            # "add a node before the indexth node": current is the indexth node,
        # so put the new node between previous and current
            if count==index:
                previous.next=newNode
                newNode.next=current
                return
            count+=1
            previous=current
            current=current.next
        # the loop ended, so current is None and count equals the length of the list.
    # "If index equals the length, append to the end": previous is the last node
        if count==index:
            previous.next=newNode
        # "If index is greater than the length, do not insert":
    # count==index is False here, so the function ends without inserting
        

    def deleteAtIndex(self, index):
        if index<0 or self.head is None:
            return 
        if index==0:
            self.head=self.head.next
            return
        previous=None
        current=self.head
        count=0
        while current:
            if count==index:
                previous.next=current.next
                return
            count+=1
            previous=current
            current=current.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)