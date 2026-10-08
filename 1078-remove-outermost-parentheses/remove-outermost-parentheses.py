class Solution(object):
    def removeOuterParentheses(self, s):
        count=0
        ans=""
        stack=[]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(s[i])
                count+=1
            else:
                stack.append(s[i])
                count-=1
            if count==0:
                stack.pop(0)
                stack.pop() 
                ans+="".join(stack)
                stack=[]
        return ans

