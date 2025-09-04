class Solution(object):
    def findClosest(self, x, y, z):
        if z>x:
            person_one=z-x
        else:
            person_one=x-z
        if z>y:
            person_two=z-y
        else:
            person_two=y-z
        if person_one>person_two:
            return 2
        elif person_one<person_two:
            return 1
        else:
            return 0