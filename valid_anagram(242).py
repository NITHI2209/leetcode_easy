#question
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = s.lower()
        w2 = t.lower()
        s1 = sorted(w1)
        s2 = sorted (w2)
        if s1 == s2:
            return True
        else:
            return False