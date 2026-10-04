class Solution(object):
    def countCommas(self, n):
        if 1000<=n<=100000:
            return n-999
        else:
            return 0

        