class Solution(object):
    def validPalindrome(self, s):
        a,b=0,len(s)-1
        while a<b:
            if s[a]==s[b]:
                a+=1
                b-=1
            else:
                z=s[a+1:b+1]
                y=s[a:b]
                return z==z[::-1] or y==y[::-1]
        return True