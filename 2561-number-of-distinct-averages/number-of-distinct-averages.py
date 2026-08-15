class Solution(object):
    def distinctAverages(self, nums):
        nums.sort()
        ans=[]
        while len(nums)>0:
            ans.append((nums[0]+nums[-1])/2.0)
            nums.pop(0)
            nums.pop()
        return len(set(ans))
        
        