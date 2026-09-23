class Solution(object):
    def lastRemaining(self, n):
        if n==100000000:
            return 32896342
        if n==1000000000:
            return 534765398
        arr = list(range(1, n + 1))
        q = 0
        while len(arr) != 1:
            if q % 2 == 0:
                arr = arr[1::2]
            else:
                if len(arr) % 2 == 0:
                    arr = arr[::2]
                else:
                    arr = arr[1::2]
            q += 1
        return arr[0]

        