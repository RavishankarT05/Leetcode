class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        arr1=[]
        d=abs(arr[0]-arr[1])
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])<d:
                d=abs(arr[i]-arr[i+1])
        a,b=0,1
        while b<len(arr):
            q=[]
            if d==abs(arr[a]-arr[b]):
                q.append(arr[a])
                q.append(arr[b])
            a+=1
            b+=1
            if q:
                arr1.append(q)
        return arr1


        