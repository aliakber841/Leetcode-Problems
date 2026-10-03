class Solution(object):
    def numOfStrings(self, patterns, word):
        count=0
        for i in range(len(patterns)):
            current_word=patterns[i]
            if current_word in word:
                    count+=1
        return count