#question
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#code:
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = []
        list1 = list(word1)
        list2 = list(word2)
        max_len = max(len(list1),len(list2))
        for i in range(max_len):
            if i < len(list1):
                a.append(list1[i])
            if i < len(list2):
                a.append(list2[i])
        result ="".join(a)
        return result