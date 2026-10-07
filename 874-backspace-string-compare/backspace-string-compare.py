class Solution(object):
    def backspaceCompare(self, s, t):
        stack1=[]
        stack2=[]
        for i in range(len(s)):
            if s[i]!="#":
                stack1.append(s[i])
            else:
                if len(stack1)==0:
                    pass
                else:
                    stack1.pop()
        for i in range(len(t)):
            if t[i]!="#":
                stack2.append(t[i])
            else:
                if len(stack2)==0:
                    pass
                else:
                    stack2.pop()
        print(stack1)
        print(stack2)
        if len(stack1)!=len(stack2):
            return False
        for i in range(len(stack1)):
            if stack1[i]!=stack2[i]:
                return False
        return True