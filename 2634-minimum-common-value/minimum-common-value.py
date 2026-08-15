class Solution(object):
    def getCommon(self, nums1, nums2):
        a,b=0,0
        while a<len(nums1) and b<len(nums2):
            if nums1[a]==nums2[b]:
                return nums1[a]
            else:
                if nums1[a]<nums2[b]:
                    a+=1
                else:
                    b+=1
        return -1



        