class Solution(object):
    def minPrice(self, prices, discounts):
        z=[]
        prices.sort()
        discounts.sort()
        while 0<len(prices) and 0<len(discounts):
            z.append((prices.pop()*(100.0-discounts.pop()))/100)
        return sum(z+prices)           


        