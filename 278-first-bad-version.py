# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left=1
        right=n
        isFalse=False
        while left<=right:
            mid=left+(right-left)//2
            isFalse=isBadVersion(mid)
            if isFalse and left==right:
                return right
            if isFalse==False:
                left=mid+1
            elif isFalse==True:
                right=mid


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left=1
        right=n
        isFalse=False
        while left<right:
            mid=left+(right-left)//2
            isFalse=isBadVersion(mid)
            if isFalse==False:
                left=mid+1
            elif isFalse==True:
                right=mid
        return left