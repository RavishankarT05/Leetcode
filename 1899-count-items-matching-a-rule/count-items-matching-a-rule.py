class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        if ruleKey=="type":
            index=0
        elif ruleKey=="color":
            index=1
        else:
            index=2
        count=0
        for i in items:
            if i[index]==ruleValue:
                count+=1
        return count