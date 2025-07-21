class Solution(object):
    def isValid(self, s):
        if not s:
            return True
        brackets_pair={')':'(' ,   '}':'{'  ,']':'['}
        stack=[]
        for i in range(len(s)):
            if s[i] in brackets_pair.values():
                stack.append(s[i])
            elif not stack or stack.pop()!=brackets_pair[s[i]]:
                return False
        return not stack