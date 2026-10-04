class Solution(object):
    def countCommas(self, n):
        count=0
        a=1000
        while a<=100000:
            if a<=n:
                count+=1
            else:
                return count
            a+=1
        return count

        