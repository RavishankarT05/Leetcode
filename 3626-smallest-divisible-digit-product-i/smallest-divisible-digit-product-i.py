class Solution(object):
    def smallestNumber(self, n, t):
        # def eg(n):
        #     product=1
        #     z=n
        #     while z>0:
        #         a=z%10
        #         product*=a
        #         z//=10
        #     if product%t==0:
        #         return n
        #     else:
        #         return eg(n+1)
        # return eg(n)
        while True:
            product=1
            x=n
            while x>0:
                a=x%10
                product*=a
                x//=10
            if product%t==0:
                return n
            n+=1


