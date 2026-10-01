class Solution(object):
    def sortPeople(self, names, heights):
        h=sorted(heights[:])
        h.reverse()
        arr=[]
        for i in h:
            arr.append(names[heights.index(i)])
        return arr
        