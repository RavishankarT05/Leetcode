class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        a=list(map(int,str(x)))
        a=sum(a)
        if x%a==0:
            return a
        return -1