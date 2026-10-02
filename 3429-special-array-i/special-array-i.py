class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums)==1:
            return True
        a,b=0,1
        while b<len(nums):
            if (nums[a]%2!=0 and nums[b]%2==0) or (nums[a]%2==0 and nums[b]%2!=0):
                pass
            else:
                return False
            a+=1
            b+=1
        return True
        