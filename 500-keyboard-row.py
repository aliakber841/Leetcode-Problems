# Efficient 
class Solution(object):
    def findWords(self, words):
        hash_table={
            "1":"qwertyuiop",
            "2":"asdfghjkl",
            "3":'zxcvbnm'
        }
        result=[]
        for i in range(len(words)):
            current_word=words[i]
            if len(current_word)==0:
                continue
            index=""
            for key,value in hash_table.items():
                if current_word[0].lower() in value:
                     index=key
                     break
            if index=="":
                continue
            isValid=True
            for j in range(1,len(current_word)):
                if current_word[j].lower() not in hash_table[index]:
                    isValid=False
                    break
            if isValid:
                result.append(current_word)
        return result
# Nested Loops but bad memory space
class Solution(object):
    def findWords(self, words):
        hash_table={
            "1":"qwertyuiop",
            "2":"asdfghjkl",
            "3":'zxcvbnm'
        }
        result=[]
        current_string=""
        index=""
        for i in range(len(words)):
            index=""
            current_string=""
            current_word=words[i]
            isValid=True
            for j in range(len(current_word)):
                for key,value in hash_table.items():
                    if current_word[j].lower() in value:
                        if index=="":
                            index=key
                        elif index!=key:
                            isValid=False
                            break
                        current_string+=current_word[j]
                        break
                if not isValid:
                    break
            if isValid and len(current_string)==len(current_word):
                 result.append(current_string)
        return result