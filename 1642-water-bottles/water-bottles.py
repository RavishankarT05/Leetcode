class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        # count=numBottles
        # while numBottles>=numExchange:
        #     numBottles=numBottles-numExchange+1
        #     count+=1
        # return count

        # count=0
        # while numBottles>=numExchange:
        #     a=(numBottles//numExchange)
        #     count+=numExchange*a
        #     numBottles=a+(numBottles%numExchange)
        # count+=numBottles
        # return count
        return numBottles + (numBottles-1)//(numExchange-1)
                