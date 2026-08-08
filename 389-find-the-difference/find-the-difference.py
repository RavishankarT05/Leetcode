class Solution(object):
    def findTheDifference(self, s, t):
        s=sorted(s)
        t=sorted(t)
        for i in t:
            if i not in s:
                return i
            else:
                s=s[1:]
        