class Solution(object):
    def addDigits(self, num):
        num=list(map(int,str(num)))
        while True:
            if sum(num)<=9:
                return sum(num)
            else:
                num=list(map(int,str(sum(num))))


        