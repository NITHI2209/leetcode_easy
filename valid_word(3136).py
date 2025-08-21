#question
# A word is considered valid if:
# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.
# Return true if word is valid, otherwise, return false.
# Notes:
# 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
# A consonant is an English letter that is not a vowel.
# Example 1:
# Input: word = "234Adas"
# Output: true
#code
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel = "aeiouAEIOU"
        has_vowel = False
        has_consonant = False
        for i in word:
            if not i.isalnum():
                return False
            if i.isalpha():
                if i in vowel:
                    has_vowel = True
                else:
                    has_consonant = True
        return has_vowel and has_consonant