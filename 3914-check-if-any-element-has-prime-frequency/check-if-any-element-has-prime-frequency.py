class Solution(object):
    def checkPrimeFrequency(self, nums):
        arr=[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # for i in range(2,len(nums)+1):
        #     for j in range(2,int(i**0.5)+1):
        #         if i%j==0:
        #             break
        #     else:
        #         arr.append(i)
        arr1=list(set(nums[:]))
        for i in arr1:
            if nums.count(i) in arr:
                return True
        return False
