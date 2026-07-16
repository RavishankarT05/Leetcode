class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1.extend(nums2)
        nums1.sort()
        while n!=0:
            nums1.remove(0)
            n-=1