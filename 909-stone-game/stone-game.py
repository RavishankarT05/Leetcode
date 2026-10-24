class Solution(object):
    def stoneGame(self, piles):
        a=0
        b=0
        c=0
        while piles:
            piles.sort()
            if c%2==0:
                d=max(piles)
                a+=d
                piles.remove(d)
            else:
                d=max(piles)
                a+=d
                piles.remove(d)
        return a>b
        