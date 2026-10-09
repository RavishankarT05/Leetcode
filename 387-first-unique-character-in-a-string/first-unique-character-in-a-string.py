class Solution(object):
    def firstUniqChar(self, s):
        a=0
        arr=[]
        for i in s:
            if i not in arr:
                arr.append(i)
        while a<len(arr):
            if s.count(arr[a])==1:
                return s.index(arr[a])
            a+=1
        return -1
