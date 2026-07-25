class Solution(object):
    def maxProduct(self, n):
        a=[]
        for i in str(n):
            a.append(i)
        count=0
        a=list(map(int,a))
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                if count<a[i]*a[j]:
                    count=a[i]*a[j]
        return count
        