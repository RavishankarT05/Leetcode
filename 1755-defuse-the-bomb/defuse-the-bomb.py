class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        res = []

        for i in range(n):
            s = 0

            if k > 0:
                for j in range(1, k + 1):
                    s += code[(i + j) % n]

            elif k < 0:
                for j in range(1, abs(k) + 1):
                    s += code[(i - j) % n]

            res.append(s)

        return res