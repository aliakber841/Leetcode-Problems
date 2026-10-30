class MyHashSet(object):

    def __init__(self):
        self.size=1000
        self.buckets=[]
        for i in range(self.size):
            self.buckets.append([])
        

    def add(self, key):
        index=key%self.size
        if key not in self.buckets[index]:
            self.buckets[index].append(key)
        

    def remove(self, key):
        index=key%self.size
        if key in self.buckets[index]:
            self.buckets[index].remove(key)
        

    def contains(self, key):
        index=key%self.size
        if key in self.buckets[index]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)