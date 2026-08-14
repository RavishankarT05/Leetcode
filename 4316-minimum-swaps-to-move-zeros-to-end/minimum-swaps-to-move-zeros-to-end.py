class Solution(object):
    def minimumSwaps(self, nums):
        count=0
        a,b=0,len(nums)-1
        while a<b:
            if nums[a]!=0:
                a+=1 
            if nums[b]==0:
                b-=1
            if a<b:
                if nums[a]==0 and nums[b]!=0:
                    nums[a],nums[b]=nums[b],nums[a]
                    count+=1
                    a+=1
                    b-=1
        return count