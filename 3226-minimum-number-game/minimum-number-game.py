class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        a=[]
        z,y=0,1
        while z<len(nums):
            a.append(max(nums[z],nums[y]))
            a.append(min(nums[z],nums[y]))
            z+=2
            y+=2
        return a
