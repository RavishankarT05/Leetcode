class Solution(object):
    def arrayPairSum(self, nums):
        # nums.sort()
        # a,b=0,1
        # count=0
        # for _ in range(len(nums)/2):
        #     count+=min(nums[a],nums[b])
        #     a+=2
        #     b+=2
        # return count
        nums.sort()
        
        # Step 2: Sum every second element starting from index 0
        return sum(nums[::2])