class Solution(object):
    def isPerfectSquare(self, num):
        a=1
        while a*a<=num:
            if a*a==num:
                return True
            a+=1
        return False