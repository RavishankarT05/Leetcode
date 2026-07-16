class Solution(object):
    def removeDuplicates(self, nums):
        for i in nums:
            a=nums.count(i)
            while a>1:
                nums.remove(i)
                a-=1

