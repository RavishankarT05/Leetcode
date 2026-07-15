class Solution(object):
    def countDigits(self, num):
        a=list(map(int,str(num)))
        count=0
        for i in a:
            if num%i==0:
                count+=1
        return count
        
    
        
        