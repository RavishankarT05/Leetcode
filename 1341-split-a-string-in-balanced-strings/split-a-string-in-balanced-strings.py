class Solution(object):
    def balancedStringSplit(self, s):
        count=0
        a=0
        for i in s:
            if i=="R":
                a+=1
            elif i=="L":
                a-=1
            if a==0:
                count+=1
        return count