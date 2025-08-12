#question
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
#code
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = list(set(nums))
        a.sort(reverse=True)
        if len(a) >= 3:
            return a[2]
        else:
            return a[0]