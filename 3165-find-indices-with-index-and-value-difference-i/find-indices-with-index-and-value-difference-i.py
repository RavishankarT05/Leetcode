class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        i,j=0,0
        while i<len(nums):
            if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                return [i,j]
            else:
                j+=1
            if j>=len(nums):
                i+=1
                j=i



        return [-1,-1]