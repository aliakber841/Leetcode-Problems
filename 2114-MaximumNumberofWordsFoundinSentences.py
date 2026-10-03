class Solution(object):
    def mostWordsFound(self, sentences):
        max_length=0
        for i in range(len(sentences)):
            current_word=sentences[i]
            current=current_word.split(" ")
            if max_length<len(current):
                max_length=len(current)
        return max_length   