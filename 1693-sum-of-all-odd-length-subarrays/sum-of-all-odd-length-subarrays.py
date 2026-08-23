class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        summ = 0
        for i in range(1,len(arr)+1,2):
            for j in range(len(arr)):
                if(j+i<=len(arr)):
                    summ+=sum(arr[j:i+j])
        return summ