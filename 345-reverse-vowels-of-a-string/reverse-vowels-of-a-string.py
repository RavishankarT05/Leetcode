class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        a,b=0,len(s)-1
        c=['A','E','I','O','U','a','e','i','o','u']
        while a<b:
            if s[a] not in c:
                a+=1
            if s[b] not in c:
                b-=1
            if s[a] in c and s[b] in c:
                s[a],s[b]=s[b],s[a]
                a+=1
                b-=1
        return "".join(s)
