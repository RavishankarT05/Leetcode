class Solution(object):
    def getRow(self, rowIndex):
        a=[]
        for i in range(rowIndex+1):
            count=1
            b=[]
            for j in range(i+1):
                b.append(count)        
                count=count*(i-j)//(j+1)
            a.append(b)
        return a[rowIndex]
        