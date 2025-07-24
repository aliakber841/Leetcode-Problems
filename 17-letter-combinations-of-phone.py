class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        dictionary_alphabets={
            '1':[],
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if len(digits)==1:
            return dictionary_alphabets[digits]
        result=[]
        def generateCombinations(index,current_combination):
            if index==len(digits):
                result.append(current_combination)
                return
            current_digit=digits[index]
            for letter in (dictionary_alphabets[current_digit]):
                generateCombinations(index+1,current_combination+letter)
        generateCombinations(0,"")
        return result