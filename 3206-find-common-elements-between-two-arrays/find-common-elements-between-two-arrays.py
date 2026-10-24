class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        ans=[]
        arr=[]
        for i in nums1:
            if i in nums2:
                arr.append(i)
        ans.append(len(arr))
        arr=[]
        for i in nums2:
            if i in nums1:
                arr.append(i)
        ans.append(len(arr))
        return ans
        
        