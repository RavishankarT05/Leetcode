class Solution(object):
    def sumOfSquares(self, nums):
        count=0
        a=len(nums)
        for i in range(1,a+1):
            if a%i==0:
                count+= nums[i-1]*nums[i-1]
        return count
        