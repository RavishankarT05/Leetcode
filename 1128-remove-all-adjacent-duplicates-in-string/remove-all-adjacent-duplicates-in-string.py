class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for i in s:
            if i not in stack:
                stack.append(i)
            else:
                a=stack[-1]
                if a==i:
                    stack.pop()
                else:
                    stack.append(i)
        return "".join(stack)
        