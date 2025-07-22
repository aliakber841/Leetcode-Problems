class Solution:
    def generateParenthesis(self, n):
        def backtrack(position,open_bracket,close_bracket,current):
            if position==2*n:
                result.append("".join(current))
                return
            if open_bracket>0:
                current[position]='('
                backtrack(position+1,open_bracket-1,close_bracket,current)
            if close_bracket>open_bracket:
                current[position]=')'
                backtrack(position+1,open_bracket,close_bracket-1,current)
        result=[]
        current=['']*(2*n)
        backtrack(0,n,n,current)
        return result