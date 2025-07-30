#question
# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
#code:
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a = []
        b = []
        Sum = 0
        for i in nums:
            if i in a:
                b.append(i)
            else:
                a.append(i)
        for j in b:
            if j in a:
                a.remove(j)
        for k in a:
            Sum += k 
        return Sum
