class Solution(object):
    def lengthOfLongestSubstring(self, s):
        arr = []
        ans = 0

        for i in s:
            if i in arr:
                arr = arr[arr.index(i) + 1:]

            arr.append(i)

            if len(arr) > ans:
                ans = len(arr)

        return ans