class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        # num=sorted(nums)
        # a,b=0,len(nums)-1
        # while a<b:
        #     if (num[a]+num[b])==target:
        #         z=nums.index(num[a])
        #         y=nums.index(num[b])
        #         return [z,y]
        #     elif (num[a]+num[b])<target:
        #         a+=1
        #     elif (num[a]+num[b])>target:
        #         b-=1
            

        