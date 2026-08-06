class Solution(object):
    def toggleLightBulbs(self, bulbs):
        a=[]
        b=set(bulbs)
        for i in b:
            count=bulbs.count(i)
            if count%2!=0:
                a.append(i)
        return sorted(a)
            