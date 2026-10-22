import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        hash_table={}
        for i in range(len(words)):
            if words[i] in hash_table:
                hash_table[words[i]]+=1
            else:
                hash_table[words[i]]=1
        
        heap=[]
        for key,value in hash_table.items():
            heapq.heappush(heap,(-value,key)) 
        
        answer=[]
        for i in range(k):
            value,key=heapq.heappop(heap)
            answer.append(key)
        return answer