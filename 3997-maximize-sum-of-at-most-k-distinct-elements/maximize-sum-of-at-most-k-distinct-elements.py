class Solution(object):
    def maxKDistinct(self, nums, k):
        nums=sorted(set(nums))
        a=[]
        while True:
            if k>0 and len(nums)>0 :
                a.append(nums[-1])
                nums.pop()
                k-=1
            else:
                return a