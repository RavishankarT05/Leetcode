class Solution(object):
    def minimumAverage(self, nums):
        a=[]
        for i in range(len(nums)/2):
            a.append((min(nums) + max(nums)) / 2.0)
            nums.remove(min(nums))
            nums.remove(max(nums))
        return min(a)
        
        # a = []
        # for i in range(len(nums) // 2):
        #     mn = min(nums)
        #     mx = max(nums)
        #     a.append((mn + mx) / 2.0)
        #     nums.remove(mn)
        #     nums.remove(mx)
        # return min(a) 