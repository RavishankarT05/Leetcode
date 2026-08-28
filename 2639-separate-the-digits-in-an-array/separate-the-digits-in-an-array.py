class Solution(object):
    def separateDigits(self, nums):
        a=[]
        for i in nums:
            a.append(list(map(int,str(i))))
        return [item for sublist in a for item in sublist]