class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        a,b=0,1
        while b<len(s):
            if abs(int(s[a])-int(s[b]))>2:
                return False
            a+=1
            b+=1
        return True
        