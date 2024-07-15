class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev_index = 0
        for i in spaces:
            result.append(s[prev_index : i])
            result.append(' ')
            prev_index = i
        
        result.append(s[prev_index:])

        return "".join(result)