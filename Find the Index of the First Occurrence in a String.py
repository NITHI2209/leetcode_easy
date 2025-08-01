#question
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#code:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)
        return index
# str.find() - finds whether the substring presents in the string, if substring is in the string it returns 0 or return -1 , it only checks the first occurance
