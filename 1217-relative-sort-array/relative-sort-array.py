class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr=[]
        a=0
        b=0
        while b<len(arr2):
            if len(arr1)<=a:
                a=0
                b+=1
            else:
                if arr1[a]==arr2[b]:
                    arr.append(arr1[a])
                    a+=1
                else:
                    a+=1
        arr1.sort()
        for i in arr1:
            if i not in arr2:
                arr.append(i)
        return arr