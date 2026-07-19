class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr=list(sorted(arr))
        count=arr[1]-arr[0]
        for i in range (len(arr)-1):
            if arr[i]+count!=arr[i+1]:
                return False
        return True
