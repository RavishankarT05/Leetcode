class Solution(object):
    def maxFrequencyElements(self, nums):
        num=set(nums[:])
        arr=[]
        for i in num:
            arr.append(nums.count(i))
        return max(arr)*arr.count(max(arr))