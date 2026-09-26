class Solution(object):
    def countGoodSubstrings(self, s):
        arr=[]
        a=0
        b=1
        c=2
        count=0
        while c<len(s):
            arr1=[]
            arr1.append(str(s[a]))
            arr1.append(str(s[b]))
            arr1.append(str(s[c]))
            a+=1
            b+=1
            c+=1
            arr.append(arr1)
        for i in arr:
            if len(i)==len(set(i)):
                count+=1
        return count