class Solution(object):
    def isHappy(self, n):
        for i in range(10):
            n=list(map(int,str(n)))
            n=[num ** 2 for num in n]
            n=sum(n)
            if n==1:
                return True
            print(n)
        else:
            return False

