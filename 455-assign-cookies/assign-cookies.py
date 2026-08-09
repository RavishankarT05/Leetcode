class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count=0
        a,b=0,0
        while len(g)>a and len(s)>b:
            if g[a]<=s[b]:
                count+=1
                a+=1
                b+=1
            else:
                b+=1
        return count    