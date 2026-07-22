# 
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = {}

        words = (s1 + " " + s2).split()

        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        output = []

        for word in count:
            if count[word] == 1:
                output.append(word)

        return output