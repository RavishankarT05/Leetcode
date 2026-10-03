class Solution(object):
    def maxNumberOfBalloons(self, text):
        arr=[]
        count=0
        for i in "balon":
            arr.append(text.count(i))
        if len(arr)!=5:
            return 0
        while arr[0]!=0 and arr[1]!=0 and arr[2]>=2 and arr[3]>=2 and arr[4]!=0:
            count+=1
            arr[0]-=1 
            arr[1]-=1 
            arr[2]-=2
            arr[3]-=2
            arr[4]-=1
        return count


