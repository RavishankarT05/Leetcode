class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        count=numBottles
        while numBottles>=numExchange:
            numBottles=numBottles-numExchange+1
            count+=1
        return count

        