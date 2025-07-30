#question:
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
# Example 1:
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
#code:
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        Sum = 0
        for i in str(n):
            mul *= int(i)
        for j in str(n):
            Sum += int(j)
        result = mul - Sum
        return result
