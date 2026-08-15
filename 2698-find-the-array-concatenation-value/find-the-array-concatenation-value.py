class Solution(object):
    def findTheArrayConcVal(self, nums):
        con=0
        while True:
            if len(nums)==1:
                con+=nums[0]
                break
            if len(nums)==0:
                break
            con+=int(str(nums.pop(0)) + str(nums.pop()))
        return con
        