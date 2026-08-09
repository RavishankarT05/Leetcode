class Solution:
    def findErrorNums(self, nums):
        m=sum(nums)-sum(set(nums))
        exp =len(nums)*(len(nums)+1)//2
        print(exp)
        t= exp-sum(set(nums))
        return  [m,t]
        


