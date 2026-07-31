class Solution(object):
    def differenceOfSums(self, n, m):
        c=0
        count=0
        for i in range(1,n+1):
            if i%m==0:
                c+=i
            else:
                count+=i
        else:
            return count-c