#question
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.
#code:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = []
        b = []
        word = list(s)
        for i in word:
            if i in a:
                b.append(i)
            else:
                a.append(i)
        for j in b:
            if j in a:
                a.remove(j)
        if a :
            return s.index(a[0])
        else:
            return -1
        