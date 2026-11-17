class Solution(object):
    def subarraySum(self, nums, k):
        current_sum=0
        answer=0
        hash_table={0:1}
        for i in range(len(nums)):
            current_sum+=nums[i]
            target=current_sum-k
            if target in hash_table:
                answer+=hash_table[target]
            if current_sum in hash_table:
                hash_table[current_sum]+=1
            else:
                hash_table[current_sum]=1
        return answer
class Solution(object):
    def subarraySum(self, nums, k):
        if len(nums)==0:
            return 0
        current_sum=0
        no_of_sub_arrays=0
        sum_count={0:1}
        for i in range(len(nums)):
            current_sum+=nums[i]
            target=current_sum-k
            if target in sum_count:
                no_of_sub_arrays+=sum_count[target]
            if current_sum in sum_count:
                sum_count[current_sum]+=1
            else:
                sum_count[current_sum]=1
        return no_of_sub_arrays