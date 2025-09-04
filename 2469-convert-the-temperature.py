class Solution(object):
    def convertTemperature(self, celsius):
        result=[]
        kelvin=celsius+273.15
        result.append(kelvin)
        fahrenheit=(celsius*1.80)+32.00
        result.append(fahrenheit)
        return result