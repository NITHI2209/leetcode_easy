#question
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#code
class Solution:
    def romanToInt(self, s: str) -> int:
        lst = list(s)
        for i in range(len(lst)):
            if lst[i] == "I":
                lst[i] = 1
            elif lst[i] == "V":
                lst[i] = 5
            elif lst[i] == "X":
                lst[i] = 10
            elif lst[i] == "L":
                lst[i] = 50
            elif lst[i] == "C":
                lst[i] = 100
            elif lst[i] == "D":
                lst[i] = 500
            else:
                lst[i] = 1000
        result = 0 
        for j in range(len(lst)-1):
            if lst[j] < lst[j+1]:
                result -= lst[j]
            else:
                result += lst[j]
        result = result + lst[len(lst)-1]
        return result