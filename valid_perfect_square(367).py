#question
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.
# Example 1:
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
#code:
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        found = False
        while i*i <= num:
            if i*i == num:
                found = True
                break
            i += 1
        return found
    # or
    num = 16
for i in range(1, num):
    if i * i == num:
        print(True)
        break
else:
    print(False)