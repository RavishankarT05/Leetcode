class Solution(object):
    def subtractProductAndSum(self, n):
        a=list(map(int,str(n)))
        pro=1
        sum=0
        for i in a:
            pro*=i
        for j in a:
            sum+=j
        return pro-sum