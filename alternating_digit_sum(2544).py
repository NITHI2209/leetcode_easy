#question
# You are given a positive integer n. Each digit of n has a sign according to the following rules:
# The most significant digit is assigned a positive sign.
# Each other digit has an opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.
# Example 1:
# Input: n = 521
# Output: 4
# Explanation: (+5) + (-2) + (+1) = 4.
#code:
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        lst = list(map(int,str(n)))
        count = 0
        for i in range(len(lst)):
            if i % 2 == 0:
                count += lst[i]
            else:
                count -= lst[i]
        return count