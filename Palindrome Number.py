#question:
#Given an integer x, return true if x is a palindrome, and false otherwise.
#Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#code:
class Solution:
    def isPalindrome(self, x: int) -> bool:
         y = str(x)
         if y == y[::-1]:
            return True
         else:
            return False
