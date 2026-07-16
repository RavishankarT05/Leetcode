class Solution(object):
    def isPalindrome(self, s):
        a=s.strip()
        a=a.lower()
        b=re.sub(r'[^a-zA-Z0-9]','',a)
        return str(b)==str(b)[::-1]