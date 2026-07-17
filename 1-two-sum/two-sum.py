class Solution(object):
    def twoSum(self, nums, target):
        a=[]
        for i in range(len(nums)-1):
            for j in range(i,len(nums)-1):
                if nums[i]+nums[j+1]==target:
                    a.append(i)
                    a.append(j+1)
        return list(set(a))


        