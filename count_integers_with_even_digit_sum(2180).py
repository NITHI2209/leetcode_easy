#question
# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.
# The digit sum of a positive integer is the sum of all its digits.
# Example 1:
# Input: num = 4
# Output: 2
# Explanation:
# The only integers less than or equal to 4 whose digit sums are even are 2 and 4. 
#code:
class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1,num+1):
            digits = list(map(int,str(i)))
            if sum(digits)%2 == 0:
                count += 1 
        return count
