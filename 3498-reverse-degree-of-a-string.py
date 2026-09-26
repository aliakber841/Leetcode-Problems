class Solution(object):
    def reverseDegree(self, s):
        sum_string=0
        alphabets="abcdefghijklmnopqrstuvwxyz"
        hash_table={}
        for i in range(len(alphabets)):
            hash_table[alphabets[i]]=26-i

        for i in range(0,len(s)):
            index=i+1
            reversed_index=hash_table[s[i]]
            sum_string+=index*reversed_index
        return sum_string

class Solution(object):
    def reverseDegree(self, s):
        sum_string=0
        hash_set="zyxwvutsrqponmlkjihgfedcba"

        for i in range(0,len(s)):
            index=i+1
            reversed_index=hash_set.index(s[i])+1
            sum_string+=index*reversed_index
        return sum_string