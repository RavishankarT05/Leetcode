class Solution(object):
    def strStr(self, haystack, needle):
        z=0
        count=0
        a,b=0,0
        c=len(haystack)
        d=len(needle)
        if c<d:
            return -1
        while a<c and b<d:
            if haystack[a]!=needle[b]:
                count+=1
                a=count
                b=0
            else:
                a+=1
                b+=1
        if b==d:
            return a-b
        else:
            return -1
            


    






# class Solution(object):
#     def strStr(self, haystack, needle):
#         count=0
#         a,b=0,0
#         c=len(haystack)
#         d=len(needle)
#         if c<d:
#             return -1
#         while a<c and b<d:
#             if len(haystack)<=a:
#                 break
#             if haystack[a]==needle[b]:
#                 a+=1
#                 b+=1
#             else:
#                 haystack=haystack[1::]
#                 count-=b
#                 a=0
#                 b=0
#             count+=1
#         print(count,b)
#         if b==0:
#             return -1