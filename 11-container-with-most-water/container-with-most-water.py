class Solution(object):
    def maxArea(self, height):
        a,b=0,len(height)-1
        count=0
        while a<b:
            if count<(min(height[a],height[b]))*(b-a):
                count=(min(height[a],height[b]))*(b-a)
            if height[a]<height[b]:
                a+=1
            else:
                b-=1
        return count
        