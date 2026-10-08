class Solution(object):
    def maxDepth(self, s):
        count=0
        ans=0
        for i in s:
            if i=="(":
                count+=1
            elif i==")":
                count-=1
            if ans<count:
                ans=count
        return ans
        