class Solution(object):
    def isValid(self, s):
        a=0
        stack=[]
        while a<len(s):
            if s[a] in "({[":
                stack.append(s[a])
            else:
                if not stack:
                    return False
                top=stack.pop()
                if s[a]=='}' and top!='{':
                    return False
                if s[a]==')' and top!='(':
                    return False
                if s[a]==']' and top!='[':
                    return False
            a+=1
        return not stack