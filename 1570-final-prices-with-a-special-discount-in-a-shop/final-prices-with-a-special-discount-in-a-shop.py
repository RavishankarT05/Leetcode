class Solution(object):
    def finalPrices(self, prices):
        arr=[]
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    arr.append(prices[i]-prices[j])
                    break
            else:
                arr.append(prices[i])
        arr.append(prices[-1])
        return arr

