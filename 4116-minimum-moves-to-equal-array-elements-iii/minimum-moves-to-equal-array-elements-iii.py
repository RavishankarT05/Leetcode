class Solution(object):
    def minMoves(self, nums):
        count=0
        a=max(nums)
        nums.remove(a)
        for i in nums:
            while i!=a:
                count+=1
                i+=1
        return count
        