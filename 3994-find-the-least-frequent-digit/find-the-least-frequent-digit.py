class Solution(object):
    def getLeastFrequentDigit(self, n):
        arr=list(str(n))
        a=sorted(set(str(n)))
        count=1000
        num=0
        print(arr)
        print(a)
        for i in a:
            if arr.count(i)<count:
                count=arr.count(i)
                num=int(i)
        return num
