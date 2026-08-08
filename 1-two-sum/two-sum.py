class Solution(object):
    def twoSum(self, nums, target):
        a=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    a.append(i)
                    a.append(j)
                    return a
        # a,b=0,len(nums)-1
        # while a<=len(nums) and b>=0:
        #     if (nums[a])+(nums[b])==target:
        #         return [a,b]
        #     elif (nums[a])+(nums[b])<target:
        #         a+=1
        #     elif (nums[a])+(nums[b])>target:
        #         b-=1
            

        