class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        z=[]
        a,b=0,-1
        while True:
            print(nums)
            z.append((nums[a]+nums[b])/2.0)
            nums.remove(nums[a])
            nums.remove(nums[b])
            if len(nums)==0:
                break
        return min(z)










        # a=[]
        # for i in range(len(nums)/2):
        #     a.append((min(nums) + max(nums)) / 2.0)
        #     nums.remove(min(nums))
        #     nums.remove(max(nums))
        # return min(a)
