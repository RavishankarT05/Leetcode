class Solution(object):
    def firstMatchingIndex(self, s):
        count=0
        for i in range(len(s)):
            if s[i]==s[len(s)-i-1]:
                return i
        return -1