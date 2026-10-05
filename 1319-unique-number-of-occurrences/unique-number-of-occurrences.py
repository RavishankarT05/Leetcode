class Solution(object):
    def uniqueOccurrences(self, arr):
        arr1=set(arr[:])
        ans=[]
        for i in arr1:
            ans.append(arr.count(i))      
        return len(ans)==len(set(ans))
        