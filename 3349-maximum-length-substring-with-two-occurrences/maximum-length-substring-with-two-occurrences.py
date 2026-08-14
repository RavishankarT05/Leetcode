class Solution(object):
    def maximumLengthSubstring(self, s):
        s=list(s)
        a=[]
        b=[]
        z=0
        while z<len(s):
            a.append(s[z])
            if a.count(s[z])>2:
                b.append(len(a)-1)
                s=s[1::]
                a=[]
                z=0
            else:
                z+=1
        b.append(len(a))
        return max(b)
