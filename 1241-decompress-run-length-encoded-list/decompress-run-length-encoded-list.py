class Solution(object):
    def decompressRLElist(self, nums):
        arr=[]
        i=0
        for i in range(len(nums)/2):
            freq=nums[2*i]
            val=nums[2*i+1]
            for j in range(freq):
                arr.append(val)
        return arr