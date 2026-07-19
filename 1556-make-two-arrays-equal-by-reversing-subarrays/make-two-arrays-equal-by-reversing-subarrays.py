class Solution(object):
    def canBeEqual(self, target, arr):

        for i in arr:
            if i not in target or arr.count(i)!=target.count(i):
                return False
        return True
        