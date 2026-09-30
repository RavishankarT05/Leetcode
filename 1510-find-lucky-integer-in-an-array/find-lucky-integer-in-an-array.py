class Solution(object):
    def findLucky(self, arr):
        arr2=list(set(arr[:]))
        a=len(arr2)-1
        while -1<a:         
            if arr2[a]==arr.count(arr2[a]):
                return arr2[a]
            a-=1
        return -1
        