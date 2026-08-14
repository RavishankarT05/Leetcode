class Solution(object):
    def firstMatchingIndex(self, s):
        # a,b=0,len(s)-1
        # while a<=b:
        #     if s[a]==s[b]:
        #         return a
        #     a+=1
        #     b-=1
        # return -1





        count=0
        for i in range(len(s)):
            if s[i]==s[len(s)-i-1]:
                return i
        return -1