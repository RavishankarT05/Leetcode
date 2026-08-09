class Solution:
    def findRelativeRanks(self, nums):
        ans = []
        sorted_nums = sorted(nums, reverse=True)
        for n in nums:
            rank = sorted_nums.index(n)
            if rank == 0:
                ans.append('Gold Medal')
            elif rank == 1:
                ans.append('Silver Medal')
            elif rank == 2:
                ans.append('Bronze Medal')
            else:
                ans.append(str(rank + 1))
        return ans