class Solution(object):
    def truncateSentence(self, s, k):
        a=""
        array=s.split()
        for i in range(0,k):
            a+=array[i]+ " "
        return a.strip()
# .strip() method is a built-in string function used to remove any leading and trailing 
# characters from a string
# the split() method is used to break a string into a list of substrings based 
# on a specified delimiter.

class Solution(object):
    def truncateSentence(self, s, k):
        array=s.split()
        return " ".join(array[:k])
# the join() method is a powerful and efficient string method used 
# to concatenate elements of an iterable (like a list, 
# tuple, or set) into a single string, using a specified separator.
# The join() method takes that list of words and concatenates them into a single string, 
# with " " (space) as the separator.