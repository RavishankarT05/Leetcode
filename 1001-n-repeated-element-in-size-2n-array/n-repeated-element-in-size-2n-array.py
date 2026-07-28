class Solution(object):
    def repeatedNTimes(self, nums):
        b=set()
        for i in nums:
            if i in b:
                return i
            b.add(i)

# class Solution:
#     def repeatedNTimes(self, nums):
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return num
#             seen.add(num)