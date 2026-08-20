class Solution(object):
    def splitNum(self, num):
        num= "".join(sorted(str(num)))
        a=str(num)[::2]
        b=str(num)[1::2]
        return int(a)+int(b)