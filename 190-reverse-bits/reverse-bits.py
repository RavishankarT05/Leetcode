class Solution(object):
    def reverseBits(self, n):
        a=format(n, '032b')
        a=a[::-1]
        return int(a,2)

        