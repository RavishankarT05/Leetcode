class Solution(object):
    def clearDigits(self, s):
        stack=[]
        for i in s:
            if i.isalpha():
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)

        