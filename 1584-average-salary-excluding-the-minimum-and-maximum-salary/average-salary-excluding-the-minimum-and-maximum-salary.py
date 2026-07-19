class Solution(object):
    def average(self, salary):
        a=list(sorted(salary))
        count=0.00000
        del a[0]
        del a[-1]
        for i in a:
            count+=i
        return count/len(a)