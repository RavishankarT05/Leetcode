class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        index = {"type": 0, "color": 1, "name": 2}[ruleKey]
        return sum(item[index] == ruleValue for item in items)