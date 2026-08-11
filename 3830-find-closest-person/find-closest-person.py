class Solution(object):
    def findClosest(self, x, y, z):
        a=max(x,z)-min(x,z)
        b=max(y,z)-min(y,z)
        if a<b:
            return 1
        elif b<a:
            return 2
        else:
            return 0