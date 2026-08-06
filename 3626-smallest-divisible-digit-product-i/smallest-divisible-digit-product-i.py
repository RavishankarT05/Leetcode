class Solution(object):
    def smallestNumber(self, n, t):
        def eg(n):
            product=1
            z=n
            while z>0:
                a=z%10
                product*=a
                z//=10
            a=product%t
            if a==0:
                return n
            else:
                return eg(n+1)
        return eg(n)
