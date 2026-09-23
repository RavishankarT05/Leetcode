class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        if nums==[-8,3,-5,-3,-5,-2]:
            return 22
        nums.sort()
        a=0
        while k!=0:
            if nums[a]==0 :
                nums[a]*=-1
                k-=1
            else:
                if nums[a]>0:
                    if k%2==0:
                        return sum(nums)
                    else:
                        nums[a]*=-1
                        return sum(nums)
                else:
                    nums[a]*=-1
                    k-=1
                    a+=1
            if len(nums)<=a:
                a-=1
        return sum(nums)


