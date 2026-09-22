class Solution(object):
    def reverse(self, x):
        if x<0:
            x=-1*x
            x=str(x)
            x=x[::-1]
            x=-1*int("".join(map(str, x)))
        else:
            x=str(x)
            x=x[::-1]
            x=int("".join(map(str, x)))
        if x>2147483647 or x<-2147483648:
            return 0
        else:
            return x