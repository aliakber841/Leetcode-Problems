class Solution(object):
    def recoverOrder(self, order, friends):
        result=[]
        for i in range(0,len(order)):
            if order[i] in friends:
                result.append(order[i])
        return result

# class Solution(object):
#     def recoverOrder(self, order, friends):
#         hash_table={}
#         result=[]
#         for i in range(len(friends)):
#             hash_table[friends[i]]=i
#         for j in range(len(order)):
#             if order[j] in hash_table:
#                 result.append(order[j])
#         return result
