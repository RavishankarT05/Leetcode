class Solution(object):
    def minimumAverage(self, nums):
        a=[]
        for i in range(len(nums)/2):
            a.append((min(nums) + max(nums)) / 2.0)
            nums.remove(min(nums))
            nums.remove(max(nums))
        return min(a)
