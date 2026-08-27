class Solution(object):
    def rearrangeString(self, s, x, y):
        s=list(s)
        a,b=0,len(s)-1
        while a<b:

            if s[a]==x and s[b]==y:
                s[a],s[b]=s[b],s[a]
                a+=1
                b-=1
            if s[a]!=x:
                a+=1
            if s[b]!=y:
                b-=1
        
        return "".join(s)
