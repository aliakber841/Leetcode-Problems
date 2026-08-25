class Solution(object):
    def sumGame(self, num):
        half_length=(len(num))/2
        sum_of_left_half=0
        sum_of_right_half=0
        left_q=0
        right_q=0
        for i in range(0,half_length):
            if num[i]=="?":
                left_q+=1
            else:
                sum_of_left_half+=int(num[i])
        for j in range(half_length,len(num)):
            if num[j]=="?":
                right_q+=1
            else:
                sum_of_right_half+=int(num[j])
        sum_difference=sum_of_left_half-sum_of_right_half
        q_difference=left_q-right_q
        return sum_difference*2!=-q_difference*9