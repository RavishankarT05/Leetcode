class Solution(object):
    def absDifference(self, nums, k):
        nums.sort()
        a=0
        b=0
        c,d=0,-1
        for i in range(k):
            a+=nums[c]
            b+=nums[d]
            c+=1
            d-=1
        return b-a