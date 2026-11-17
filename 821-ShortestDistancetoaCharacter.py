class Solution(object):
    def shortestToChar(self, s, c):
        result=len(s)*[0]
        latest_seen=0
        previous=-1
        for i in range(len(s)):
            if s[i]==c:
                result[i]=0
                while latest_seen<i:
                    if previous==-1:
                        result[latest_seen]=i-latest_seen
                    else:
                        result[latest_seen]=min(i-latest_seen, latest_seen-previous)
                    latest_seen+=1
                latest_seen=i+1
                previous=i
        
        while latest_seen<len(s):
            result[latest_seen]=latest_seen-previous
            latest_seen+=1
        return result    