class Solution(object):
    def maximum69Number (self, num):
        num=list(map(int,str(num)))
        for i in range(len(num)):
            if num[i]==6:
                num[i]=9
                return int("".join(map(str,num)))
        return int("".join(map(str,num)))
        