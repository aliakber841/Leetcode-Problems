class Solution(object):
    def intToRoman(self, num):
        integer_values=[
           1000,900,500,400,100,90,50,40,10,9,5,4,1
        ]
        roman_values=[
            'M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'
        ]
        i=0
        roman_number=''
        while num>0:
            for _ in range(num//integer_values[i]):
                roman_number+=roman_values[i]
                num-=integer_values[i]
            i+=1
        return roman_number
        
