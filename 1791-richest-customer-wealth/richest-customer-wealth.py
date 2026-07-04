class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth=0
        for i in accounts:
            wealth=sum(i)
            if max_wealth<wealth:
                max_wealth=wealth
        return max_wealth