class Solution(object):
    def findEvenNumbers(self, digits):
        result=[]
        hash_table={}

        for i in range(len(digits)):
            if digits[i] not in hash_table:
                 hash_table[digits[i]]=1
            else:
                hash_table[digits[i]]+=1
            
        i=100
        while i<=998:
            digit=i #102
            remaining_digits=digit
            isValid=True
            number_table={}
            while remaining_digits>0:
                digit=remaining_digits%10 #2
                remaining_digits=remaining_digits//10 #10
                if digit not in number_table:
                    number_table[digit]=1
                else:
                    number_table[digit]+=1
            for digit in number_table:
                if digit not in hash_table or number_table[digit]>hash_table[digit]:
                    isValid=False
                    break

            if isValid==True:
                result.append(i)
            i+=2
        return result