class Solution(object):
    def removeElement(self, nums, val):
        a=nums.count(val)
        while a!=0:
            nums.remove(val)
            a-=1
        