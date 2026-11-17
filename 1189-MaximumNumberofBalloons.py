class Solution(object):
    def maxNumberOfBalloons(self, text):
        hash_table={}
        for i in range(len(text)):
            if text[i] in hash_table:
                hash_table[text[i]]+=1
            else:
                hash_table[text[i]]=1
        
        count_b=hash_table.get("b",0)
        count_a=hash_table.get("a",0)
        count_l=hash_table.get("l",0)
        count_o=hash_table.get("o",0)
        count_n=hash_table.get("n",0)

        words_from_l=count_l//2
        words_from_o=count_o//2
        return min(count_b,count_a,words_from_l,words_from_o,count_n)