class Solution:
    def twoSum(self, nums, target):
        prevMap = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in prevMap:
                return [prevMap[dif], i]
            prevMap[n] = i