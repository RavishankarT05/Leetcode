class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        sign = ""

        if num < 0:
            sign = "-"
            num = abs(num)

        ans = ""

        while num > 0:
            rem = num % 7
            ans = str(rem) + ans
            num //= 7

        return sign + ans