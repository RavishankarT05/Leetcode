class Solution(object):
    def containsDuplicate(self, nums):
        # a=[]
        # for i in nums:
        #     if i in a:
        #         return True
        #     else:
        #         a.append(i)
        # return False
        if len(nums)==len(set(nums)):
            return False
        else:
            return True