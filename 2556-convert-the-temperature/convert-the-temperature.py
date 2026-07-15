class Solution(object):
    def convertTemperature(self, celsius):
        a=[]
        k=celsius+273.1500
        a.append(k)
        f=celsius*1.800+32
        a.append(f)
        return a

        