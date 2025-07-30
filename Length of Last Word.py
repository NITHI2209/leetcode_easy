#question:
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#code:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(" ")
        last_word = words[-1]
        final_word = (len(last_word))
        return final_word
