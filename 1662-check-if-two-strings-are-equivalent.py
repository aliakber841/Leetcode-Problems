class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        delimiter=""
        word1=delimiter.join(word1)
        word2=delimiter.join(word2)
        return word1==word2