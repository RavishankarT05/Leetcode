class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        return [sum(sum(grid, [])) - sum(set(sum(grid, []))),(set(range(1, len(sum(grid, [])) + 1)) - set(sum(grid, []))).pop()]
        # a = sum(grid, [])
        # a.sort()
        # z=[]
        # y=0
        # x=0
        # for i in range(len(a)) :
        #     if a[i] not in z:
        #         z.append(a[i])
        #     else:
        #         y+=a[i]
        #     if i+1 not in a:
        #         x+=i+1
        # return [y,x] 
        