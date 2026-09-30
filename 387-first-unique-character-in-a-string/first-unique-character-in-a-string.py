# class Solution(object):
#     def firstUniqChar(self, s):
        # a=0
        # while a<len(s):
        #     if s.count(s[a])==1:
        #         return a
        #     a+=1
        # return -1

class Solution(object):
    def firstUniqChar(self, s):
        a=0
        arr=[]
        for i in s:
            if i not in arr:
                arr.append(i)
        print(arr)
        while a<len(arr):
            if s.count(arr[a])==1:
                return s.index(arr[a])
            a+=1
        return -1