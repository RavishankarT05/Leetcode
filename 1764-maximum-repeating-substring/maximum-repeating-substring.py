class Solution(object):
    def maxRepeating(self, sequence, word):
        count=0
        arr=word[:]
        while True:
            if arr in sequence:
                count+=1
                arr+=word
            else:
                return count