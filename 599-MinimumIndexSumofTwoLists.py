class Solution(object):
    def findRestaurant(self, list1, list2):
        hash_table={}
        result=[]
        for i in range(len(list1)):
            current_word=list1[i]
            hash_table[current_word]=i
        
        minValue=len(list1)+len(list2)
        for j in range(len(list2)):
            current_word=list2[j]
            if current_word in hash_table:
                val1=hash_table[current_word]
                value=val1+j
                if minValue>value:
                    minValue=value
                    result=[current_word]
                elif minValue==value:
                    result.append(current_word)
        return result
        