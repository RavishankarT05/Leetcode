# class Solution(object):
#     def replaceElements(self, arr):
#         ans=[]
#         a=1
#         while a<len(arr):
#             ans.append(max(arr[a:]))
#             a+=1
#         if a==1:
#             return [-1]
#         ans.append(-1)
#         return ans

class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        maxRight = -1 
        for i in range(n - 1, -1, -1):
            current = arr[i]
            arr[i] = maxRight
            maxRight = max(maxRight, current)
        return arr



















        # a,b=0,1
        # c=0
        # while a<len(arr) and b<len(arr):
        #     if arr[a]<arr[b]:
        #         arr[a]=arr[b]
        #         c+=1
        #     b+=1
        #     if len(arr)<=b:
        #         if c==0:
        #             arr[a]=-1
        #             c=0
        #         print(arr[a])    
        #         a+=1
        #         b=a+1
        # arr[-1]=-1
        # return arr