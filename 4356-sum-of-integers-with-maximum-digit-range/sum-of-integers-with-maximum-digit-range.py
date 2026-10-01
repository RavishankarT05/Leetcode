class Solution(object):
    def maxDigitRange(self, nums):
        arr=[]
        ans=[]
        for i in nums:
            a=list(map(int,str(i)))
            arr.append(max(a)-min(a))
        count=arr.count(max(arr))
        value=max(arr)
        print(count)
        print(value)
        for i in range(count):
            ans.append(nums[arr.index(value)])
            arr[arr.index(value)]=-1
        return sum(ans)

            

        