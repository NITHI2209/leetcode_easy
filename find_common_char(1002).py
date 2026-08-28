# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = list(words[0])

        for i in words[1:]:
            current = list(i)
            new = []
            for j in common:
                if j in current:
                    new.append(j)
                    current.remove(j)
            common = new
        return common
 
