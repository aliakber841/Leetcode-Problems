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