class Solution(object):
    def gcdOfOddEvenSums(self, n):
        a=n*n
        b=n*(n+1)
        while b:
            a,b=b,a%b
        return a
        