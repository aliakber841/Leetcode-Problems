class MyHashMap(object):

    def __init__(self):
        self.size=1000
        self.buckets=[]
        for i in range(self.size):
            self.buckets.append([])
        

    def put(self, key, value):
        index=key%self.size
        bucket=self.buckets[index]
        for pair in bucket:
            if pair[0]==key:
                pair[1]=value
                return
        bucket.append([key,value])

    def get(self, key):
        index=key%self.size
        bucket=self.buckets[index]
        for pair in bucket:
            if pair[0]==key:
                return pair[1]
        return -1
        

    def remove(self, key):
        index=key%self.size
        bucket=self.buckets[index]
        for pair in bucket:
            if pair[0]==key:
                bucket.remove(pair)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)