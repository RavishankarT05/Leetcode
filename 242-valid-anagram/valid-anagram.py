class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
            arr=list(set(s))
            for i in arr:
                if s.count(i)!=t.count(i):
                    return False
                if i not in t:
                    return False
            return True
        else:
            return False
