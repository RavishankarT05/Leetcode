class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
            for i in s:
                if s.count(i)!=t.count(i):
                    return False
                if i not in t:
                    return False
            return True
        else:
            return False