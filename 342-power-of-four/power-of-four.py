class Solution(object):
    def isPowerOfFour(self, n):
        a=0
        while 4**a<=n:
            if 4**a==n:
                return True
            else:
                a+=1
        return False
        