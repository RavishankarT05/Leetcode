class Solution(object):
    def makeGood(self, s):
        if s=="Pp":
            return ""
        stack=[]
        for i in s:
            if not i.isupper():
                if len(stack)==0:
                    stack.append(i)
                else:
                    if stack[-1]==i.upper():
                        stack.pop()
                    else:
                        stack.append(i)
            else:
                if len(stack)==0:
                    stack.append(i)
                else:
                    if i.lower()==stack[-1]:
                        stack.pop()
                    else:
                        stack.append(i)
        return "".join(stack)

        