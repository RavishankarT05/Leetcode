class Solution(object):
    def findTheArrayConcVal(self, nums):
        a,b=0,-1
        con=0
        while True:
            if len(nums)==1:
                con+=nums[a]
            if len(nums)<=1:
                break
            con+=int(str(nums[a]) + str(nums[b]))
            nums=nums[1:-1:]
        return con
        