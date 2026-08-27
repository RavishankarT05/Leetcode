class Solution(object):
    def trimTrailingVowels(self, s):
        a=s
        for i in range(len(a)-1,-1,-1):
            if s[i] in ['a','e','i','o','u']:
                s=s[:-1]
            else:
                break
        return s
        