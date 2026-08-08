class Solution(object):
    def minimumBoxes(self, apple, capacity):
        capacity=sorted(capacity,reverse=True)
        count=capacity[0]
        s=sum(apple)
        a=1
        index=1
        while True:
            if s<=count:
                print(count)
                return index
            else:
                count+=capacity[a]
                a+=1
                index+=1
        