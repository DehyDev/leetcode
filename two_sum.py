# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        for ix, x in enumerate(nums):
            for iy, y in enumerate(nums):
                if x + y == target and ix != iy:
                    return [ix, iy]
