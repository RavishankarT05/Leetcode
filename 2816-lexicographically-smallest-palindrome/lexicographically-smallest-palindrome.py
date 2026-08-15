class Solution(object):
    def makeSmallestPalindrome(self, s):
        s=list(s)
        a,b=0,len(s)-1
        while a<b:
            if s[a]==s[b]:
                a+=1
                b-=1
            else:
                if ord(s[a])<ord(s[b]):
                    s[b]=s[a]
                else:
                    s[a]=s[b]
                a+=1
                b-=1
        return "".join(s)
