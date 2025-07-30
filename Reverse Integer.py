#question
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Example 1:
# Input: x = 123
# Output: 321
#code:
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            rev = -int(str(-x)[::-1])
        else:
            rev = int(str(x)[::-1])
        
        return rev if -2**31 <= rev <= 2**31 - 1 else 0
