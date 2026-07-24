class Solution(object):
    def generate(self, numRows):
        a=[]
        for i in range(numRows):
            count=1
            b=[]
            for j in range(i+1):
                b.append(count)        
                count=count*(i-j)//(j+1)
            a.append(b)
        return a