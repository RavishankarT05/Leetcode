class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        a,b=0,len(s)-1
        c=['A','E','I','O','U','a','e','i','o','u']
        while a<b:
            if s[a] in c:
                if s[b] in c:
                    if s[a] in c and s[b] in c:
                        s[a],s[b]=s[b],s[a]
                        a+=1
                        b-=1
                else:
                    b-=1
            else:
                a+=1
        return "".join(s)
