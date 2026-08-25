class Solution(object):
    def missingMultiple(self, nums, k):
        a=k
        while True:
            if k not in nums:
                return k
            k+=a
