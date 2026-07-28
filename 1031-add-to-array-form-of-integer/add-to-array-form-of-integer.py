class Solution(object):
    def addToArrayForm(self, num, k):
        # n=int("".join(map(str,num)))
        # # n=n+k
        # return list(map(int,str(n+k)))
        num_val = int("".join([str(x) for x in num])) 
        num_val += k
        return [int(x) for x in (list(str(num_val)))]