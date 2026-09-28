class Solution(object):
    def selfDividingNumbers(self, left, right):
        arr=[]
        for i in range(left,right+1):
            FLAG=True
            a=list(map(int,str(i)))
            for k in a:
                if k==0:
                    FLAG=False
                    continue
                if i%k==0:
                    pass
                else:
                    FLAG=False
            if FLAG:
                arr.append(i)
        return arr
                