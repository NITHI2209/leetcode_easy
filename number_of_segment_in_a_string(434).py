#question
# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.
# Example 1:
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
#code
class Solution:
    def countSegments(self, s: str) -> int:
        lst = s.split()
        count = 0
        for i in lst:
            count += 1
        return count