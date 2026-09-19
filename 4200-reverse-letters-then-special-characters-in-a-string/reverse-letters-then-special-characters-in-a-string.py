class Solution(object):
    def reverseByType(self, s):
        s=list(s)
        a,b=0,len(s)-1
        while a<b:
            if s[a].isalpha():
                a+=1
            if s[b].isalpha():
                b-=1
            if not s[a].isalpha() and not s[b].isalpha():
                s[a],s[b]=s[b],s[a]
                a+=1
                b-=1
        a,b=0,len(s)-1
        while a<b:
            if not s[a].isalpha():
                a+=1
            if not s[b].isalpha():
                b-=1
            if s[a].isalpha() and s[b].isalpha():
                s[a],s[b]=s[b],s[a]
                a+=1
                b-=1
        z="".join(map(str,s))
        return z
