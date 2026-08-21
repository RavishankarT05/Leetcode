class Solution(object):
    def rotateString(self, s, goal):
        for _ in range(len(s)):
            if s[1:]+s[:1]==goal:
                return True
            s=s[1:]+s[:1]
        return False