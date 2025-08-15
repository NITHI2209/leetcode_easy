#question
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
# Example 4:
# Input: s = "([])"
# Output: true
# Example 5:
# Input: s = "([)]"
# Output: false
#code
class Solution:
    def isValid(self, s: str) -> bool:
        c = []
        flag = 1
        for i in s:
            if i == "(" or i == "[" or i == "{":
                c.append(i)
            elif i ==")":
                if len(c)==0 or c.pop()!="(":
                    flag = 0
                    break
            elif i == "]":
                if len(c) == 0 or c.pop()!= "[":
                    flag = 0
                    break
            elif i == "}":
                if len(c) == 0 or c.pop()!= "{":
                    flag = 0
                    break
        if flag and len(c) == 0:
            return True
        else:
            return False   