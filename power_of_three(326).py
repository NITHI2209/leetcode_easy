#question
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.
# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 33
#code
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        power = 1
        while power <= n:
            if power == n:
                return True
            power *= 3
        return False