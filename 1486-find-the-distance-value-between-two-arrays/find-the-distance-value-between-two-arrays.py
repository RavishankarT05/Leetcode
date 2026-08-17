class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        f=0
        count=0
        ans=0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<= d:
                    count+=1
            if count==f:
                ans+=1
            else:
                f=count
        return ans