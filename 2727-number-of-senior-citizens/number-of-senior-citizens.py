class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            age = int(details[i][11])*10 + int(details[i][12])
            if age > 60:
                count += 1

        return count