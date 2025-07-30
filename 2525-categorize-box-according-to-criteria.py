class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        string=""
        volume=length*width*height
        if mass>=100:
            string+="Heavy"
        if length>=10000 or width>=10000 or height>=10000 or volume>=10**9:
            string+="Bulky"
        if "Heavy" in string and "Bulky" in string:
            return "Both"
        if not string:
            return "Neither"
        else:
            return string  