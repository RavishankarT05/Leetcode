class Solution(object):
    def findMaxAverage(self, nums, k):
        maxx=sum(nums[:k])
        w=[]
        w.append(maxx)
        a,b=0,k
        while b<len(nums):
            maxx=(maxx-nums[a])+nums[b]
            w.append(maxx)
            a+=1
            b+=1
        return (max(w)+0.0)/k