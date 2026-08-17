class Solution(object):
    def diStringMatch(self, s):
        z=[]
        a=0
        b=len(s)
        for i in s:
            if i=="I":
                z.append(a)
                a+=1
            else:
                z.append(b)
                b-=1
        if s[len(s)-1]=="I":
            z.append(a)
        else:
            z.append(b)
        return z